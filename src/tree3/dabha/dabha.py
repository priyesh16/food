#!/usr/bin/env python3
from tree3.blenderlib.blenderlib import *
import pdb

# Clear the window manager
wm = WindowManager()
wm.clear()

# Create scene
scene = Scene( bpy.context.scene )

# This is the container( dabha )that holds the cutting device
cutDabha = scene.addCutDabha( "cutDabha" )
cutDabha.addCameraRig()

scene.update()

# Save the file as a .blend file
blendFile = BlendFile()
blendFile.save()

# Render the scene
scene.render()
