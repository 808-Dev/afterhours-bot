import os
while True :

	stringfile = open('urllist.dat','r')

	for url in stringfile :

		command = 'java -jar /Network/BOT1/ripme.jar -u ' + url
		os.system(command)

	print ('DOWNLOAD COMPLETE.')
	stringfile.close()
	command = "find . -iregex '.*\.\(jpg\|gif\|png\|jpeg\)$' -mtime 0 > filelist.dat"
	os.system(command)
