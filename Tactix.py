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
#resize mid gameplay without screwing it up...

class grid:
	edge='+'
	line_x='-'
	line_y='|'
	
	def __init__(self,width,height):
		self.width=width
		self.height=height	
		size = width*height
		if size:
			self.data = [None]*size
		else:
			self.data = [None]
		
	
	def draw(x,y,width,height,data):
		#data is the inner contents.
		#x is left offset.
		#y is top offset.
		#width...
		#height, I'm sure you can figure it out.
		l=0
		while l < (width*height): #width and height are max values.
			if data[l] == '\n':
				l+=((l/width)+1)*width # jump one line.
			else:
				self.data[((l+x)*y)%width]=data[l]
				l+=1
	
	def flush(x,y,width,height):
		ret = [None]*((width*height)+height)
		l=0
		while l < (width*height):
			if not (l%(width+1)):
				ret[l] = '\n'
			else:
				ret[l] = self.data[((l+x)*y)%width]
		
#... stuff...
global character_field
character_field = getTerminalSize()

#text orientation.
#def t_orient(text,x,y,maxx,maxy):
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

class game:
	main_menu = grid(character_field[0],character_field[1]);
	
	def __init__(self):
		main_menu
	
	
	








#debug section.
print(game.main_menu.width)
print(game.main_menu.height)













#eof, cause Imma stup.
