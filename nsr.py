#!/usr/bin/env python3

#from pathlib import Path
import os, sys, string, shutil
import argparse, subprocess, requests
#from colorama import Fore, Style, Back



# Options
#################

russian_alphabet_on = True
push_to_cont = False

# I know that these should be argparse options. They probably will be sooner or later.



# Data Structure:
#################

# This will produce a list of punctuation and whitespace characters we don't want in file names.
rm_keys_list = [char for char in string.punctuation + 
      string.whitespace if not char in "-_+."]

if russian_alphabet_on:
	
	# This will produce a string of all the characters in the Russian alphabet.
	russian_alphabet = ''.join(
		[chr(i) for i in range(1040, 1104)])

	# This will add all of the alphabet characters to the list.
	for chr in russian_alphabet:
		rm_keys_list.append(chr)

# This transforms list into the dict.
rm = dict()
for key in rm_keys_list:
	if key == ' ':
		rm[key] = "_"
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



# Fucntions:
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
    print(f"There are {len(files_to_count)} {file_types} in {path}\n")

def list_files(file_list):
# will output the files without the directories to the terminal
    for f in file_list:
        print(f"FILE: {f}")
    print("")

def relist():
# will reflect the changes made after each replace_single_charater() call
    cwd, ls = list_dir()
    files = divide_files_from_dirs(ls)
    return files

def replace_single_char(char_to_remove, char_to_insert, file_list):
# will replace a single character at a name and rename the files. This is why the relist is necessary.
    
    global files_renamed
    files = [f for f in file_list if char_to_remove in f]
    count(files, f"files with '{char_to_remove}'", os.getcwd())
    
    if push_to_cont:
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
        shutil.move(old, new)
        files_renamed += 1
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
	
	press_to_cont("\tScript does not currently have recursive functionality,\n\t"\
		+ "so all files inside these directories will not be processed.\n\n"
		+ "Press RETURN to Continue or type 'QUIT'\n >  ")
	
	count(files, "files to process", cwd)
	list_files(files)

	for k, v in rm_dict.items():
		files = replace_single_char(k, v, files)

	print(f"Process Complete.\n\t{files_renamed} files were renamed")
	
if __name__ == '__main__':
	main(rm)
