# -*- coding: utf-8 -*-


#!/usr/bin/env python3

import os
from PIL import Image
#import PIL.Image
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets





class Ui_TIfToJPG(object):

    def folder_click(self):
        print('folderclick')
        filename = QtWidgets.QFileDialog.getExistingDirectory()
        self.path = filename[0]
        self.folder_path = filename
        self.FolderText.setPlaceholderText(filename)
        print(filename)



    def low_click(self):
        print('lowClicked')
        print(self.quality_value)
        self.quality_value = self.low_value
        self.QualityText.setPlaceholderText(self.quality_value)
        print(self.quality_value)

    def med_click(self):
        print('medClicked')
        self.quality_value = self.med_value
        self.QualityText.setPlaceholderText(self.quality_value)
        print(self.quality_value)

    def high_click(self):
        print('highClicked')
        self.quality_value = self.high_value
        self.QualityText.setPlaceholderText(self.quality_value)
        print(self.quality_value)

    def setupUi(self, TIfToJPG):

        # Initiate all variables and set defaults
        self.quality_value = "100"
        self.low_value = '25'
        self.med_value = '60'
        self.high_value = '95'

        self.folder_path = ""


        self.outfile_type = ".jpg"



        TIfToJPG.setObjectName("TIfToJPG")
        TIfToJPG.resize(368, 369)
        #
        self.centralwidget = QtWidgets.QWidget(TIfToJPG)
        self.centralwidget.setObjectName("centralwidget")
        #
        self.Convert = QtWidgets.QPushButton(self.centralwidget)
        self.Convert.setGeometry(QtCore.QRect(10, 230, 351, 41))
        self.Convert.setObjectName("Convert")
        self.Convert.clicked.connect(self.convert_click)
        #
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 160, 211, 16))
        self.label.setObjectName("label")
        #
        self.LowButton = QtWidgets.QPushButton(self.centralwidget)
        self.LowButton.setGeometry(QtCore.QRect(10, 110, 91, 41))
        self.LowButton.setObjectName("LowButton")
        self.LowButton.clicked.connect(self.low_click)

        #
        self.MediumButton = QtWidgets.QPushButton(self.centralwidget)
        self.MediumButton.setGeometry(QtCore.QRect(140, 110, 91, 41))
        self.MediumButton.setObjectName("MediumButton")
        self.MediumButton.clicked.connect(self.med_click)
        #
        self.HighButton = QtWidgets.QPushButton(self.centralwidget)
        self.HighButton.setGeometry(QtCore.QRect(260, 110, 91, 41))
        self.HighButton.setObjectName("HighButton")
        self.HighButton.clicked.connect(self.high_click)
        #
        self.FolderText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.FolderText.setGeometry(QtCore.QRect(10, 30, 211, 41))
        self.FolderText.setObjectName("FolderText")
        self.FolderText.setPlaceholderText(self.folder_path)

        #
        self.QualityText = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.QualityText.setGeometry(QtCore.QRect(10, 180, 221, 41))
        self.QualityText.setObjectName("QualityText")
        self.QualityText.setPlaceholderText(self.quality_value)
        #
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 181, 16))
        self.label_5.setObjectName("label_5")
        #
        '''
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 320, 351, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        '''
        #
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 290, 171, 16))
        self.label_6.setObjectName("label_6")
        #
        self.FolderButton = QtWidgets.QPushButton(self.centralwidget)
        self.FolderButton.setGeometry(QtCore.QRect(250, 30, 81, 41))
        self.FolderButton.setObjectName("FolderButton")
        self.FolderButton.clicked.connect(self.folder_click)

        #
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 131, 16))
        self.label_2.setObjectName("label_2")
        #
        TIfToJPG.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(TIfToJPG)
        self.statusbar.setObjectName("statusbar")
        TIfToJPG.setStatusBar(self.statusbar)

        self.retranslateUi(TIfToJPG)
        QtCore.QMetaObject.connectSlotsByName(TIfToJPG)




    def retranslateUi(self, TIfToJPG):
        _translate = QtCore.QCoreApplication.translate
        TIfToJPG.setWindowTitle(_translate("TIfToJPG", "Tif To JPG"))
        self.Convert.setText(_translate("TIfToJPG", "Convert!"))
        self.label.setText(_translate("TIfToJPG", "Conversion Quality - 1 to 100 (best)"))
        self.LowButton.setText(_translate("TIfToJPG", "Low Quality"))
        self.MediumButton.setText(_translate("TIfToJPG", "Medium Quality"))
        self.HighButton.setText(_translate("TIfToJPG", "High Quality"))
        self.label_5.setText(_translate("TIfToJPG", "Folder to convert"))
        self.label_6.setText(_translate("TIfToJPG", "Output File Type"))
        self.FolderButton.setText(_translate("TIfToJPG", "Choose Folder"))
        self.label_2.setText(_translate("TIfToJPG", "Conversion Quality - Quick"))


    def convert_click(self):
        print("convert")
        print('folder_path' + self.folder_path)
        os.chdir(self.folder_path)
        self.image_list = os.listdir()
        print(self.image_list)

        # Convert all images
        for name in self.image_list:
            file_name = name.split('.')[0]
            print(file_name)
            im = Image.open(name)
            im.save(file_name + '.jpg')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TIfToJPG = QtWidgets.QMainWindow()
    ui = Ui_TIfToJPG()
    ui.setupUi(TIfToJPG)
    TIfToJPG.show()
    sys.exit(app.exec_())
