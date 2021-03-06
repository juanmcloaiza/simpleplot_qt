# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_preference_window(object):
    def setupUi(self, preference_window):
        preference_window.setObjectName("preference_window")
        preference_window.resize(334, 655)
        self.centralwidget = QtWidgets.QWidget(preference_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.canvas_tab = QtWidgets.QWidget()
        self.canvas_tab.setObjectName("canvas_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.canvas_tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.canvas_tree_view = QtWidgets.QTreeView(self.canvas_tab)
        self.canvas_tree_view.setObjectName("canvas_tree_view")
        self.verticalLayout_2.addWidget(self.canvas_tree_view)
        self.tabWidget.addTab(self.canvas_tab, "")
        self.plot_tab = QtWidgets.QWidget()
        self.plot_tab.setObjectName("plot_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.plot_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.plot_tab)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.canvas_select = QtWidgets.QComboBox(self.plot_tab)
        self.canvas_select.setObjectName("canvas_select")
        self.horizontalLayout.addWidget(self.canvas_select)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.widget = QtWidgets.QWidget(self.plot_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.plot_tree_view = QtWidgets.QTreeView(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plot_tree_view.sizePolicy().hasHeightForWidth())
        self.plot_tree_view.setSizePolicy(sizePolicy)
        self.plot_tree_view.setObjectName("plot_tree_view")
        self.verticalLayout_4.addWidget(self.plot_tree_view)
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayout_4.addWidget(self.splitter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_plot = QtWidgets.QPushButton(self.widget)
        self.add_plot.setObjectName("add_plot")
        self.horizontalLayout_3.addWidget(self.add_plot)
        self.remove_plot = QtWidgets.QPushButton(self.widget)
        self.remove_plot.setObjectName("remove_plot")
        self.horizontalLayout_3.addWidget(self.remove_plot)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.widget)
        self.tabWidget.addTab(self.plot_tab, "")
        self.io_in_tab = QtWidgets.QWidget()
        self.io_in_tab.setObjectName("io_in_tab")
        self.tabWidget.addTab(self.io_in_tab, "")
        self.io_out_tab = QtWidgets.QWidget()
        self.io_out_tab.setObjectName("io_out_tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.io_out_tab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.io_layout = QtWidgets.QVBoxLayout()
        self.io_layout.setObjectName("io_layout")
        self.verticalLayout_9.addLayout(self.io_layout)
        self.tabWidget.addTab(self.io_out_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        preference_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(preference_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 334, 27))
        self.menubar.setObjectName("menubar")
        preference_window.setMenuBar(self.menubar)

        self.retranslateUi(preference_window)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(preference_window)

    def retranslateUi(self, preference_window):
        _translate = QtCore.QCoreApplication.translate
        preference_window.setWindowTitle(_translate("preference_window", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.canvas_tab), _translate("preference_window", "Canvas"))
        self.label.setText(_translate("preference_window", "Canvas:"))
        self.add_plot.setText(_translate("preference_window", "+"))
        self.remove_plot.setText(_translate("preference_window", "-"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.plot_tab), _translate("preference_window", "Plot"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.io_in_tab), _translate("preference_window", "Load"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.io_out_tab), _translate("preference_window", "Save"))

