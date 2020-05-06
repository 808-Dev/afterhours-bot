import tweepy, time, os
os.system('clear')
API_KEY = ''
API_SECRET = ''
API_ACCESS_TOKEN = ''
API_SECRET_TOKEN = ''
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(API_ACCESS_TOKEN, API_SECRET_TOKEN)
api = tweepy.API(auth)

file = open('filelist.dat','r')
fileout = open('output.dat','w')
for line in file :
	fail = False
	fileout.write ('Test line: '+line)
	line1 = line[line.find('___')+3:]

	if line1[3:].find('___') != -1 :

		fileout.write (line1)
#		break


	line2 = line1[:line1.find('_')]

	if line2.find('___') == -1 :
		line3 = line2[:line1.find('___')]
#		fileout.write('Triple Score Trim: '+line3+'\n')
		final_test = line3.lower()

	if line2.find('_') == -1 :
		line3 = line2[:line1.find('_')]
#		fileout.write('Underscore Trim: '+line3+'\n')
		finaltest = line3.lower()

	if line2.find('-') != -1 :
		line3 = line2[1+line2.find('-'):]
#		fileout.write('Hyphen Trim: '+line3+'\n')
		finaltest = line3.lower()

	if line2.find('-') == -1 :
#		fileout.write('No Trim: '+line2+'\n')
		finaltest = line2.lower()
	fileout.write( finaltest+'\n')
	fail = False
	if finaltest == 'm' :
		fileout.write('Failed to acquire User ID from file: ' + line+'\nReason: Gender was tagged.\n\n')
		fail = True
	if finaltest == 'f' :
		fileout.write('Failed to acquire User ID from file: ' + line+'\nReason: Gender was tagged.\n\n')
		fail = True
	if finaltest == 'mm' :
		fileout.write('Failed to acquire User ID from file: ' + line+'\nReason: Gender was tagged.\n\n')
		fail = True
	if finaltest == 'ff' :
		fileout.write('Failed to acquire User ID from file: ' + line+'\nReason: Gender was tagged.\n\n')
		fail = True
	if finaltest == 'mf' :
		fileout.write('Failed to acquire User ID from file: ' + line+'\nReason: Gender was tagged.\n\n')
		fail = True
	if finaltest == 'fm' :
		fileout.write('Failed to acquire User ID from file: ' + line+'\nReason: Gender was tagged.\n\n')
		fail = True
	if finaltest.find('Network') != -1 :
		fileout.write('Failed to acquire User ID from file: ' + line+'\nReason: Path was tagged.\n\n')
		fail = True
	if finaltest == '' :
		fileout.write('Failed to acquire User ID from file: ' + line+'\nReason: Empty string.\n\n')
		fail = True
	if fail == False :
		msg = 'Original Credit to: ' + finaltest + '. @botnamehere #bottybot #bot '
		path = '/path/subpathifyouwant(Noslash)'+line[1:]
		print (path)
		api.update_with_media(line[:len(line)-1], msg)
		print ('Sent File Successfully.')
		time.sleep(1200)
