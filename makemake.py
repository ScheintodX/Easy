#!/usr/bin/python3

import json

with open( 'conf.json', 'r' ) as f:

	conf = json.load( f )

ALL=[]

BTOG = conf['BTOG'].split()

def printRule( name, w, h, x, y ):

	print( "%s: $(BASE) xpm.Makefile" % name )
	print( "	%s %dx%d+%d+%d $< $@" % ( "$(CROP)", w, h, x, y ) )
	print()

	ALL.append( name )


bw = conf['border_w']
bh = conf['border_h']
th = conf['title_h']

ww = conf['win_w']
wh = conf['win_h']


for button in conf['BUTTONS'].split():

	for btype in conf['BTYPES'].split():

		x = conf[ button + '_x' ]
		w = conf['button_w']

		y = conf[ btype + '_y' ] +bh/2
		h = conf['title_h'] #+bh

		name = "xfwm4/%s-%s.xpm" % ( button, btype )

		printRule( name, w, h, x, y )

		if button in BTOG:

			name = "xfwm4/%s-toggled-%s.xpm" % ( button, btype )

			x += conf['button_w']

			printRule( name, w, h, x, y )



printRule( "xfwm4/top-left-active.xpm", bw, bh+th, 0, 0 )
printRule( "xfwm4/top-left-inactive.xpm", bw, bh+th, 0, wh )

printRule( "xfwm4/top-right-active.xpm", bw, bh+th, ww-bw, 0 )
printRule( "xfwm4/top-right-inactive.xpm", bw, bh+th, ww-bw, wh )

printRule( "xfwm4/bottom-active.xpm", 1, bh, bw, wh-bh )
printRule( "xfwm4/bottom-inactive.xpm", 1, bh, bw, (2*wh)-bh )

printRule( "xfwm4/bottom-left-active.xpm", bw, bh, 0, bh )
printRule( "xfwm4/bottom-left-inactive.xpm", bw, bh, 0, (2*wh)-bh )

printRule( "xfwm4/bottom-right-active.xpm", bw, bh, bw, wh-bh )
printRule( "xfwm4/bottom-right-inactive.xpm", bw, bh, bw, (2*wh)-bh )

printRule( "xfwm4/left-active.xpm", bw, 1, 0, bh )
printRule( "xfwm4/left-inactive.xpm", bw, 1, wh, bh )

printRule( "xfwm4/right-active.xpm", bw, 1, ww-bw, bh )
printRule( "xfwm4/right-inactive.xpm", bw, 1, ww-bw, bh )

for i in range(1,6):
	printRule( "xfwm4/title-%d-active.xpm" % i, 1, th+bh, 120+10*i, 0 )
	printRule( "xfwm4/title-%d-inactive.xpm" % i, 1, th+bh, 120+10*i, wh )


print( "ALL_XPM=%s" % " ".join( ALL ) )
print()
