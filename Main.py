# -*- coding: utf-8 -*-
"""
Created on Wed May 23 13:10:37 2018

@author: scott.downard
Data to Video Compare
Script opens a single linear file, per framerate input the script will take
a snapshot of the graph at specific times and then input all the frames into a
single video that can be used to compare to the deployment video.
"""



from PIL import Image
import os
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import mainwindow
import matplotlib.pyplot as plt
import numpy as np
from LinearReader import *


    

#Object that runs GUI.
class LinearVideoApp(QtWidgets.QMainWindow, mainwindow.Ui_MainWindow):

#Initialize widgets.    
    def __init__(self,parent=None):
        filterlist = ['Raw','60','180']
        fpsList = ['1000','2000','4000']
        super(LinearVideoApp, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget.setColumnCount(3)        
        self.filterBox.addItems(filterlist)
        self.fpsBox.addItems(fpsList)
        self.directorybtn.clicked.connect(self.browse_folder)
        self.startbtn.clicked.connect(self.create)
        self.data_dict = {}    
        self.test_list = []
        
    def browse_folder(self):        
        self.directory = QtWidgets.QFileDialog.getExistingDirectory(self,"Pick a Folder")        
        if self.directory:
            self.tableWidget.clear()
            tempdict = {}
            tempdict = fileRead(self.directory)
            for key in tempdict:
                if key in self.data_dict.keys():
                    self.data_dict[key] = tempdict[key]
                    tempdict.pop(key,None)
            self.data_dict.update(tempdict)
            
            for keys in tempdict:
                self.test_list.append(keys)
            tempdict.clear()
            self.tableWidget.setRowCount(len(self.test_list))
            self.tableWidget.setHorizontalHeaderLabels(['Test Name','Line Color','Delete'])
            i = 0
            for k in self.test_list:
            
                self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(str(k)))
                self.tableWidget.item(i,0).setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                header = self.tableWidget.horizontalHeader()
                header.setSectionResizeMode(0,QtWidgets.QHeaderView.ResizeToContents)
                self.btncolor = QtWidgets.QPushButton()
                self.btncolor.clicked.connect(self.clickedColor)
                self.btncolor.setStyleSheet("background-color: black")
                self.tableWidget.setCellWidget(i,1,self.btncolor)
                self.btnDel = QtWidgets.QPushButton()
                self.btnDel.clicked.connect(self.deleteData)
                self.btnDel.setText("Remove")             
                self.tableWidget.setCellWidget(i,2,self.btnDel)
                i +=1
            
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
    def create(self):
        savedirectory = QtWidgets.QFileDialog.getSaveFileName(self,"Select Where to Save") #Get directory for path to save file.
        filtersize = self.filterBox.currentText() 
        if filtersize != 'Raw':
            for key in self.data_dict:
                self.data_dict[key]['Acceleration']['RawYData'] = filterProcessing(self.data_dict[key]['Acceleration']['RawYData'],int(filtersize),self.data_dict[key]['Acceleration']['Sample Rate'])            
        for key in self.data_dict:
            timeIdx = []
            
            fps = int(self.fpsBox.currentText())
            if fps == 1000:
                timeArray = np.arange(0,150,1)
            elif fps == 2000:
                timeArray = np.arange(0,150,0.5,dtype = np.float64)
            elif fps == 4000:
                timeArray = np.arange(0,150,0.25,dtype = np.float64)
            for i in timeArray:
                idx = (np.abs(self.data_dict[key]['Acceleration']['XData']-i)).argmin()
                timeIdx.append(idx)
            start = timeIdx[0]
            framecount = 1
            for i in timeIdx:
                plt.plot(self.data_dict[key]['Displacement']['RawYData'][start:i],self.data_dict[key]['Acceleration']['RawYData'][start:i])
                title = str(key)
                title = title.replace("\r","")
                plt.title(title)
                plt.xlabel('Displacement [mm]')
                plt.ylabel('Acceleration [g]')
                plt.savefig(savedirectory[0] + title +' Frame_' + str(framecount))

                height, width, layers = cv2.imread(savedirectory[0] + title +' Frame_' + str(framecount)+'.png')
                video = cv2.VideoWriter(title,-1,1,(width,height))
                video.write(cv2.imread(savedirectory[0] + title +' Frame_' + str(framecount)))
                os.remove(savedirectory[0] + title +' Frame_' + str(framecount)+'.png')
                plt.close()
                cv2.destroyAllWindows()
                video.release()
                framecount += 1
                
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = LinearVideoApp()
    form.show()
    app.exec_()
if __name__ == '__main__':
    main()