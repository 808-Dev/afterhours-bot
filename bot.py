import tweepy, time, os
from datetime import datetime

def sleep_timer():

    time.sleep(300)

os.system('clear')
API_KEY = ''
API_SECRET = ''
API_ACCESS_TOKEN = ''
API_SECRET_TOKEN = ''
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(API_ACCESS_TOKEN, API_SECRET_TOKEN)
api = tweepy.API(auth)
admin_id = 1234567890
cache = open('cache.log','r')
error_in_last_tweet = False
dbstat_complete = False
error_exists = True

api.send_direct_message(admin_id,'I am now online!')
for filename in cache:

    message_file = open('message.txt','r')
    artist = filename[filename.find('(')+1:filename.find(')')]
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    message = ('Artist: ' + artist + ' has been cited! Sending tweet at: ' + current_time)
    label = filename[filename.find('[')+1:filename.find(']')]
    tweet_content = ('Artist: ' + artist + message_file.readline())

    try:

        try:
            if error_exists == True:
                print('Bypassing timer')
                error_exists = False
            else:
                sleep_timer()

        except KeyboardInterrupt:

            print ('Cancelling...')

        api.update_with_media(filename[:len(filename)-1], tweet_content)
        print ('Success! Tweet has been sent.')

        if error_in_last_tweet == True:

            api.send_direct_message(admin_id,'Issue has been resolved.')
            error_in_last_tweet = False

        else:

            error_in_last_tweet = False

    except:
        errorexists = True
        ratelimittest = 1
        print ('Notifying an admin...')
        exception_contents = 'I had an error sending "' + filename + '". File may be corrupt.'
        api.send_direct_message(admin_id,exception_contents)
        error_in_last_tweet = True
        dbstat_complete = True

api.update_status('Image database has been completed. Please wait while the database is updated.')

length_data = open('subs.txt','r')
length_of_file = 0
stage = 0

for throw_away_data in length_data:
    length_of_file = length_of_file + 1
    sub_reddits = open('subs.txt','r')

for sub in sub_reddits:

    stage = stage + 1
    download_command = 'sudo python3 reddit.py '+ sub
    os.system(download_command)
    stage_info = 'Stage ' + str(stage) + ' of ' + str(length_of_file) + ' has been completed.'
    api.send_direct_message(admin_id,stage_info)

    if stage == length_of_file:

        api.send_direct_message(admin_id,'Database has been updated! Posting will resume shortly.')
        api.update_status('The database has been updated. Posting will restart shortly.')
        os.system('rm -f cache.log')
        os.system("find . -iregex '.*\.\(jpg\|gif\|png\|jpeg\)$' -mtime -7 -size -3M > cache.log")
        os.system("find . -iregex '.*\.\(jpg\|gif\|png\|jpeg\)$' -mtime +7 > removal_list.log")
        rmfilelist = open('removal_list.log','r')
        cache = open('cache.log','r')

        for removable_file in rmfilelist:

            removal_command = 'rm ' + removable_file
            os.system(removal_command)

os.system('sudo reboot')
