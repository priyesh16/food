#!/usr/bin/env python3

class Cube( object ):
    def __init__( self, name ):
        self.name = name

    def add( self, location=(0, 0, 0) ):
        bpy.ops.mesh.primitive_cube_add(
            location=location )
	
