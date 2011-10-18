#/usr/bin/env python

# this is a ping program using scapy
import sys
import getopt
from scapy.all import sr1,IP,ICMP


def ping(host, repeat=4):
	packet = IP(dst=host)/ICMP()
	for x in range(repeat):
		response = sr1(packet)
		response.show()

def usage():
	print "ping.py <hostname>"

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hd:v", ["help", "dest="])
	except gotopt.GetoptError, err:
		#print help information and exit
		print str(err) # will print something like "option -a not recogniszed"
		usage()
		sys.exit(2)
	output = None
	verbose = False
	for o, a in opts:
		if o == "-v":
			print "version 0.1"
		elif o in ("-h", "--help"):
			usage()
			sys.exit()
		elif o in ("-d", "--dest"):
			host = a
		else:
			assert False, "unhandled option"

		ping(host, 2)

if __name__ == '__main__':
	main()
