# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'surface_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SurfaceWidget(object):
    def setupUi(self, SurfaceWidget):
        SurfaceWidget.setObjectName("SurfaceWidget")
        SurfaceWidget.resize(569, 916)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SurfaceWidget.sizePolicy().hasHeightForWidth())
        SurfaceWidget.setSizePolicy(sizePolicy)
        SurfaceWidget.setMinimumSize(QtCore.QSize(50, 0))
        self.formlayout = QtWidgets.QFormLayout(SurfaceWidget)
        self.formlayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formlayout.setObjectName("formlayout")
        self.label = QtWidgets.QLabel(SurfaceWidget)
        self.label.setObjectName("label")
        self.formlayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.name = QtWidgets.QLineEdit(SurfaceWidget)
        self.name.setObjectName("name")
        self.formlayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name)
        self.line_2 = QtWidgets.QFrame(SurfaceWidget)
        self.line_2.setMinimumSize(QtCore.QSize(50, 0))
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formlayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        self.label_8 = QtWidgets.QLabel(SurfaceWidget)
        self.label_8.setObjectName("label_8")
        self.formlayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.label_8)
        self.label_3 = QtWidgets.QLabel(SurfaceWidget)
        self.label_3.setObjectName("label_3")
        self.formlayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.position_x = QtWidgets.QDoubleSpinBox(SurfaceWidget)
        self.position_x.setMinimum(-100000.0)
        self.position_x.setMaximum(100000.0)
        self.position_x.setObjectName("position_x")
        self.formlayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.position_x)
        self.label_9 = QtWidgets.QLabel(SurfaceWidget)
        self.label_9.setObjectName("label_9")
        self.formlayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.position_y = QtWidgets.QDoubleSpinBox(SurfaceWidget)
        self.position_y.setMinimum(-100000.0)
        self.position_y.setMaximum(100000.0)
        self.position_y.setObjectName("position_y")
        self.formlayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.position_y)
        self.label_10 = QtWidgets.QLabel(SurfaceWidget)
        self.label_10.setObjectName("label_10")
        self.formlayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.position_z = QtWidgets.QDoubleSpinBox(SurfaceWidget)
        self.position_z.setMinimum(-100000.0)
        self.position_z.setMaximum(100000.0)
        self.position_z.setObjectName("position_z")
        self.formlayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.position_z)
        self.line = QtWidgets.QFrame(SurfaceWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formlayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.label_4 = QtWidgets.QLabel(SurfaceWidget)
        self.label_4.setObjectName("label_4")
        self.formlayout.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.label_4)
        self.label_2 = QtWidgets.QLabel(SurfaceWidget)
        self.label_2.setObjectName("label_2")
        self.formlayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.scale_x = QtWidgets.QDoubleSpinBox(SurfaceWidget)
        self.scale_x.setMinimum(-100000.0)
        self.scale_x.setMaximum(100000.0)
        self.scale_x.setObjectName("scale_x")
        self.formlayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.scale_x)
        self.label_11 = QtWidgets.QLabel(SurfaceWidget)
        self.label_11.setObjectName("label_11")
        self.formlayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.scale_y = QtWidgets.QDoubleSpinBox(SurfaceWidget)
        self.scale_y.setMinimum(-100000.0)
        self.scale_y.setMaximum(100000.0)
        self.scale_y.setObjectName("scale_y")
        self.formlayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.scale_y)
        self.label_7 = QtWidgets.QLabel(SurfaceWidget)
        self.label_7.setObjectName("label_7")
        self.formlayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.scale_z = QtWidgets.QDoubleSpinBox(SurfaceWidget)
        self.scale_z.setMinimum(-100000.0)
        self.scale_z.setMaximum(100000.0)
        self.scale_z.setObjectName("scale_z")
        self.formlayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.scale_z)
        self.line_4 = QtWidgets.QFrame(SurfaceWidget)
        self.line_4.setMinimumSize(QtCore.QSize(50, 0))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.formlayout.setWidget(14, QtWidgets.QFormLayout.SpanningRole, self.line_4)
        self.label_6 = QtWidgets.QLabel(SurfaceWidget)
        self.label_6.setObjectName("label_6")
        self.formlayout.setWidget(15, QtWidgets.QFormLayout.SpanningRole, self.label_6)
        self.axis_x = QtWidgets.QLineEdit(SurfaceWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axis_x.sizePolicy().hasHeightForWidth())
        self.axis_x.setSizePolicy(sizePolicy)
        self.axis_x.setMaximumSize(QtCore.QSize(70, 16777215))
        self.axis_x.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.axis_x.setObjectName("axis_x")
        self.formlayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.axis_x)
        self.rot_x = QtWidgets.QDoubleSpinBox(SurfaceWidget)
        self.rot_x.setMinimum(-100000.0)
        self.rot_x.setMaximum(100000.0)
        self.rot_x.setObjectName("rot_x")
        self.formlayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.rot_x)
        self.axis_y = QtWidgets.QLineEdit(SurfaceWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axis_y.sizePolicy().hasHeightForWidth())
        self.axis_y.setSizePolicy(sizePolicy)
        self.axis_y.setMaximumSize(QtCore.QSize(70, 16777215))
        self.axis_y.setObjectName("axis_y")
        self.formlayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.axis_y)
        self.rot_y = QtWidgets.QDoubleSpinBox(SurfaceWidget)
        self.rot_y.setMinimum(-100000.0)
        self.rot_y.setMaximum(100000.0)
        self.rot_y.setObjectName("rot_y")
        self.formlayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.rot_y)
        self.axis_z = QtWidgets.QLineEdit(SurfaceWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.axis_z.sizePolicy().hasHeightForWidth())
        self.axis_z.setSizePolicy(sizePolicy)
        self.axis_z.setMaximumSize(QtCore.QSize(70, 16777215))
        self.axis_z.setObjectName("axis_z")
        self.formlayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.axis_z)
        self.rot_z = QtWidgets.QDoubleSpinBox(SurfaceWidget)
        self.rot_z.setMinimum(-100000.0)
        self.rot_z.setMaximum(100000.0)
        self.rot_z.setObjectName("rot_z")
        self.formlayout.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.rot_z)
        self.line_3 = QtWidgets.QFrame(SurfaceWidget)
        self.line_3.setMinimumSize(QtCore.QSize(50, 0))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.formlayout.setWidget(20, QtWidgets.QFormLayout.SpanningRole, self.line_3)
        self.label_19 = QtWidgets.QLabel(SurfaceWidget)
        self.label_19.setObjectName("label_19")
        self.formlayout.setWidget(21, QtWidgets.QFormLayout.SpanningRole, self.label_19)
        self.label_20 = QtWidgets.QLabel(SurfaceWidget)
        self.label_20.setObjectName("label_20")
        self.formlayout.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.label_5 = QtWidgets.QLabel(SurfaceWidget)
        self.label_5.setObjectName("label_5")
        self.formlayout.setWidget(23, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.gradient_layout = QtWidgets.QVBoxLayout()
        self.gradient_layout.setContentsMargins(0, -1, 0, -1)
        self.gradient_layout.setObjectName("gradient_layout")
        self.formlayout.setLayout(24, QtWidgets.QFormLayout.SpanningRole, self.gradient_layout)
        self.line_5 = QtWidgets.QFrame(SurfaceWidget)
        self.line_5.setMinimumSize(QtCore.QSize(50, 0))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.formlayout.setWidget(25, QtWidgets.QFormLayout.SpanningRole, self.line_5)
        self.label_12 = QtWidgets.QLabel(SurfaceWidget)
        self.label_12.setObjectName("label_12")
        self.formlayout.setWidget(26, QtWidgets.QFormLayout.SpanningRole, self.label_12)
        self.label_13 = QtWidgets.QLabel(SurfaceWidget)
        self.label_13.setObjectName("label_13")
        self.formlayout.setWidget(27, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.iso_check = QtWidgets.QCheckBox(SurfaceWidget)
        self.iso_check.setText("")
        self.iso_check.setObjectName("iso_check")
        self.formlayout.setWidget(27, QtWidgets.QFormLayout.FieldRole, self.iso_check)
        self.label_14 = QtWidgets.QLabel(SurfaceWidget)
        self.label_14.setObjectName("label_14")
        self.formlayout.setWidget(28, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.iso_levels = QtWidgets.QSpinBox(SurfaceWidget)
        self.iso_levels.setObjectName("iso_levels")
        self.formlayout.setWidget(28, QtWidgets.QFormLayout.FieldRole, self.iso_levels)
        self.label_15 = QtWidgets.QLabel(SurfaceWidget)
        self.label_15.setObjectName("label_15")
        self.formlayout.setWidget(29, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.iso_width = QtWidgets.QDoubleSpinBox(SurfaceWidget)
        self.iso_width.setObjectName("iso_width")
        self.formlayout.setWidget(29, QtWidgets.QFormLayout.FieldRole, self.iso_width)
        self.label_18 = QtWidgets.QLabel(SurfaceWidget)
        self.label_18.setObjectName("label_18")
        self.formlayout.setWidget(30, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.iso_offset = QtWidgets.QDoubleSpinBox(SurfaceWidget)
        self.iso_offset.setObjectName("iso_offset")
        self.formlayout.setWidget(30, QtWidgets.QFormLayout.FieldRole, self.iso_offset)
        self.label_16 = QtWidgets.QLabel(SurfaceWidget)
        self.label_16.setObjectName("label_16")
        self.formlayout.setWidget(32, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.iso_gradient_check = QtWidgets.QCheckBox(SurfaceWidget)
        self.iso_gradient_check.setText("")
        self.iso_gradient_check.setObjectName("iso_gradient_check")
        self.formlayout.setWidget(32, QtWidgets.QFormLayout.FieldRole, self.iso_gradient_check)
        self.label_17 = QtWidgets.QLabel(SurfaceWidget)
        self.label_17.setObjectName("label_17")
        self.formlayout.setWidget(33, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.iso_color = QtWidgets.QPushButton(SurfaceWidget)
        self.iso_color.setText("")
        self.iso_color.setObjectName("iso_color")
        self.formlayout.setWidget(33, QtWidgets.QFormLayout.FieldRole, self.iso_color)
        self.surface_check = QtWidgets.QCheckBox(SurfaceWidget)
        self.surface_check.setText("")
        self.surface_check.setObjectName("surface_check")
        self.formlayout.setWidget(22, QtWidgets.QFormLayout.FieldRole, self.surface_check)

        self.retranslateUi(SurfaceWidget)
        QtCore.QMetaObject.connectSlotsByName(SurfaceWidget)

    def retranslateUi(self, SurfaceWidget):
        _translate = QtCore.QCoreApplication.translate
        SurfaceWidget.setWindowTitle(_translate("SurfaceWidget", "Form"))
        self.label.setText(_translate("SurfaceWidget", "Name"))
        self.label_8.setText(_translate("SurfaceWidget", "Position"))
        self.label_3.setText(_translate("SurfaceWidget", "x"))
        self.label_9.setText(_translate("SurfaceWidget", "y"))
        self.label_10.setText(_translate("SurfaceWidget", "z"))
        self.label_4.setText(_translate("SurfaceWidget", "Scalling"))
        self.label_2.setText(_translate("SurfaceWidget", "x"))
        self.label_11.setText(_translate("SurfaceWidget", "y"))
        self.label_7.setText(_translate("SurfaceWidget", "z"))
        self.label_6.setText(_translate("SurfaceWidget", "Rotation"))
        self.axis_x.setText(_translate("SurfaceWidget", "1,0,0"))
        self.axis_y.setText(_translate("SurfaceWidget", "0,1,0"))
        self.axis_z.setText(_translate("SurfaceWidget", "0,0,1"))
        self.label_19.setText(_translate("SurfaceWidget", "Surface"))
        self.label_20.setText(_translate("SurfaceWidget", "Active"))
        self.label_5.setText(_translate("SurfaceWidget", "Color"))
        self.label_12.setText(_translate("SurfaceWidget", "Isosurface"))
        self.label_13.setText(_translate("SurfaceWidget", "Active"))
        self.label_14.setText(_translate("SurfaceWidget", "Levels"))
        self.label_15.setText(_translate("SurfaceWidget", "Line width"))
        self.label_18.setText(_translate("SurfaceWidget", "Offset"))
        self.label_16.setText(_translate("SurfaceWidget", "Use Gradient"))
        self.label_17.setText(_translate("SurfaceWidget", "Color"))

