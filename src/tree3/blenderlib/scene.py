#!/usr/bin/env python3

from tree3 import blenderlib

class Scene( object ):
	def __init__( self, sceneNum ):
		self.sceneNum = 0

	def clearScreen( self ):
		bpy.ops.wm.read_factory_settings(use_empty=True)
