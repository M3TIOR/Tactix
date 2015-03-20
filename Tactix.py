#!/usr/bin/python
#This is the old version of Tactix befor I decided to make the C version.
#I hope you all like it.

#I wanted to include it to make sure even if you only have a monochrome display you can still play!
#	* HORRAY FOR GAMERS!

#I may very well have modded this a bit too, just so it feels more like the full version.

import os #needed for screen clear call.

#I had to grab this off of stack overflow...
#WHAT?! I NEVER SAID I WAS THE BEST PROGRAMMER ON THE PLANNET!
def getTerminalSize():
	import os
	env = os.environ
	def ioctl_GWINSZ(fd):
		try:
			import fcntl, termios, struct, os
			cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,'1234'))
        	except:
			return
		return cr
	cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
	if not cr:
		try:
			fd = os.open(os.ctermid(), os.O_RDONLY)
			cr = ioctl_GWINSZ(fd)
			os.close(fd)
		except:
			pass
		if not cr:
			cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

		### Use get(key[, default]) instead of a try/catch
		#try:
		#    cr = (env['LINES'], env['COLUMNS'])
		#except:
		#    cr = (25, 80)
	return int(cr[1]), int(cr[0])

###MY_CODE \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

#initiate our character size data so we can calculate how large our screen can be.
#this kindof sucks because doing screen size calculations this way means the user can't
#resize the game without screwing it up...

class grid:
	def 
	__init__(self,x,y,target):
		def append_data:
			
		size = x*y
		self.data = [size]
		if target == "stdout"
			self.target = print
	
	
	
	#pushes data to console.
	def flush():
		os.system("clear")

global character_field
character_field = grid(getTerminalSize())

#text orientation.
def t_orient(text,x,y):
	#quadrants work as such
	#
	#    +-----------------+
	#    |     |     |     |
	#    | 0,0 | 1,0 | 2,0 |
	#    +-----------------+
	#    |     |     |     |
	#    | 0,1 | 1,1 | 2,1 |
	#    +-----------------+
	#    |     |     |     |
	#    | 0,2 | 1,2 | 2,2 |
	#    +-----------------+


class main_menu:
	def draw():
		
	def context():
		

class game:
	main = menu();

class ai:
	



#MAIN_CODE

def main():
	


#finally we call to main.
main()
