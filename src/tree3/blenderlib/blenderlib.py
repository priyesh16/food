#!/usr/bin/env python3

import blenderbpy
from blenderbpy import bpy

DEFAULT_BLEND_FILE = "/bld/dabba.blend"

class BlendFile( object ):
    def __init__( self, fileName=DEFAULT_BLEND_FILE ):
        self.fileName = fileName

    def save( self ):
        bpy.ops.wm.save_as_mainfile( filepath=self.fileName )

class Scene( object ):
	def __init__( self, sceneNum=0 ):
		self.sceneNum = 0

	def clear( self ):
		bpy.ops.wm.read_factory_settings(use_empty=True)

class Cube( object ):
    def __init__( self, name ):
        self.name = name

    def add( self, location=(0, 0, 0) ):
        bpy.ops.mesh.primitive_cube_add(
            location=location )
	
class Camera( object ):
    def __init__( self, name ):
        self.name = name
        self.cam = bpy.data.cameras.new( name )

    def setLocation( self, location ):
        self.cam.location = location

    def setRotation( self, rotation ):
        self.cam.rotation_euler = rotation
