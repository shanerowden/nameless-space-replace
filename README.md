# nameless-space-replace v2
Renames files for Linux, replaces spaces and removing special characters

For `remove_enclosing`, the first two parameters can be changed so enclosing characters to be removed. In `replace_single_char`, the first param is the character to be removed, and the second is the character to be inserted. You can add lines like these to the script to make other operations. `remove_enclosing` should precede all `replace_single_character` operations.

```
files = remove_enclosing("(", ")", files)
files = remove_enclosing("[", "]", files)
files = remove_enclosing("{", "}", files)
files = replace_single_char(' ', '_', files)
files = replace_single_char('"', '', files)
files = replace_single_char("'", '', files)
```

These operations will only affect the CWD. I put nsr.sh in my `/bin/` dir so that I can call it anywhere. You may need to edit this shell script to reflect the appropriate file path of nsr.py.

The program will point out directories that exist in the CWD, but note that it does not have recursive functionality yet. This is mainly a precaution.

Though I have tested it a bit, I'm sure there are scenarios it is not prepared to handle. Please feel free to submit issues or bugs.
