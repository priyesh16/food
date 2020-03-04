#!/usr/bin/env python3

DEFAULT_BLEND_FILE = "/bld/dabba.blend"
class BlendFile( object ):
    def __init__( self, filename=DEFAULT_BLEND_FILE ):
        self.fileName = fileName

    def save( self ):
        bpy.ops.wm.save_as_mainfile( filepath=self.fileName )
