#!/usr/bin/env python3
from tree3.blenderlib.blenderlib import *

# Clear the screen
scene = Scene()
scene.clear()

# This is the container( dabba )that holds the cutting device
cutDabba = Cube( "cutDabba" )
cutDabba.add( location=( 0, 0, 0 ) )

# Save the file as a .blend file
blendFile = BlendFile()
blendFile.save()
