import tweepy, time, os
os.system('clear')
API_KEY = ''
API_SECRET = ''
API_ACCESS_TOKEN = ''
API_SECRET_TOKEN = ''

msg = "After Hours API BETA V.0.0.3"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(API_ACCESS_TOKEN, API_SECRET_TOKEN)
api = tweepy.API(auth)

print ('Starting ' + msg + '...')

filelist = open('filelist.dat','r+')


while True:

    for filename in filelist :

        killfile = open('killfile.dat')

                         #Kill file

        for arg in killfile :
            print('Checking kill file...')
            if arg != '' :
                exit()
        filename = filename
        asmr = filename[2:-1]

        if asmr == 'tempbot.py' :
            break
        if asmr == 'filelist.dat' :
            break
        if asmr == 'killfile.dat' :
            break

        message = 'kdialog --title "Uploading" --passivepopup \ "Filename: ' + asmr + ' - Sending tweet at: ' + time.asctime() + '." 10'
        print ('Upoading "' + asmr + '"...')
        if asmr != '' :
            api.update_with_media(asmr, msg)

            os.system(message)
            time.sleep(1200)

    #Content update.

    #os.system('java --jar ripme.jar -r')
    #os.system('find -type f -size -3M > filelist.dat')
    #dirlist = open('filelist.dat')
    #for directory in dirlist :

        #message = 'kdialog --title "Download Complete!" --passivepopup \ "Directory: ' + directory + ' - Downloaded. Copying contents!" 10'
        #os.system(message)
        #dir = directory[:2]
        #os.chdir(dir)
        #dirfile = 'cp * /root/content/TEMP/'
        #os.shell(dirfile)
        #os.chdir('..')
