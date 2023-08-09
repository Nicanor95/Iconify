# Iconify
 Makes icons for all directories inside the directory the script is executed.
 the --directory option doesn't rarely works honestly so don't try it, just 
 cd to the desired directory and execute the script
 
 It grabs an image from inside the directory and turns it into a 256x256 icon, example:
 
 ```
 mydirectory ─┬ stuff.txt
              └ image.png
 ```
 
 Turns into:
 
 ```
 mydirectory ─┬ stuff.txt
              ├ desktop.ini (hidden)
              ├ icon.ico
              └ image.png
 ```
 
 If an icon doesn't show try changing the capitalization of `icon.ico` or `desktop.ini` otherwise
 you may clean windows icon cache.
