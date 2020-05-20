#!/usr/bin/env python3

import os, sys, string, shutil
import random, argparse
from pathlib import Path



# Initialize Paths
##################

script = Path(os.path.abspath(__file__))
description = Path.joinpath(script.parent, 'docs', 'description.txt')



# CLI Arguments
#################

parser = argparse.ArgumentParser(description=description.read_text())

parser.add_argument('-i', "--interactive", 
                    action="store_true", default=False,
                    help="Ask Confirmations on Every File Process")

parser.add_argument('-q', "--quiet", 
                    action="store_true", default=False,
                    help="Silences print to stdout making the program less text-heavy.")

# I will eventually add every character that is difficult to type but this is a start...
parser.add_argument('-R', "--russian", action="store_true", default=False,
                    help="Replace Russian Characters with random lowercase ASCII range letters")



args = parser.parse_args()




# Data Structure:
#################

# This will produce a list of punctuation and whitespace characters we don't want in file names.
rm_keys_list = [char for char in string.punctuation + 
      string.whitespace if not char in "-_+./"]


rm = dict()


if args.russian:

    # This will produce a string of all the characters in the Russian alphabet.
    russian_alphabet = ''.join([chr(i) for i in range(1040, 1104)])

    # This will add all of the alphabet characters to the dict for removal.
    for char in russian_alphabet:
        
        # It uses random lowercase characters to make sure that a directory of full Russian file names
        # would not reduce the files to such a short name that they repeatedly write over each other with the same name.
        rm[char] = random.choice(string.ascii_lowercase)

# transforms rm_keys_list into the rm dict..
for key in rm_keys_list:
    if key == ' ':
        rm[key] = ""
        # Space will become '_'
    elif key == '@':
        rm[key] = 'at'
        # @ will become 'at'
    elif key == ':':
        rm[key] = '-'
        # Colon will become '-'
    else: 
        rm[key] = ''
        # blank string removes others characters.

files_renamed = 0

# Functions:
############

def list_dir():
# will list the files in the current directory
    dir_path = os.getcwd()
    list_files = os.listdir(dir_path)
    return dir_path, list_files


def divide_files_from_dirs(listed_files):
# will remove the directories from the files
    listedfiles = []
    listeddirs = []
    for f in listed_files:
        f = os.path.abspath(f)
        if os.path.isdir(f):
            listeddirs.append(f)
            if not args.quiet:
                print(f"\tDIRECTORY: {f}")
        elif os.path.isfile(f):
            listedfiles.append(f)
    print("")
    return listedfiles

def press_to_cont(msg):
# will toggle interactive (press-to-continue) mode
    confirm = input(msg)
    print("")
    if confirm == "QUIT":
        sys.exit(1)

def count(files_to_count, file_types, path):
# counts the number of files, to determines if something looks wrong before processing
    if not args.quiet:
        print(f"There are {len(files_to_count)} {file_types} in {path}\n")

def list_files(file_list):
# will output the files without the directories to the terminal
    for f in file_list:
        if not args.quiet:
            print(f"FILE: {f}")
    print("")

def relist():
# will reflect the changes made after each replace_single_charater() call
    cwd, ls = list_dir()
    files = divide_files_from_dirs(ls)
    return files

def collision_of_files(og_filename: str, potential_filename: str, files_in_cwd: list):
# Check if file already Exists
    potential_path = Path(potential_filename)
    og_path = Path(og_filename)
    if potential_path.exists():
        return True
    elif og_filename in files_in_cwd:
        return True
    else:
        return False
    

def only_underscores_check(p):
    for char in p:
        if not char == "_":
            return False, "_"
    
    rand = random.choice(string.ascii_letters.split(''))
    
    return True, rand
    

def replace_single_char(char_to_remove, char_to_insert, file_list):
# will replace a single character at a name and rename the files. This is why the relist is necessary.
    
    global files_renamed
    files = [f for f in file_list if char_to_remove in f]
    count(files, f"files with '{char_to_remove}'", os.getcwd())
    
    if args.interactive:
        press_to_cont("Press to Continue or type 'QUIT' > ")
        
    for f in files:
        # Alias original filepath
        old = f
        
        # Make sure only editing relative filepath
        f = f.split(os.sep)
        f = f[-1]
        
        # cut out characters
        split = f.split(char_to_remove)
        resplit = char_to_insert.join(split)
        new = os.path.abspath(resplit)
        
        # rename
        only_underscores, rand = only_underscores_check(new.split(os.sep)[-1])
        if only_underscores:
            new_name = rand + new.split(os.sep)[-1]
            new = os.path.abspath(new_name)
        shutil.move(old, new)
        files_renamed += 1
    
    if not args.quiet:
        print(f"files with '{char_to_remove}' renamed with '{char_to_insert}'")
    
    # Make sure that file list reflects changes
    files = relist()
    return files



# Main 
#######

def main(rm_dict):
    cwd, ls = list_dir()
    count(ls, "files and directories", cwd)
    files = divide_files_from_dirs(ls)

    if args.interactive:
        press_to_cont("""\tScript does not currently have recursive functionality,\n\t 
            so all files inside these directories will not be processed.\n\n
            Press RETURN to Continue or type 'QUIT'\n >""")
        
    count(files, "files to process", cwd)
    list_files(files)

    for k, v in rm_dict.items():
        files = replace_single_char(k, v, files)
    

    print(f"Process Complete.\n\t{files_renamed} files were renamed")
        


if __name__ == '__main__':
    main(rm)
