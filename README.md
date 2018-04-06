# dwangoACDrawAssist
Python scripts to assist with using the pbn (paint by number) part of dwangoAC's chat.

All of my scripts are in Python3. Sorry for any inconvience.<br>
The first script is convert.py.<br>
YOU MUST HAVE PYGAME INSTALLED!<br>
Pygame is used both as a GUI for the script as well as the backend, and is therefore very required.<br>
<code>pip install pygame</code><br>
should be suffecient for most systems. The program is controlled with the arrow keys and enter. By default, it will look for png files in a subfolder called assets. This can be changed by editing the line 13:<br>
<code>for img in glob.glob("assets\\*.png"):</code><br>
change "assets\\" to any subfolder you like, or remove it to search the directory that the script is in.<br>
change ".png" to your desired filetype that is also within the following:<br>
JPG, PNG, GIF (non-animated), BMP, PCX, TGA (uncompressed), TIF, LBM (and PBM), PBM (and PGM and PPM), and XPM.<br>
Example: "*.png", "folder\\subfolder\\subsubfolder\\*.gif"<br>
Up and down arrow keys will cycle through all of the valid files in the given directory. Press enter to select a file. Then, use the up and down arrow keys to change the y-offest and left and right arrow keys to change the x-offset. Press enter to generate the text file, which will be placed in the same folder as the image.<br><br>
The second script is post.py.<br>
This script has no dependencies that are not installed by default with Python3. However, the file will need to be supplied with a Twitch username and oAuth token.<br>
Twitch links to this site for getting your oAuth token:<br>
<url>https://twitchapps.com/tmi/</url><br>
As always, never give your personal information to someone you do not trust. Feel free to aquire your oAuth token in any way you desire.<br>
The script can be run with parameters in the command line, in which the first will be used as the path of the file and the rest ignored. If run without parameters, it will ask for a file path on runtime. It will then create a socket connection to Twitch IRC, specifically to the pbn room on dwangoAC's channel. It will then send a chat message for every line of the text file, empty lines ignored, every two seconds until all the lines have been posted, then it will close itself.<br>
Example: <code>python post.py</code> or <code>python post.py "folder/image.png"</code><br><br>
Please post an issue with any errors you encounter.
