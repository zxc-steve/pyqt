# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:47:19 2021

@author: Stevedir
"""

import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import *
# from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
#     QVBoxLayout, QDialog)

class loadDirDialog(QtWidgets.QFileDialog):
    def __init__(self, *args):
        QtWidgets.QFileDialog.__init__(self, *args)
        self.setOption(self.DontUseNativeDialog, True)
        #self.setFileMode(self.DirectoryOnly)
        self.setFileMode(QtWidgets.QFileDialog.Directory)

        for view in self.findChildren(QtWidgets.QListView):
            if isinstance(view.model(), QtWidgets.QFileSystemModel):
                view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
                
        #https://stackoverflow.com/questions/28544425/pyqt-qfiledialog-multiple-directory-selection
        # this is for ExtendedSelection, not for comboBox enter event
        for view in self.findChildren(QtWidgets.QTreeView):     
            if isinstance(view.model(), QtWidgets.QFileSystemModel):
                view.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
                
        combo_box=self.findChild(QtWidgets.QComboBox,"lookInCombo")
        print(combo_box)
        combo_box.setEditable(True)
        
        #https://stackoverflow.com/questions/51189055/qcombobox-using-enter-event
        shortcut = QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return), combo_box, activated=self.onActivated)

    def onActivated(self):
        combo_box=self.findChild(QtWidgets.QComboBox,"lookInCombo")

        print("combo_box text()=",combo_box.currentText())
        self.setDirectory(combo_box.currentText())
        
class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

    # Greets the user
    def greetings(self):
        print(f"Hellowww {self.edit.text()}")

if __name__ == '__main__':
    # Create the Qt Application
    #app = QApplication(sys.argv)
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance() 
    # Create and show the form
    # form = Form()
    # form.show()
    ex = loadDirDialog()
    fileNames=[]
    if ex.exec_():
        fileNames = ex.selectedFiles()
        print(fileNames)
        listview=ex.findChild(QtWidgets.QListView,"listView")
        sys.exit()

    # Run the main Qt loop
    #sys.exit(app.exec_())
    app.exec_()
