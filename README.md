<h1>Afterhours-bot 5.0</h1>
<body>
Afterhours is a batch of scripts that are meant to post images to Twitter automatically. They work together to make the bot sustain a good flow of content to your audience. When the content runs out, the bot will download more and delete unneeded content from itself. (bad explaination but nobody looks at this so you get what you get.)
<br>
  <h1>Prerequisites</h1>
  1. Raspberry Pi (Unless you have unlimited systems to waste money on)
  2. Internet (duh)
  3. 16gb sd card with Raspbian (Raspberry OS) lite installed
  4. a bit of linux know how.
<br>
<h1>Installation</h1>
<hr>
Installing this sucker is pretty easy if you already know a bit of linux. 
Make sure you install the required apps in order to get it running.
<code>sudo apt update && sudo apt install python3 python3-pip -y && pip install tweepy requests</code>
  <br>
You will also want to install a ripper for the bot to use. The one I use (and that the bot has built in support for) can be found here: <a href="https://github.com/thisisppn/reddit-media-downloader">https://github.com/thisisppn/reddit-media-downloader</a>. Just copy it to the main folder that <code>bot.py</code> is located in, and you will be good to go. Otherwise you may need to edit the <code>download_command</code> variable to support what you are using.
<h1>Setup</h1>
<hr>
You will need to enter your API Keys and the administration user ID for the bot in order to get it to start posting images.
You can do this by editing the <code>bot.py</code> file and dropping the API keys into their own fields, and by entering the administrators user id in the <code>admin_id</code> field. 
<br>
Next, you will want to add subreddits for the bot to look for. To do this simply open the <code>subs.txt</code> file, and enter the subreddits (leaving out the r/) from the names. To download more than one, simply seperate the subs by putting them on different lines. 
<br>
Finally, the last thing you will have to do is edit the <code>message.txt</code> file. This will be used when sending out a custom message for your bot to post. The author name will already be taken care of, so you enter in some hashtags and other stuff.
<br>
After all that, you are now free to start the bot by entering this command into the command line: <code>python3 bot.py</code>
The system will restart when completed, and will send you back to the login screen. (If you don't want to have to restart the bot manually everytime you turn the system on, add the command to the end of the </code>.bashrc</code> file in your user directory.)
