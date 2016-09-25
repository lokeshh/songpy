#!/usr/bin/env python2.7

from google import search
from os import system

song_name = raw_input('Enter song name: ')
video = raw_input('Do you want video? (y/n): ') == 'y'
result = search(song_name).next()
if video:
	system('youtube-dl ' + result)
else:
	system('youtube-dl -f bestaudio ' + result)


