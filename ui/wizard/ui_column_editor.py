# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_column_editor.ui'
#
# Created: Wed Oct 05 16:10:05 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ColumnEditor(object):
    def setupUi(self, ColumnEditor):
        ColumnEditor.setObjectName(_fromUtf8("ColumnEditor"))
        ColumnEditor.resize(364, 314)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ColumnEditor.sizePolicy().hasHeightForWidth())
        ColumnEditor.setSizePolicy(sizePolicy)
        ColumnEditor.setMaximumSize(QtCore.QSize(16777215, 320))
        self.verticalLayout_3 = QtGui.QVBoxLayout(ColumnEditor)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.notif_bar = QtGui.QVBoxLayout()
        self.notif_bar.setSpacing(8)
        self.notif_bar.setContentsMargins(-1, -1, -1, 5)
        self.notif_bar.setObjectName(_fromUtf8("notif_bar"))
        self.verticalLayout_3.addLayout(self.notif_bar)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(ColumnEditor)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.edtColDesc = QtGui.QLineEdit(ColumnEditor)
        self.edtColDesc.setObjectName(_fromUtf8("edtColDesc"))
        self.gridLayout.addWidget(self.edtColDesc, 1, 1, 1, 1)
        self.label_11 = QtGui.QLabel(ColumnEditor)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout.addWidget(self.label_11, 2, 0, 1, 1)
        self.edtUserTip = QtGui.QLineEdit(ColumnEditor)
        self.edtUserTip.setText(_fromUtf8(""))
        self.edtUserTip.setObjectName(_fromUtf8("edtUserTip"))
        self.gridLayout.addWidget(self.edtUserTip, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(ColumnEditor)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.cboDataType = QtGui.QComboBox(ColumnEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboDataType.sizePolicy().hasHeightForWidth())
        self.cboDataType.setSizePolicy(sizePolicy)
        self.cboDataType.setEditable(False)
        self.cboDataType.setObjectName(_fromUtf8("cboDataType"))
        self.gridLayout.addWidget(self.cboDataType, 3, 1, 1, 1)
        self.btnColProp = QtGui.QPushButton(ColumnEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnColProp.sizePolicy().hasHeightForWidth())
        self.btnColProp.setSizePolicy(sizePolicy)
        self.btnColProp.setObjectName(_fromUtf8("btnColProp"))
        self.gridLayout.addWidget(self.btnColProp, 4, 1, 1, 1)
        self.edtColName = QtGui.QLineEdit(ColumnEditor)
        self.edtColName.setObjectName(_fromUtf8("edtColName"))
        self.gridLayout.addWidget(self.edtColName, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ColumnEditor)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setContentsMargins(90, -1, 0, 5)
        self.gridLayout_2.setVerticalSpacing(10)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.cbMandt = QtGui.QCheckBox(ColumnEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbMandt.sizePolicy().hasHeightForWidth())
        self.cbMandt.setSizePolicy(sizePolicy)
        self.cbMandt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cbMandt.setChecked(False)
        self.cbMandt.setObjectName(_fromUtf8("cbMandt"))
        self.gridLayout_2.addWidget(self.cbMandt, 0, 0, 1, 1)
        self.cbSearch = QtGui.QCheckBox(ColumnEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbSearch.sizePolicy().hasHeightForWidth())
        self.cbSearch.setSizePolicy(sizePolicy)
        self.cbSearch.setObjectName(_fromUtf8("cbSearch"))
        self.gridLayout_2.addWidget(self.cbSearch, 1, 0, 1, 1)
        self.cbUnique = QtGui.QCheckBox(ColumnEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbUnique.sizePolicy().hasHeightForWidth())
        self.cbUnique.setSizePolicy(sizePolicy)
        self.cbUnique.setObjectName(_fromUtf8("cbUnique"))
        self.gridLayout_2.addWidget(self.cbUnique, 2, 0, 1, 1)
        self.cbIndex = QtGui.QCheckBox(ColumnEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbIndex.sizePolicy().hasHeightForWidth())
        self.cbIndex.setSizePolicy(sizePolicy)
        self.cbIndex.setObjectName(_fromUtf8("cbIndex"))
        self.gridLayout_2.addWidget(self.cbIndex, 3, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.buttonBox = QtGui.QDialogButtonBox(ColumnEditor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(ColumnEditor)
        QtCore.QMetaObject.connectSlotsByName(ColumnEditor)
        ColumnEditor.setTabOrder(self.edtColName, self.edtColDesc)
        ColumnEditor.setTabOrder(self.edtColDesc, self.edtUserTip)
        ColumnEditor.setTabOrder(self.edtUserTip, self.cboDataType)
        ColumnEditor.setTabOrder(self.cboDataType, self.btnColProp)
        ColumnEditor.setTabOrder(self.btnColProp, self.cbMandt)
        ColumnEditor.setTabOrder(self.cbMandt, self.cbSearch)
        ColumnEditor.setTabOrder(self.cbSearch, self.cbUnique)
        ColumnEditor.setTabOrder(self.cbUnique, self.cbIndex)

    def retranslateUi(self, ColumnEditor):
        ColumnEditor.setWindowTitle(_translate("ColumnEditor", "Column editor", None))
        self.label_3.setText(_translate("ColumnEditor", "Description", None))
        self.edtColDesc.setPlaceholderText(_translate("ColumnEditor", "Column Description", None))
        self.label_11.setText(_translate("ColumnEditor", "User tip", None))
        self.edtUserTip.setPlaceholderText(_translate("ColumnEditor", "Enter text to appear in the form as a tooltip", None))
        self.label_4.setText(_translate("ColumnEditor", "Column data type", None))
        self.btnColProp.setText(_translate("ColumnEditor", "Column properties ...", None))
        self.edtColName.setPlaceholderText(_translate("ColumnEditor", "Enter column name", None))
        self.label_2.setText(_translate("ColumnEditor", "Column name", None))
        self.cbMandt.setText(_translate("ColumnEditor", "Mandatory", None))
        self.cbSearch.setText(_translate("ColumnEditor", "Searchable", None))
        self.cbUnique.setText(_translate("ColumnEditor", "Unique", None))
        self.cbIndex.setText(_translate("ColumnEditor", "Column Indexed", None))

