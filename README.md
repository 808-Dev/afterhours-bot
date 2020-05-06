# AfterHours-API

Image hosting platform for cross posting.

Setup for After Hours (Bot) API

The bot once out of BETA phase will coded for cross platform use (Windows, *nix, and Mac OS systems).
Until then the bot will only be able to run under Linux or Mac OS based systems, since their file
architecture vary from the normal Windows architecture. (It may be possible I just never tried it or
thought it was worth trying.)

SETUP

1. Download ripme to be able to rip files from sites and etc. (If you haven't installed Java JRE download that as well. 
   Or if your on a linux distro, just run 'sudo apt-get install java-common -y' to install it.)
    'https://github.com/RipMeApp/ripme'
    'https://www.java.com/en/download/manual.jsp' <- Java
    
2. Create a Twitter developer account. This is neccessary to share content to Twitter. Goto 'dev.twitter.com' and fill out
   any questions asked. If you are planning on making the bot post seperate from what you post, you will need to make a new
   account. After the account is setup proceed to create an 'App'. Once complete you will be given window displaying your apps
   key and tokens. Generate the secret keys and tokens, these keys are important so make sure to keep them in a file if they
   need to be used in the future.
   
3. Use 'git clone https://github.com/After-Hours-Bot/AfterHours-API/' to download the required files. (On Windows systems this
   may be different.)

4. Open 'tempbot.py' in an editor and paste the contents of the four keys from the window into the corresponding variables 
   while keeping the quotations. 
   
5. If you are planning on running the bot from somewhere other than /, you may want to change the paths to your selected path.


6. Create a file named 'urllist.dat'. This will give the ripper a URL to scrub through. (providing it accepts it)

7. Open 'Ripme.jar' and configure the output taget to be where you plan on the bot getting its information from

8. Copy all the contents of the bot to the folder containing where it should get its files from. 
   (yeah I know its stupid shut up.)
   
9. Run the thing and leave me alone to die in pain filled agony.
