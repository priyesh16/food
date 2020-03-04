#!/usr/bin/env python3
import bpy
bpy.ops.mesh.primitive_cube_add( location=(0,0,0), rotation=(0,0,0) )

# Add a camera and set its location and rotation values
bpy.ops.object.camera_add()
camera = bpy.data.objects[ bpy.context.object.name ]
bpy.context.scene.camera = camera

bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.filepath = "//render_out"
bpy.ops.render.render( write_still = True )
