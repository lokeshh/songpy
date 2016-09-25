#!/usr/bin/env python2.7

from google import search
from os import system
import sys

sys.argv.pop(0)
if sys.argv[0] == '-v':
	video = True
	sys.argv.pop(0)
else:
	video = False

song_name = ' '.join(sys.argv)
result = search(song_name).next()
if video:
	system('youtube-dl ' + result)
else:
	system('youtube-dl -f bestaudio ' + result)


