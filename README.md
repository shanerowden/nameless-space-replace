# nameless-space-replace v2.2
Renames files for Linux, replaces spaces and removing special characters. This is handy for Windows users who have horded files and never realized they would one day think like a CLI user.

# Usage
Type `nsr` and the program will automatically rename files in the directory (not including directories). 

# Installation
Edit nsr.sh and make sure the filepath on line 2 reflects the permenant file path of nsr.py.

Move and rename nsr.sh to bin directory without the extention using `cp nsr.sh /bin/nsr`. You will then need to `cd /bin && chmod +x nsr`. You may need to use `sudo` on both of these commands.

Move back to the permenant path of nsr.py and `chmod +x nsr.py`and you should now be able to give the command `nsr` in any directory to rename it files.


## Specific Changes From 2.1 
The `rm` dict on line 7-24 can be edited or changed. The key value pairs reflect the character to be replaced and the character to be inserted respectively. 

The `remove_enclosing` function was removed as it caused errors in file sets endng with odd numbers of repeating characters. We now just use `replace_single_character` to do the same job in fewer lines.

## Interactive Mode Option
If you would like an interactive mode (Press to Continue Mode), uncomment out line 67.


## Recursive
The program will point out directories that exist in the CWD, but note that it does not have recursive functionality yet. This is mainly a precaution. This is why I have included walk.py which you can use if you want to, but I have not included it in the main program yet because I want to see what kind of bugs we'll run into before I'm encouraging people to use it.

## Testing
Though I have tested it a bit, I'm sure there are possibly still scenarios it is not prepared to handle, but dare I say I don't believe there are many of them. Please feel free to submit issues or bugs.
