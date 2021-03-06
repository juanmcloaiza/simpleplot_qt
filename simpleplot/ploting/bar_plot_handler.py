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

from .plot_data_types.bar_data      import BarData
from .plot_handler                  import PlotHandler

from .plot_items.bar_plot           import BarPlot
# from .plot_ray_handlers.surface     import SurfaceRayHandler
from .plot_items.SimpleItemSample   import SimpleItemSample

from .plot_geometries.transformer   import Transformer

class BarPlotHandler(PlotHandler):

    def __init__(self, **kwargs):
        '''
        '''
        if 'Name' in kwargs.keys():
            PlotHandler.__init__(self, kwargs['Name'])
        else:
            PlotHandler.__init__(self, 'No_name')

        self._plot_data     = BarData()
        self.addChild(self._plot_data)
        self.addChild(BarPlot(**kwargs))
        self._plot_data.setData(**kwargs)

    def setData(self, **kwargs):
        '''
        Set the data of the image and then let the 
        program decide which procedure to target Note
        that this routine aims at updating the data only
        '''
        self._plot_data.setData(**kwargs)
        
        for child in self._children:
            if hasattr(child, 'refresh'):
                child.refresh()
        
        self._model.dataChanged.emit(self._plot_data.index(),self._plot_data.index())

    def legendItems(self):
        '''
        return to the legend the items to be used
        '''
        # return SimpleItemSample([self.childFromName('Line'), self.childFromName('Scatter'), self.childFromName('Error')])
        return []
