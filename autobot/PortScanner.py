#!/usr/bin/python

# Simple nmap scan using python-nmap module
# Code ripped from sample in documentation 
# http://xael.org/pages/python-nmap-en.html

import nmap

def ScanMe(ip, port_range) :

	nm = nmap.PortScanner()
	nm.scan(ip, arguments = '-n -sT -p' +port_range)

	result = ''

	for host in nm.all_hosts():
		for proto in nm[host].all_protocols():
			lport = nm[host][proto].keys()
			lport.sort()

			for port in lport:
                                
				result += '%s (%s)\t' % (port, nm[host][proto][port]['state'])


	return result


if __name__ == '__main__' :
	print 'Running test scan'
	print ScanMe('scanme.nmap.org','22-445')
	print 'Scan complete exiting'


