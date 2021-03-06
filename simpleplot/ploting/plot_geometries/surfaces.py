#  -*- coding: utf-8 -*-
# *****************************************************************************
# Copyright (c) 2017 by the NSE analysis contributors (see AUTHORS)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Module authors:
#   Alexander Schober <alex.schober@mac.com>
#
# *****************************************************************************

#############################
#personal libraries
from .points import Point
from .transformations import *
from .operations import getNormal

#############################
#mathematic libraries
import numpy as np

class Surface:

    def __init__(self, **kwargs):
        '''
        This is the main surface class that will
        contain all common function calls such as 
        parameter changes and processing.
        '''
        self.identifier_type = 'Surface'
        self.type_name      = kwargs['name']
        self.generated      = False
        self.points         = []
        self.vertexes       = []
        self.faces          = []
        self.topography     = None
        self.border_points  = []

        self.resolution_x = 10
        self.resolution_y = 10

        #process kwargs
        if 'color' in kwargs.keys():
            self.color = kwargs['color']

        else:
            self.color = [1, 1, 1, 1]

    def changeResolution(self, resolution_x, resolution_y):
        '''
        Change the resolution parameter
        '''
        self.resolution_x = int(resolution_x)
        self.resolution_y = int(resolution_y)

    def getVertices(self):
        '''
        Sends out the vertices for ploting in the
        desired numpy format. 
        '''
        vertices = np.asarray(self.points)
        return vertices

    def getFaces(self):
        '''
        Sends out the faces for ploting in the
        desired numpy format. 
        '''
        return np.asarray(self.faces)

    def applyTransformation(self, transformation):
        '''
        This method will be used before processing a
        volume as the surfaces will be 
        '''
        
        #apply it to the generated points
        if self.generated:
            transformation.apply(self.border_points)
        
        #apply it to out points
        transformation.apply(self.points)

class QuadSurface(Surface):

    def __init__(self, border_points = None, height = None, width = None, **kwargs):
        '''
        This class is supposed to manage the quadratic 
        surfaces. It will initialise the positions and
        then create the faces array.      

        It is supposed that the points are given in an
        ordered manner forming rectangular strucutres. 
        '''
        Surface.__init__(self, **kwargs)

        self.type_name = 'QuadSurface'

        #save the points locally
        self.logic = [
            (border_points == None),
            (height == None),
            (height == None)
            ]

        if all(self.logic):
            self.border_points = [
                Point('Point_0', 0, 0, 0),
                Point('Point_1', 1, 0, 0),
                Point('Point_2', 1, 1, 0),
                Point('Point_3', 0, 1, 0)
            ]
            self.generated = True
        
        elif not self.logic[0]:
            self.border_points = border_points
            self.generated = False

        elif self.logic[0] and not self.logic[1] and not self.logic[2]:
            self.border_points = [
                Point('Point_0', 0, 0, 0),
                Point('Point_1', width, 0, 0),
                Point('Point_2', width, height, 0),
                Point('Point_3', 0, height, 0)
            ]
            self.generated = True
            
        #process the normal vector to process topography
        self.normal_vector = getNormal(self.border_points)
        
    def trace(self):
        '''
        calculate points and link them to create the
        vertices.   
        '''
        ids = np.arange(self.resolution_x*self.resolution_y, dtype='uint').reshape((self.resolution_y,self.resolution_x))
        self.np_points = np.zeros((self.resolution_y,self.resolution_x, 3),dtype='float32')

        for j,i in [(j,i) for j in range(self.resolution_y) for i in range(self.resolution_x)]:
            p_0_bis = (
                (self.border_points[3].vec - self.border_points[0].vec) 
                / (self.resolution_y-1)) * j + self.border_points[0].vec
            p_1_bis = (
                (self.border_points[2].vec - self.border_points[1].vec) 
                /(self.resolution_y-1)) * j + self.border_points[1].vec           
            self.np_points[j,i] = ( (p_1_bis - p_0_bis) / (self.resolution_x-1)) * i + p_0_bis

        self.faces = np.zeros(
            (self.np_points.shape[0]-1, self.np_points.shape[1]-1, 2, 3), 
            dtype='uint')

        for j,i in [(j,i) for j in range(self.resolution_y-1) for i in range(self.resolution_x-1)]:
            self.faces[j,i] = (
            np.array([
                [ids[j,i], ids[j,i+1], ids[j+1,i]] if i%2 == 0 else [ids[j,i], ids[j+1,i+1], ids[j+1,i]],
                [ids[j,i+1], ids[j+1,i+1], ids[j+1,i]] if i%2 == 0 else [ids[j,i], ids[j,i+1], ids[j+1,i+1]]]
            if j%2==0 else [
                [ids[j,i], ids[j+1,i+1], ids[j+1,i]] if i%2 == 0 
                else [ids[j,i], ids[j,i+1], ids[j+1,i]],
                [ids[j,i], ids[j,i+1], ids[j+1,i+1]] if i%2 == 0 
                else [ids[j,i+1], ids[j+1,i+1], ids[j+1,i]]]))

        self.points     = self.np_points.reshape((self.resolution_x*self.resolution_y,3))
        self.faces      = self.faces.reshape(((self.resolution_x-1)*(self.resolution_y-1)*2,3)).tolist()

        if not isinstance(self.topography, type(None)):
            self.applyTopography()

    def setTopography(self, topography, x_axis = None, y_axis = None, scale = 1):
        '''
        This function will allow to add a topography
        to the surface element. The topography will be
        given by an x axis and an y axis in form of 1D
        numpy array structures. The topography will be 
        given by a 2D numpy array.

        A scalding factor is given to account for
        '''
        self.topography = np.asarray(topography)
        self.changeResolution(topography.shape[0],topography.shape[1])
        self.trace()

    def applyTopography(self):
        '''
        This function applies the provided topography 
        '''
        if all([self.normal_vector[i] == element for i,element in enumerate([0,0,1])]):
            self.points[:,2] = np.reshape(self.topography.transpose(),(self.points.shape[0]))

        else:
            for j in range(self.resolution_y):
                for i in range(self.resolution_x):
                    translate = Translation(self.normal_vector * self.topography[i,j])
                    translate.apply([self.points[j * self.resolution_x + i]]) 


