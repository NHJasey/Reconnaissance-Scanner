import sys, urllib2

ofile = "dirs.txt"

fil = open(ofile,'w')

dirs = fil.readlines()

for x in dirs:
	response = urllib2.urlopen('http://python.org/'+x)
	html = response.read()
