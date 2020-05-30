# nameless-space-replace 
## Shænᚱ
### version 2.3 | licensed under APGL 3.0

This simple script renames files for a CLI Linux experience without the horror of spaces or characters that cannot easily be typed: It replaces not only spaces with underscores but removes special characters and is capable of replacing any character with any character actually. 

This is handy for me as an ex-Windows user who has hoarded files and never till recently realized I would one day think like a CLI user... and hate every single file name. This can fix that.


## Usage
Type `nsr` and the program will automatically rename files in the directory (not including directories). 

I've realized I'm going to need to add some command line argument control, so those are the next things I'm working on.

## Installation
Ultimately all we need is a shell script at $PATH somewhere that we can call anywhere, and say, "Hey, you know where to find that Python3 script right? Because its in the same place as alwasy right?" and make sure both of them have permissions to execute.

This is what will allow you to use the program anywhere in any directory without having to move the py file with you to each directory where you will want to use it


First create the shell script.

Create nsr.sh and make it look like this: 

```bash
#!/bin/bash
exec /path/to/nsr.py "$@"
```

But make sure the file path on line 2 reflects the permenant file path of `nsr.py`.

You will need to move the file located at `./nsr.sh` to `/bin/nsr` -- move it and remove the extention at the end of `nsr` (if you prefer not to type the whole thing).

There are other ways to get the script on $PATH, but this is the easiest way if you can temporarily have root without there being a security concern.

## "Easy" Installation

I'm going to assume you cloned the file to `~/Git/nameless-space-replace/nsr.py` ... and are going to use that path permenantly, so.. enter all of this into the command line if you are not sure how to set this up after I explained it, but keep in mind that the first thing we're typing is the path of the file. So use the right one if yours is different.

`NSRPATH="~/Git/nameless-space-replace/nsr.py" && echo #!/bin/bash > nsr.sh && echo exec $NSRPATH "$@" >> nsr.sh && sudo chmod +x nsr.sh nsr.py && mv nsr.sh /bin/nsr` 

from that point on, you can type `nsr` in any directory, and the program will run.

### Keep in Mind...

One of the commands I told you to enter is the `sudo` command, which will elevate permissions. If you do not have permissions to move things into the `/bin/` directory or don't want to, then you'll need to add your local clone of the repo to `$PATH` or move the file with you every time you use it. All three are acceptable solutions.

## Version 2.3: 

* The dict that was formerly hardcoded no lonnger is. I programmatically gather the information to make the dict now, as it should be, and...

* I've started to include other character sets that I don't want to be seeing in my files, like for example: characters in the Russian alphabet can be removed from file names as well now. I kind of realized if I add one set of chars, I might as well add all of them, but that will come later, since it will require options.

* I also realized that, I implemented some kind of verbose/quiet functionality that I left as a commented out line that you could comment back in to the script if you wanted to toggle the option, mainly because I didn't expect anyone to actually use it -- but I realized that that is kind of unacceptable if I'm going to learn how it should be done. 

* What I'm planning to add next is `argparse` functionality, but for now, the two options are booleans on lines 10 and 11: `russian_alphabet_on` and `push_to_cont` -- which for now is better than the way it was. `True` for the first means that Russians characters will be removed from file names and on the latter, it means that you will get a very annoying interactive verbose functionality. 
* It will stop the script to ask you if each file change is acceptable, like any such flag option. I'm less concerned about using this personally now that I've seen the script run a lot. But it's there if you're not certain.

* I should probably consider cleaning up how ugly the output is either way. The information is there but it's not the prettiest thing

* I should maybe also learn to build an 'installer' or some kind of streamlines setup... because... You just can't expect everyone to know how to set up a python script unfortunately.

### Results of My Testing for Several Months And Possible Directions to Go

I have concluded that this script is fairly reliable in terms of not damaging your files or system. At first I was somewhat nervous about encouraging people to use it, because I was so certain there was some elusive circumstance I was overlooking that would destroy something. So I took some time to test it. I've used it on everything from spaces, to dollars signs, colons, Russian characters, and emojis. 

The worst case scenario is that, if your files are entirely in Russian (or other foreign character sets when I eventually add them and/or emojis in this case)... is that they could come out looking like this, except without the random nonsense characters to keep them there. What I mean is that, if the program removes every 'unique' character from a file that only has 'unique' characters, it will essentially try to rename itself something very simple., like... "___.jpg" might be a common possibility for such file names to reduce to. Suppose that this happened with multiple files... Well, what would happen is taht they would start writing over each other.

So... I will look into safe guarding that. But otherwise, this is the worst that could happen if your files are anything but all Russian.


```
26__2019_...-4ZbT3TRswvc.mp4      _-Im9jAPME-AA.mp4
26__2019_.-GQycWRa45X4.mp4        _😍😍😍-jrC97NDxJRY.mp4
27__2019_._-VzCRbj3W8Bc.mp4       People_2606_-__love_to_watch_videos-nyQEAV8w7Zw.mp4
```

Unless you are capped out in your system on such file names, which I specifically had to make a reason to put on my computer for testing...  you will more liekly end up wtih some files that look like `The_Singer_of_The_Song_-_The_Song` -- there can be an excess of duplicating characters like periods especially (due to file names that were using periods as seperators before), but in my opinion it is infintely better than this: 

```
 absolute-positioning-command        'Dysangelist - Pro
'dont shoot'                          'Dysangelist - Sub
 DontShoot.mp3                       'Dysangelist - UNt
'Dysangelist - Entropic Vision.mp3'   entropic-vision 
```

### Version History

#### Version 2.2: 
When I actually started keeping track of versions. The program seemed to work in every set of files I put it in, but I didn't trust myself to encourage anyone to use it without a warning at this time. I specifically didn't add a recursive function to apply itself to all subdirs.

#### Version 2.0 - 2.1: 
The `rm` dict that originally was on lines 7-24 was edited and changed. The key value pairs reflect the character to be replaced and the character to be inserted respectively. The `remove_enclosing` function was deprecated as it caused errors in file sets endng with odd numbers of repeating characters. We now just use `replace_single_character` to do the same job in fewer lines.

#### 1st Version: 
This program didn't even work until at least a second or third iteration, but we'll call those all the first version. Everything at this point was my shame as a brand new programmer. Believe it or not, this simple thing was a huge dysfunctional mess. If it would go any length to help anyone out there trying their best, it was the comprehension of the list comprehension that was the breakthrough in making this work.


