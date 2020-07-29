import time, os, sys, tweepy
os.system('cd config')
configfile = open('../config/config.dat')

for configline in configfile :

	if configline[0:7] == 'message' :

		inputline = (configline[9:len(configline)-2])

		print('Custom message set.')

	if configline[0:5] == 'timer' :

		sleeptime = (configline[7:len(configline)-2])

		print('Timer has been set.')

	if configline[0:5] == 'admin' :

		admin = (configline[7:len(configline)-2])

		print('Administrator account set. [Not implemented yet]')

	if configline[0:9] == 'interface' :

		interface = (configline[11:len(configline)-2])

		print('Interface set.')

	if configline[0:4] == 'mods' :

		modsfolder = (configline[6:len(configline)-2])

		print('Mod folder set...')

	if configline[0:7] == 'rippers' :

		ripfile = (configline[9:len(configline)-2])

		print('Ripper has been set.')

	if configline[0:10] == 'silentmode' :

		nothing = (configline[12:len(configline)-2])

		print('Silent mode set.')

	if configline[0:6] == 'runmod' :

		modfile = (configline[8:len(configline)-2])

		print('Mod loading...')

	if configline[0:9] == 'filecache' :

		cache = open((configline[11:len(configline)-2]),'r')
		modcache = open((configline[11:len(configline)-2]),'r')

		print('File cache set up.')

	if configline[0:6] == 'output' :

		fileout = open(configline[8:len(configline)-2],'w')

		print('Output file set.')

	if configline[0:8] == 'imgcache' :

		imgcache = configline[8:len(configline)-2],'w'

		print('Output file set.')

	if configline[0:11] == 'badwordfile' :

		banwords = open(configline[13:len(configline)-2],'r')

		print('Bad words file configured.')

		banwordfile = open(banwords,'r')

		print('Bad words file opened.')

	if configline[0:7] == 'api_key' :

		def api_keys():
			api_key = configline[7:len(configline)-2]

	if configline[0:5] == 'start' :

		if configline[7:12] == 'false' :

			print('Seriously?')

		if configline[7:11] == 'true' :

			print('Thank god.')
			print('API set up.')
			keyfile = open('../config/keys.dat','r')

			api_key = keyfile.readline()
			API_KEY = api_key[:len(api_key)-1]

			api_secret = keyfile.readline()
			API_SECRET = api_secret[:len(api_secret)-1]

			api_access_token = keyfile.readline()
			API_ACCESS_TOKEN = api_access_token[:len(api_access_token)-1]

			api_secret_token = keyfile.readline()
			API_SECRET_TOKEN = api_secret_token[:len(api_secret_token)-1]

			auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
			auth.set_access_token(API_ACCESS_TOKEN, API_SECRET_TOKEN)
			api = tweepy.API(auth)

			for imagefile in cache :

					filename = imagefile[:len(imagefile)-1]
					print('filename'+filename)
					artist = filename[filename.find('(')+1:filename.find(')')]
					print('Filtered Name: '+artist)
					print('File sending: '+filename)
					print('Message sent with file: '+inputline+'a'+artist)
					api.update_with_media(filename,  inputline + ' '+artist)
					print('File sent.')

					time.sleep(int(sleeptime))
