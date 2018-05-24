# -*- coding: utf-8 -*-
"""
Created on Wed May 23 13:10:37 2018

@author: scott.downard
Data to Video Compare
Script opens a single linear file, per framerate input the script will take
a snapshot of the graph at specific times and then input all the frames into a
single video that can be used to compare to the deployment video.
"""


import cv2
import tkinter
import os
import struct
from PIL import Image



data_dict = fileRead(direc)

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import Mainwindow
from LinearReader import *
from exporttoexcel import *

#Object that runs GUI.
class LinearVideoApp(QtWidgets.QMainWindow, Mainwindow.Ui_mainwindow):

#Initialize widgets.    
    def __init__(self,parent=None):
        filterlist = ['Raw','60','180']
        super(LinearApp, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget.setColumnCount(5)        
        self.filterBox.addItems(filterlist)
        self.openFile.clicked.connect(self.browse_folder)
        self.graphbtn.clicked.connect(self.report)
#        self.export_2.clicked.connect(self.exportexcel)
        self.data_dict = {}    
        self.test_list = []
        
    def browse_folder(self):        
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self,"Pick a Folder")        
        if self.directory:
            self.tableWidget.clear()
            tempdict = {}
            group_list = []
            tempdict = fileRead(self.directory)
            for key in tempdict:
                if key in self.data_dict.keys():
                    self.data_dict[key] = tempdict[key]
                    tempdict.pop(key,None)
            self.data_dict.update(tempdict)
            
            for keys in tempdict:
                self.test_list.append(keys)
            tempdict.clear()
            for i in range(len(self.test_list)):
                group_list.append(str(i+1))
            self.tableWidget.setRowCount(len(self.test_list))
            self.tableWidget.setHorizontalHeaderLabels(['Test Name','Line Color','Delete'])
            
#Button function for selection color with color picker. 
    def clickedColor(self):
        button = QtWidgets.qApp.focusWidget()
        color = QtWidgets.QColorDialog.getColor()
        button.setStyleSheet("QWidget { background-color: %s}" % color.name())
        index = self.tableWidget.indexAt(button.pos())
        self.data_dict[self.tableWidget.item(index.row(),0).text()]['Color'] = color.name()
#Delete unwanted files from dictionary. (Not from folder)        
    def deleteData(self):
        button = QtWidgets.qApp.focusWidget()
        index = self.tableWidget.indexAt(button.pos())
        namedel = self.tableWidget.item(index.row(),0).text()
        self.data_dict.pop(namedel,None)
        self.test_list.remove(namedel)
        self.tableWidget.removeRow(index.row())
        
            
        


                
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = LinearVideoApp()
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()