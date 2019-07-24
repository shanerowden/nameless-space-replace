#!/usr/bin/env python3

import os
import sys
import shutil

rm = {' ': '_',
      '[': '',
      ']': '',
      '{': '',
      '}': '',
      '!': '',
      '$': '',
      '&': '',
      '*': '',
      '%': '',
      '@': 'at',
      '(': '',
      ")": '',
      "#": 'no',
      ':': '-',
      ';': '',
      '"': '',
      "'": ''}

def list_dir():
    dir_path = os.getcwd()
    list_files = os.listdir(dir_path)
    return dir_path, list_files

def divide_files_from_dirs(listed_files):
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
    confirm = input(msg)
    print("")
    if confirm == "QUIT":
        sys.exit(1)

def count(files_to_count, file_types, path):
    print(f"There are {len(files_to_count)} {file_types} in {path}\n")

def list_files(file_list):
    for f in file_list:
        print(f"FILE: {f}")
    print("")

def relist():
    cwd, ls = list_dir()
    files = divide_files_from_dirs(ls)
    return files

def replace_single_char(char_to_remove, char_to_insert, file_list):
    global files_renamed
    files = [f for f in file_list if char_to_remove in f]
    count(files, f"files with '{char_to_remove}'", cwd)
    #press_to_cont("Press to Continue or type 'QUIT' > ")
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

files_renamed = 0
cwd, ls = list_dir()
count(ls, "files and directories", cwd)
files = divide_files_from_dirs(ls)
press_to_cont("\tScript does not currently have recursive functionality,\n\tso all files inside these directories will not be processed.\n\nPress RETURN to Continue or type 'QUIT' >  ")
count(files, "files to process", cwd)
list_files(files)
for k, v in rm.items():
    files = replace_single_char(k, v, files)

print(f"Process Complete.\n\t{files_renamed} files were renamed")
