from exception import *
from clientlib import *
from shell import *
import sys, getopt
import settings.py

def main(argv):
	if not argv:
		usage()
		sys.exit()
	hostname=argv[0]
	port=21
	username='anonymous' #Default username
	password='anonymous@' #Default Password

	try:
		opts,args = getopt.getopt(argv[1:],"hp:u:P")
		
	except getopt.GetoptError:
		''' Invalid arguments'''
		raise getopt.GetoptError('Invalid Paramaters')
	else:
		for opt,arg in opts:
			if opt == '-h':
				'''Display help'''
				pass
			elif opt == '-p':
				'''Custom port number provided'''
				try:
					port = int(arg)
				except Exception,e:
					'''Invalid port number error'''
					raise InvalidPortNumberError('Please enter a valid port number')
					sys.exit()

			elif opt == '-u':
				username = arg
				password=''
			elif opt == '-P':
				password = arg

		try:
			sh = Shell(CLIENT(hostname,port,username,password))
		except Exception,e:
			print e

def usage():
	print 'Usage:'
	print 'pyftp <hostname> -p <portnum> -u <username> -P <password>'
	print 'optional parameters:'
	print '-p: Default set to 1'
	print '-u: Default is anonymous'
	print '-P: Default is anonymous@'

if(__name__=='__main__'):
	main(sys.argv[1:])