class Disk(QuadSurface):
    
    def __init__(self, dimension = 1, **kwargs):
        '''
        ##############################################
        This is a wrapper class that will indeed 
        call the parent class made up of Quadsurface
        that inherits from surfaces.    
        ———————
        Input: -
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        QuadSurface.__init__(self, height = dimension, width = dimension, **kwargs)
        self.type_name = 'Disk'



class Square(QuadSurface):
    
    def __init__(self, dimension = 1, **kwargs):
        '''
        ##############################################
        This is a wrapper class that will indeed 
        call the parent class made up of Quadsurface
        that inherits from surfaces.    
        ———————
        Input: -
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        QuadSurface.__init__(self, height = dimension, width = dimension, **kwargs)
        self.type_name = 'Square'

class Rectangle(QuadSurface):
    
    def __init__(self, height = 1, width = 1, **kwargs):
        '''
        ##############################################
        This is a wrapper class that will indeed 
        call the parent class made up of Quadsurface
        that inherits from surfaces.     
        ———————
        Input: -
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        QuadSurface.__init__(self, height = height, width = width, **kwargs)
        self.type_name = 'Rectangle'

class TriSurface(Surface):

    def __init__(self):
        '''
        ##############################################
        This class is supposed to manage the quadratic 
        surfaces. It will initialise the positions and
        then create the faces array.      
        ———————
        Input: -
        ———————
        Output: -
        ———————
        status: active
        ##############################################
        '''
        Surface.__init__(self)
        self.type_name = 'TriSurface'

# class CylSurface(Surface):

#     def __init__(self):
#         '''
#         ##############################################
        
#         ———————
#         Input: -
#         ———————
#         Output: -
#         ———————
#         status: active
#         ##############################################
#         '''
#         Surface.__init__(self)
#         self.type_name = 'CylSurface'

# class SphereSurface(Surface):

#     def __init__(self):
#         '''
#         ##############################################
        
#         ———————
#         Input: -
#         ———————
#         Output: -
#         ———————
#         status: active
#         ##############################################
#         '''
#         Surface.__init__(self)
#         self.type_name = 'SphereSurface'

# class ConeSurface(Surface):

#     def __init__(self):
#         '''
#         ##############################################
        
#         ———————
#         Input: -
#         ———————
#         Output: -
#         ———————
#         status: active
#         ##############################################
#         '''
#         Surface.__init__(self)
#         self.type_name = 'ConeSurface'