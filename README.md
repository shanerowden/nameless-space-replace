# nameless-space-replace v2.1
Renames files for Linux, replaces spaces and removing special characters. This is handy for Windows users who have horded files and never realized they would one day think like a CLI user.

# Usage
Type `nsr` and the program will automatically rename files in the directory (not including directories). 

# Installation
Edit nsr.sh and make sure the filepath on line 2 reflects the permenant file path of nsr.py.

Move and rename nsr.sh to bin directory without the extention using `cp nsr.sh /bin/nsr`. You will then need to `cd /bin && chmod +x nsr`. You may need to use `sudo` on both of these commands.

Move back to the permenant path of nsr.py and `chmod +x nsr.py`and you should now be able to give the command `nsr` in any directory to rename it files.


## Specific Changes
The following lines 107 - 124 can be edited or changed.
They reflect in the first parameter, the caracter to be replaced and in the second parameter, the character to be inserted.

```
files = replace_single_char(' ', '_', files)
files = replace_single_char("[", '', files)
files = replace_single_char("]", '', files)
files = replace_single_char("{", '', files)
files = replace_single_char("}", '', files)
files = replace_single_char("!", '', files)
files = replace_single_char("$", '', files)
files = replace_single_char("&", '', files)
files = replace_single_char("*", '', files)
files = replace_single_char("%", '', files)
files = replace_single_char("@", 'at', files)
files = replace_single_char("(", '', files)
files = replace_single_char(")", '', files)
files = replace_single_char("#", 'no', files)
files = replace_single_char(':', '-', files)
files = replace_single_char(';', '', files)
files = replace_single_char('"', '', files)
files = replace_single_char("'", '', files)
```

## Interactive Mode Option
If you would like an interactive mode (Press to Continue Mode), uncomment out line 78.


## Recursive
The program will point out directories that exist in the CWD, but note that it does not have recursive functionality yet. This is mainly a precaution. This is why I have included walk.py which you can use if you want to, but I have not included in the program yet because I want to see what kind of bug we'll run into befopre I'm encouraging people to use it.

## Testing
Though I have tested it a bit, I'm sure there are possible still scenarios it is not prepared to handle, but dare I say I don't believe there are many of them. Please feel free to submit issues or bugs.
