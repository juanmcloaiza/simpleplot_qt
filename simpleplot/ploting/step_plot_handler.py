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

from PyQt5 import QtGui, QtCore

from .plot_data_types.step_data     import StepData
from .plot_handler                  import PlotHandler

from .plot_items.step_plot          import StepPlot
from .plot_items.SimpleItemSample   import SimpleItemSample

from .plot_geometries.transformer   import Transformer

class StepPlotHandler(PlotHandler):

    def __init__(self, **kwargs):
        '''
        '''
        if 'Name' in kwargs.keys():
            PlotHandler.__init__(self, kwargs['Name'])
        else:
            PlotHandler.__init__(self, 'No_name')

        self._plot_data     = StepData()
        self.addChild(self._plot_data)
        self.addChild(StepPlot(**kwargs))
        # self._ray_handler   = SurfaceRayHandler()
        # self.addChild(self._ray_handler)
        self._plot_data.setData(**kwargs)

    def setData(self, **kwargs):
        '''
        Set the data of the image and then let the 
        program decide which procedure to target Note
        that this routine aims at updating the data only
        '''
        self['Data'].setData(**kwargs)
        
        for child in self._children:
            if hasattr(child, 'refresh'):
                child.refresh()
        
        self._model.dataChanged.emit(self._plot_data.index(),self._plot_data.index())

    def legendItems(self):
        '''
        return to the legend the items to be used
        '''
        return SimpleItemSample([])

    def addProjectionItem(self, item, direction = 'x'):
        '''
        Allows to set 1D projection items 
        as the plot items
        '''
        self._proj_list.append([item, direction])

