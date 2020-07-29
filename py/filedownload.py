import os, time
while True :
	configfile = open('../config/config.dat','r')
	url_cache = open('../config/urlcache.dat','r')

	for configline in configfile :

		if configline[0:6] == 'ripper' :

			ripper = (configline[8:len(configline)-2])
			print('Ripper has been found! Beginning download...')

		if configline[0:8] == 'cooldown' :

			timer = (configline[10:len(configline)-2])
			print('Cool down timer set.')


	for url in url_cache :

		ripper_string = 'python3 ' + ripper + ' ' + url
		os.system(ripper_string)
		time.sleep(int(timer))

		os.system('clear')

		print ('Downloaded: ' + url)

	url_cache.close()

	os.system("ls ../data/cache/* > ../data/filecache.dat")
