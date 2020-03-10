#!/usr/bin/env python3

import pdb
import blenderbpy
import bmesh
from blenderbpy import bpy
from math import pi, sin, cos, radians, sqrt
print('=' * 80)

DEFAULT_BLEND_FILE = "/bld/dabba.blend"
DEFAULT_RENDER_FILE = "/bld/render"


class BlendFile(object):
    def __init__(self, fileName=DEFAULT_BLEND_FILE):
        self.fileName = fileName

    def save(self):
        bpy.ops.wm.save_as_mainfile(filepath=self.fileName)

class WindowManager( object ):
    def clear( self ):
        bpy.ops.wm.read_factory_settings( use_empty=True )

class Scene( WindowManager ):
    sceneNum = 0
    def __init__(self, scene):
        self.scene = scene
        self.sceneNum = self.sceneNum + 1
        self.scene.name = "Scene" + str( self.sceneNum )

    def link( self, obj ):
        self.scene.objects.link( obj )

    def addCutDabha( self, name ):
        cutDabha = CutDabha( self, name )
        return cutDabha

    def addCamera( self, camera ):
        self.scene.camera = camera

    def render( self ):
        self.scene.render.filepath = DEFAULT_RENDER_FILE
        bpy.ops.render.render( write_still=True , scene=self.scene.name)

    def update( self ):
        self.scene.update()
        
class CameraRig():
    def __init__( self, scene, name ):
        self.scene = scene
        self.name = name
        self.camera = None
        self.gimbal = None
        self.dolly = None
        self.keyLight = None
        self.fillLight = None
        self.backLight = None
        self.addCamera()
        #self.addGimbal()
        self.addDolly()

    def addCamera( self ):
        name = self.name + 'Camera'
        cam = bpy.data.cameras.new( name )
        self.camera = bpy.data.objects.new( name, cam )
        self.scene.link( self.camera )
        self.scene.camera = self.camera
        self.scene.addCamera( self.camera )

    def setLocation( self, x, y, z ):
        self.obj.location = ( x, y, z )

    def setRotation( self, rotation ):
        x, y, z = rotation
        self.obj.rotation_euler = rotation

    def addGimbal( self ):
        name = self.name + 'Gimbal'
        self.gimbal = bpy.data.objects.new( name, None )
        self.gimbal.empty_draw_type = 'CUBE'
        self.gimbal.empty_draw_size = 0.5
        self.scene.link( self.gimbal )
        childConstraint = self.camera.constraints.new( 'CHILD_OF' )
        childConstraint.target = self.gimbal

    def addDolly( self ):
        name = self.name + 'Dolly'
        bpy.ops.curve.primitive_bezier_circle_add(radius=3.0)
        self.dolly = bpy.context.object
        self.dolly.name = name
        followConstraint = self.camera.constraints.new( 'FOLLOW_PATH' )
        followConstraint.target = self.dolly
        followConstraint.use_curve_follow = True

    def lookAt( self, target ):
        trackConstraint = self.camera.constraints.new( 'TRACK_TO' )
        trackConstraint.target = target 
        trackConstraint.track_axis = 'TRACK_NEGATIVE_Z'
        trackConstraint.up_axis = 'UP_Y'

    def getVector( self, deltaPos ):
        x = deltaPos.x
        y = deltaPos.y 
        z = deltaPos.z
        vectorLen = sqrt( ( pow( x, 2 ) + pow( y, 2) + pow( z, 2 ) ) )
        return ( 1 / vectorLen ) * deltaPos

    def addLight( self, name, angle, energy, target ):
        # Defaults
        distance = 1
        height = 2

        targetPos = target.location
        cameraPos = targetPos.copy()
        cameraPos.x = -3
        deltaPos = cameraPos - targetPos
        vector = self.getVector( deltaPos ) 
        tempVector = vector.copy()
        tempVector.x = ( cos( angle ) * vector.x ) + ( -sin( angle ) * vector.y )
        tempVector.y = ( sin( angle ) * vector.x ) + ( cos( angle ) * vector.y )
        x = targetPos.x + distance * tempVector.x
        y = targetPos.y + distance * tempVector.y

        lightData = bpy.data.lamps.new( name=name, type="SUN" )
        lightData.energy = energy
        light = bpy.data.objects.new( name=name, object_data=lightData )
        light.location = ( x, y, height )

        trackConstraint = light.constraints.new( type="TRACK_TO" )
        trackConstraint.target = target
        trackConstraint.track_axis = "TRACK_NEGATIVE_Z"
        trackConstraint.up_axis = "UP_Y"

        self.scene.link( light )

        return light
        
    def add3PointLights( self, target ):
        # Defaults
        keyAngle = radians( 26 )
        fillAngle = radians( 145 )
        backAngle = radians( 235 )
        keyEnergy = 0.8
        fillEnergy = 0.6 
        backEnergy = 0.5

        # Add 3 point lights
        self.keyLight = self.addLight( self.name + "KeyLight", keyAngle, keyEnergy, target )
        self.fillLight = self.addLight( self.name + "FillLight", fillAngle, fillEnergy, target )
        self.backLight = self.addLight( self.name + "BackLight", backAngle, backEnergy, target )
        self.keyLight.data.shadow_method = 'RAY_SHADOW'

class CutDabha():
    def __init__( self, scene, name ):
        self.scene = scene
        self.name = name
        self.mesh = bpy.data.meshes.new( name )
        self.dabha = bpy.data.objects.new( name, self.mesh )
        bm = bmesh.new()
        bmesh.ops.create_cube( bm, size=1.0 )
        bm.to_mesh( self.mesh )
        bm.free()
        self.scene.link( self.dabha )

    def addCameraRig( self ):
        camera = CameraRig( self.scene, self.name )
        camera.lookAt( self.dabha )
        camera.add3PointLights( self.dabha )
        return camera
 
class Light( object ):
    def __init__( self, name, lightType='POINT' ):
        self.name = name
        self.light = bpy.data.lamps.new( name=name, type=lightType )
        self.obj = bpy.data.objects.new( name=name, object_data=self.light )

    def setLocation( self, x, y, z ):
        self.obj.location =  ( x, y, z )
