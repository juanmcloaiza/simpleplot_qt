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

from ..pointer.pointer  import Pointer
from ..pointer.zoomer   import Zoomer
from ..pointer.measurer import Measurer
from ..io.mouse         import Mouse
from .axes              import Axes
from .axes_gl           import Axes3D
from .legend            import Legend
from .grid_gl           import GridGl
from ..model.node       import SessionNode

from ..ploting.plot_handler import get_plot_handler
import pyqtgraph as pg

from copy import deepcopy
import numpy as np

class Artist():
    '''
    '''
    def __init__(self, canvas = None):

        self.canvas         = canvas
        self.artist_type    = '2D'
        self.child_widgets  = []


    def addPlot(self, name_type, *args, **kwargs):
        '''
        This method will go through the plot handlers
        and check if one of them has already the 
        selected items. if not a new instance will be
        generated and then fed into the handler system
        '''
        active_handlers = [child._name for child in self.canvas._plot_root._children]

        if not name_type in active_handlers:
            self.canvas._plot_root.addChild(get_plot_handler(name_type))

        active_handlers = [child._name for child in self.canvas._plot_root._children]
        output = self.canvas._plot_root._children[active_handlers.index(name_type)].addChild(*args, **kwargs)
        self.canvas._plot_model.referenceModel()

        return output

    def removePlot(self,name_type, name = '', idx = None):
        '''
        Remove an item from the handlers
        '''
        # active_handlers = [handler.name for handler in self.plot_handlers]

        # if idx == None and name == '':
        #     print("You can't remove nothing ...")

        # else:
        #     self.plot_handlers[active_handlers.index(name_type)].removeItem(
        #         name    = name, 
        #         idx     = idx,
        #         target  = self.canvas )
            
    def draw(self):
        '''
        This method will go through the plot handlers
        and check if one of them has already the 
        selected items. if not a new instance will be
        generated and then fed into the handler system
        '''
        for plot_handler in self.canvas._plot_root._children:
            plot_handler.draw(self.canvas)

    # def redraw(self):
    #     '''
    #     This method will go through the plot handlers
    #     and check if one of them has already the 
    #     selected items. if not a new instance will be
    #     generated and then fed into the handler system
    #     '''
    #     for plot_handler in self.plot_handlers:
    #         plot_handler.draw(self.canvas)

    def clear(self):
        '''
        Interactive plotting software needs the
        ability to clear the current content. This is 
        done here by asking everyone to be deleted...
        '''
        for handler in self.plot_handlers:
            for element in handler.plot_elements:
                element.removeItem(self.canvas)
            handler.plot_elements = []


