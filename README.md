<h1>Afterhours API (not really but go off)</h1>
<body>
Afterhours is a script that is meant to post images to Twitter automatically. It runs with other scripts so as to make itself self sustainable. 
When the image database is considered empty it will refresh it with new images from reddit where you find you can find your dank may mays or 
hentai or whatever you jerk off to and repost it to the specific account that you have set up to post them along with the original author. 
<br>
<h1>Installation</h1>
<hr>
Installing this sucker is pretty easy. Just copy and paste this into your command line along with any permissions you need in order to make apt happy with you.

<code> wget github.com/After-Hours-Bot/Afterhours-API/ahinstall.sh && sh ./ahinstall.sh </code>

Once copied into the terminal and executed, the installer will install the necessary stuff required by the bot to function as well as get the <a href="https://github.com/thisisppn/reddit-media-downloader">reddit.py</a>
from their proper source. It may ask you if you are planning on running this from a pi or as an automatically executed script I dunno yet tho since it's 6:43 AM rn
I'm fucking tired and I still dont have it uploaded yet.

<h1> Configuring </h1>

If you don't have a Twitter Developer account setup, make sure you set it up at Twitters <a href="dev.twitter.com">Developer</a> site before you continue
since you need a developer account in order to get started.

<h2>Setup With New Developer Account</h2>
<br>
Your setup process will be different from other users if you are setting up a new account since you won;t have the necessary keys for the bot to use in order 
to login to Twitter.

Be sure to make a new app by going here:<a href="https://developer.twitter.com/en/portal/apps/new"> https://developer.twitter.com/en/portal/apps/new </a> 

From here you will name your app, and copy both the API Key and API Secret Key. Make sure to store them since they will be needed.

Click the 'get user tokens link'

After that you will then click 'Generate' button in the access token and secret box.

Copy both the Access Token and Access Token Secret and store them as well.

<h2>Setup Existing Developer Account</h2>
<br>
Copy your current API Key, API Secret Key, Access Token, and Access Token Secret.

Open 'bot.py' in an editor of your choosing.

Paste the keys to their corresponding field.

Go to: <a href="http://gettwitterid.com/">http://gettwitterid.com/</a> and enter the admin account username. (This is meant for the bot to send DMs)

Paste the ID into the "admin_id" field.

Open 'subs.txt' and enter in the subreddits you want to rip.

<h1>Starting The Bot</h1>
<br>
Just type in <code>python3 ./bot.py</code> and the bot will automatically send you a DM stating it is up and is downloading content. This will take a
while depending on how many subreddits you entered, butit  should only request a reboot and start back up again to allow the bot to post.


<h1>Built In Samba Drive</h1>
<br>
This feature is meant to allow you to maintain what is on your pi while it powered on. You will have access to the filesystem, the content (images), bot files, and permissions.
The password for the '<code>root</code>' and '<code>pi</code>' is <code>0000</code>. You can disable it by going into the permissions folder and replacing the '<code>smb.conf</code>' with the '<code>lockdown</code>' file provided.
