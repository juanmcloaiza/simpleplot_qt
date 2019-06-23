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
#   Alexander Schober <alexander.schober@mac.com>
#
# *****************************************************************************

import numpy as np
from .plot_data import PlotData

from ..plot_geometries.surfaces import QuadSurface
from ..plot_geometries.points   import Point
from ..plot_geometries.shaders  import ShaderConstructor
from ...pyqtgraph.pyqtgraph     import functions

from ...model.node   import SessionNode

class VolumeData(PlotData, SessionNode): 
    '''
    This will be the main data class purposed
    to be inherited by variations with different
    variations.
    '''
    def __init__(self, **kwargs):
        PlotData.__init__(self, **kwargs) 
        SessionNode.__init__(self,'Data')

        self._axes = ['x','y','z','data']
        self._data = [None, None, None, None]
        self._bounds = [[0,1],[0,1],[0,1],[0,1]]

    def setData(self, **kwargs):
        '''
        set the local data manually even after
        initialization of the class
        '''
        elements = [None]*len(self._axes)
        changed  = [False, False, False, False]

        for i,value in enumerate(self._axes):
            if value in kwargs.keys():
                if isinstance(kwargs[value],np.ndarray) or isinstance(kwargs[value],list):
                    elements[i] = np.array(kwargs[value])
                    changed[self._axes.index(value)] = True

        if elements[self._axes.index('data')] is None:
            if not self._data[self._axes.index('data')] is None:
                elements[self._axes.index('data')] = self._data[self._axes.index('data')]  
            else:
                elements[self._axes.index('data')] = np.zeros((5,5,5))
                changed[self._axes.index('data')] = True

        if elements[self._axes.index('x')] is None:
            if not self._data[self._axes.index('x')] is None:
                elements[self._axes.index('x')] = self._data[self._axes.index('x')]  
            else:
                elements[self._axes.index('x')] = np.arange(elements[self._axes.index('data')].shape[0])
                changed[self._axes.index('x')] = True

        if elements[self._axes.index('y')] is None:
            if not self._data[self._axes.index('y')] is None:
                elements[self._axes.index('y')] = self._data[self._axes.index('y')]  
            else:
                elements[self._axes.index('y')] = np.arange(elements[self._axes.index('data')].shape[1])
                changed[self._axes.index('y')] = True

        if elements[self._axes.index('z')] is None:
            if not self._data[self._axes.index('z')] is None:
                elements[self._axes.index('z')] = self._data[self._axes.index('z')]  
            else:
                elements[self._axes.index('z')] = np.arange(elements[self._axes.index('data')].shape[2])
                changed[self._axes.index('z')] = True

        if self._sanity(elements):
            norm_data = np.array(elements[3]) - np.amin(elements[3])
            norm_data /= np.amax(norm_data)
            self._data = elements + [norm_data]
            self._setBounds()

    def getData(self):
        '''
        return a dataset as the data on the 
        wanted orientation
        '''
        return self._data

    def getBounds(self):
        '''
        returns the bounds
        '''
        return self._bounds

    def getIsosurface(self, value):
        '''
        Returns the x,y,z isocurve position fo the given
        level omn the present data
        '''
        return functions.isocurve(self._data[2], value, connected = True)

    def getBoundingBox(self):
        '''
        Returns the x,y,z isocurve position fo the given
        level omn the present data
        '''
        return self._boundingBox

    def _sanity(self, elements):
        '''
        Check that the data makes sense in 
        '''
        if not elements[self._axes.index('x')].shape[0] == elements[self._axes.index('data')].shape[0]:
            return False
        if not elements[self._axes.index('y')].shape[0] == elements[self._axes.index('data')].shape[1]:
            return False
        if not elements[self._axes.index('z')].shape[0] == elements[self._axes.index('data')].shape[2]:
            return False
        return True

    def _setBounds(self):
        '''
        returns the bounds of the set datastructure
        '''
        self._bounds = []
        for element in self._data:
            self._bounds.append([np.amin(element), np.amax(element)])
        
    def _setBoundingBox(self):
        '''
        Update the topography of the surface
        '''
        bounds = self._bounds

        bounding_box = np.array([
            #top and bottom
            [
                [bounds[0][0], bounds[1][0], bounds[2][0]],
                [bounds[0][1], bounds[1][0], bounds[2][0]],
                [bounds[0][0], bounds[1][1], bounds[2][0]]],
            [
                [bounds[0][1], bounds[1][0], bounds[2][0]],
                [bounds[0][0], bounds[1][1], bounds[2][0]],
                [bounds[0][1], bounds[1][1], bounds[2][0]]],
            [
                [bounds[0][0], bounds[1][0], bounds[2][1]],
                [bounds[0][1], bounds[1][0], bounds[2][1]],
                [bounds[0][0], bounds[1][1], bounds[2][1]]],
            [
                [bounds[0][1], bounds[1][0], bounds[2][1]],
                [bounds[0][0], bounds[1][1], bounds[2][1]],
                [bounds[0][1], bounds[1][1], bounds[2][1]]],

            #front back
            [
                [bounds[0][0], bounds[1][0], bounds[2][0]],
                [bounds[0][1], bounds[1][0], bounds[2][0]],
                [bounds[0][0], bounds[1][0], bounds[2][1]]],
            [
                [bounds[0][0], bounds[1][0], bounds[2][1]],
                [bounds[0][1], bounds[1][0], bounds[2][0]],
                [bounds[0][1], bounds[1][0], bounds[2][1]]],
            [
                [bounds[0][0], bounds[1][1], bounds[2][0]],
                [bounds[0][1], bounds[1][1], bounds[2][0]],
                [bounds[0][0], bounds[1][1], bounds[2][1]]],
            [
                [bounds[0][0], bounds[1][1], bounds[2][1]],
                [bounds[0][1], bounds[1][1], bounds[2][0]],
                [bounds[0][1], bounds[1][1], bounds[2][1]]],
                
            #left right
            [
                [bounds[0][0], bounds[1][0], bounds[2][0]],
                [bounds[0][0], bounds[1][1], bounds[2][0]],
                [bounds[0][0], bounds[1][1], bounds[2][1]]],
            [
                [bounds[0][0], bounds[1][1], bounds[2][1]],
                [bounds[0][0], bounds[1][0], bounds[2][0]],
                [bounds[0][0], bounds[1][0], bounds[2][1]]],
            [
                [bounds[0][1], bounds[1][0], bounds[2][0]],
                [bounds[0][1], bounds[1][1], bounds[2][0]],
                [bounds[0][1], bounds[1][1], bounds[2][1]]],
            [
                [bounds[0][1], bounds[1][1], bounds[2][1]],
                [bounds[0][1], bounds[1][0], bounds[2][0]],
                [bounds[0][1], bounds[1][0], bounds[2][1]]]])

        self._boundingBox = bounding_box