class Artist2DNode(SessionNode, Artist):
    '''
    This is the 2D artist manager, which can be seen as
    the subplot reference. It is linked to the drawing region
    and all plot elements.
    '''

    def __init__(self,name, parent,  canvas = None):

        #internal element identifier
        SessionNode.__init__(self, name, parent)
        Artist.__init__(self)

        self.canvas         = canvas
        self.plot_handlers  = []
        self.artist_type    = '2D'

        self.axes       = Axes(self.canvas)
        self.mouse      = Mouse(self.canvas)
        # self.Keyboard   = KeyboardClass.Keyboard(self.Canvas,Multi = self.Multi)
        self.pointer    = Pointer(self.canvas)
        self.zoomer     = Zoomer(self.canvas)
        self.measurer   = Measurer(self.canvas)
        self.legend     = Legend(self.canvas)
        # self.Modifier   = ModificationClass.Modify(self.Canvas)
        # self.Title      = None #TitleClass.TitleClass(self.Canvas)


    # def draw(self):
    #     '''
    #     This method will go through the plot handlers
    #     and check if one of them has already the 
    #     selected items. if not a new instance will be
    #     generated and then fed into the handler system
    #     '''
    #     for plot_handler in self.plot_handlers:
    #         plot_handler.draw(self.canvas)

    #     self.setup()
    #     for handler in self.plot_handlers:
    #         for element in handler.plot_elements:
    #             for item in element.draw_items:
    #                 if not isinstance(item, pg.ImageItem):
    #                     self.legend.legend_item.addItem(item, element.getParameter('Name'))

    def redraw(self):
        '''
        This method will go through the plot handlers
        and check if one of them has already the 
        selected items. if not a new instance will be
        generated and then fed into the handler system
        '''
        for plot_handler in self.plot_handlers:
            plot_handler.draw(self.canvas)
        self.zoomer.zoom()

    def clear(self):
        '''
        Interactive plotting software needs the
        ability to clear the current content. This is 
        done here by asking everyone to be deleted...
        '''
        for handler in self.plot_handlers:
            for element in handler.plot_elements:
                element.removeItems(self.canvas)
                for item in element.draw_items:
                    self.legend.legend_item.removeItem(item)
                    
            handler.plot_elements = []
        self.zoomer.zoom()

    def setup(self):
        '''
        Once all elements are created it is possible 
        to set up the functionalities. 
        '''
        try:
            self.pointer.unbindPointer()
        except:
            pass

        try:
            self.zoomer.quiet()
        except:
            pass

        self.pointer.bindPointer()
        self.zoomer.listen()

    def setMode(self, idx):
        '''
        Once all elements are created it is possible 
        to set up the functionalities. 

        '''
        self.zoomer.quiet()
        self.measurer.quiet()

        if idx == 0:
            self.zoomer.listen()

        elif idx == 1:
            self.measurer.listen()
        
    def setHistogram(self, location, item = None):
        '''
        Put a histogram on the layout
        The location is a string that will 
        indicate the four possible options.

        Parameters
        ----------
        location : str
            The location of the hist, left, right top, bottom

        item: Q item
            The item that should be linked 
        '''
        locations = {
            'left'  : [1,0],
            'top'   : [0,1],
            'bottom': [2,1],
            'right' : [1,2]}

        self.gradient_widget  = pg.GradientWidget(orientation = location)
        self.gradient_widget.setBackground(self.canvas.handler['Background'])

        if not item == None:
            state = {
                'mode':'rgb', 
                'ticks':[
                    tuple(
                        [item.getParameter('Positions')[i], 
                        tuple((np.array(item.getParameter('Colors')[i])*255).tolist())])
                    for i in range(len(item.getParameter('Positions')))]}
            self.gradient_widget.restoreState(state)

        self.canvas.grid_layout.addWidget(
            self.gradient_widget,
            locations[location][0],
            locations[location][1])

        self.gradient_widget.sigGradientChanged.connect(self._updateColors)
        return self.gradient_widget

    def _updateColors(self):
        '''
        Tell the plot item to update the colors
        of the surface plot item
        '''
        state       = self.gradient_widget.saveState()
        positions   = [element[0] for element in state['ticks']]
        colors      = [list(np.array(element[1])/255) for element in state['ticks']]
        colors      = [c for _,c in sorted(zip(positions, colors))]
        positions   = sorted(positions)

        self.canvas._plot_root.childFromName('Surface')
        for child in self.canvas._plot_root.childFromName('Surface')._children:
            child.setColor(colors, positions)

    def mouse_move(self,event):
        self.mouse.move(event)
    def mouse_press(self,event):
        self.mouse.press(event)
    def mouse_release(self,event):
        self.mouse.release(event)

class Artist3DNode(SessionNode, Artist):
    '''
    This is the 2D artist manager, which can be seen as
    the subplot reference. It is linked to the drawing region
    and all plot elements.
    '''
    def __init__(self,name, parent,  canvas = None):
        SessionNode.__init__(self, name, parent)
        Artist.__init__(self, canvas)

        self.canvas         = canvas
        self.plot_handlers  = []
        self.artist_type    = '3D'

        self.grid = GridGl(canvas)
        self.axes = Axes3D(canvas)

        self.canvas.view.rayUpdate.connect(self.processRay)


    def setup(self):
        '''
        Once all elements are created it is possible 
        to set up the functionalities. 
        '''
        pass

    def set_mode(self, idx):
        '''
        Once all elements are created it is possible 
        to set up the functionalities. 
        '''
        pass

    def processRay(self):
        '''
        Will try to Manage the items and their 
        ray tracing position calculation
        '''
        hits = []
        for child in self.canvas._plot_root._children:
            hits.append(child.processRay(self.canvas.view.mouse_ray))
        distances = [np.linalg.norm(e - self.canvas.view.mouse_ray[0]) for elements in hits for e in elements ]
    
    def _processDistances(self):
        '''
        Will process the distance arrangement of the ray
        and then tell the program from whom to pick 
        the data for the position lines
        '''
        pass

    def _getPointerData(self):
        '''
        Call the pointer onto the right child
        '''
        pass