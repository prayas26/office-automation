# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import RPi.GPIO as GPIO
import time
import os
import csv


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

def light1on(lon):
    GPIO.output(18,GPIO.HIGH)

def light2on(lon):
    GPIO.output(14,GPIO.HIGH)

def light3on(lon):
    GPIO.output(15,GPIO.HIGH)

def fan1on(fon):
    GPIO.output(23,GPIO.HIGH)

def fan2on(fon):
    GPIO.output(24,GPIO.HIGH)

def light1off(loff):
    GPIO.output(18,GPIO.LOW)

def light2off(loff):
    GPIO.output(14,GPIO.LOW)

def light3off(loff):
    GPIO.output(15,GPIO.LOW)

def fan1off(foff):
    GPIO.output(23,GPIO.LOW)

def fan2off(foff):
    GPIO.output(24,GPIO.LOW)
    
def last_log_lock():
    l = open("last_log.txt", 'w')
    log = "LOCK"
    l.write(log)
    l.close()

def last_log_unlock():
    u = open("last_log.txt", 'w')
    log = 'UNLOCK'
    u.write(log)
    u.close()

def doorclose(doorlock):
    o = open("last_log.txt", 'rw')
    x = o.read()
    if x == "LOCK":
        o.close()
    elif x == "UNLOCK":
        o.close()
        p = GPIO.PWM(21, 65)
        p.start(7.5)
        p.ChangeDutyCycle(12.5) 
        time.sleep(0.4)
        p = GPIO.PWM(21, 90)
        logs = []
        if os.access("lock_log.csv", os.F_OK):
            f = open("lock_log.csv", 'a')
            localtime = time.asctime( time.localtime(time.time()) )
            log = [localtime, 'LOCK']
            logs.append(log)
            for items in logs:
                    csv.writer(f).writerow(items)
            f.close()
        last_log_lock()
    else:
        o.close()

def dooropen(doorunlock):
    o = open("last_log.txt", 'rw')
    x = o.read()
    if x == "UNLOCK":
        o.close()
    elif x == "LOCK":
        o.close()
        p = GPIO.PWM(21, 165)
        p.start(7.5)
        p.ChangeDutyCycle(12.5)
        time.sleep(0.4)
        p = GPIO.PWM(21, 90)
        logs = []
        if os.access("lock_log.csv", os.F_OK):
            f = open("lock_log.csv", 'a')
            localtime = time.asctime( time.localtime(time.time()) )
            log = [localtime, 'UNLOCK']
            logs.append(log)
            for items in logs:
                csv.writer(f).writerow(items)
            f.close()
        last_log_unlock()
    else:
        o.close()


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

class Ui_raiot(object):
    def setupUi(self, raiot):
        raiot.setObjectName(_fromUtf8("raiot"))
        raiot.resize(500, 557)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(raiot.sizePolicy().hasHeightForWidth())
        raiot.setSizePolicy(sizePolicy)
        raiot.setMinimumSize(QtCore.QSize(500, 557))
        raiot.setMaximumSize(QtCore.QSize(500, 557))
        self.centralwidget = QtGui.QWidget(raiot)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 500, 500))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.doorunlock = QtGui.QPushButton(self.tab)
        self.doorunlock.setGeometry(QtCore.QRect(280, 200, 119, 40))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doorunlock.sizePolicy().hasHeightForWidth())
        self.doorunlock.setSizePolicy(sizePolicy)
        self.doorunlock.setMinimumSize(QtCore.QSize(20, 15))
        self.doorunlock.setMaximumSize(QtCore.QSize(120, 40))
        self.doorunlock.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        self.doorunlock.setObjectName(_fromUtf8("doorunlock"))
        self.doorlock = QtGui.QPushButton(self.tab)
        self.doorlock.setGeometry(QtCore.QRect(90, 200, 119, 40))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.doorlock.sizePolicy().hasHeightForWidth())
        self.doorlock.setSizePolicy(sizePolicy)
        self.doorlock.setMinimumSize(QtCore.QSize(20, 15))
        self.doorlock.setMaximumSize(QtCore.QSize(120, 40))
        self.doorlock.setStyleSheet(_fromUtf8("background-color: rgb(12, 255, 28);"))
        self.doorlock.setObjectName(_fromUtf8("doorlock"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.layoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(100, 140, 121, 271))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.light1on = QtGui.QPushButton(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.light1on.sizePolicy().hasHeightForWidth())
        self.light1on.setSizePolicy(sizePolicy)
        self.light1on.setMinimumSize(QtCore.QSize(20, 15))
        self.light1on.setMaximumSize(QtCore.QSize(120, 40))
        self.light1on.setStyleSheet(_fromUtf8("background-color: rgb(12, 255, 28);"))
        self.light1on.setObjectName(_fromUtf8("light1on"))
        self.verticalLayout.addWidget(self.light1on)
        self.light2on = QtGui.QPushButton(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.light2on.sizePolicy().hasHeightForWidth())
        self.light2on.setSizePolicy(sizePolicy)
        self.light2on.setMinimumSize(QtCore.QSize(20, 15))
        self.light2on.setMaximumSize(QtCore.QSize(120, 40))
        self.light2on.setStyleSheet(_fromUtf8("background-color: rgb(12, 255, 28);"))
        self.light2on.setObjectName(_fromUtf8("light2on"))
        self.verticalLayout.addWidget(self.light2on)
        self.light3on = QtGui.QPushButton(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.light3on.sizePolicy().hasHeightForWidth())
        self.light3on.setSizePolicy(sizePolicy)
        self.light3on.setMinimumSize(QtCore.QSize(20, 15))
        self.light3on.setMaximumSize(QtCore.QSize(120, 40))
        self.light3on.setStyleSheet(_fromUtf8("background-color: rgb(12, 255, 28);"))
        self.light3on.setObjectName(_fromUtf8("light3on"))
        self.verticalLayout.addWidget(self.light3on)
        self.fan1on = QtGui.QPushButton(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fan1on.sizePolicy().hasHeightForWidth())
        self.fan1on.setSizePolicy(sizePolicy)
        self.fan1on.setMinimumSize(QtCore.QSize(20, 15))
        self.fan1on.setMaximumSize(QtCore.QSize(120, 40))
        self.fan1on.setStyleSheet(_fromUtf8("background-color: rgb(12, 255, 28);"))
        self.fan1on.setObjectName(_fromUtf8("fan1on"))
        self.verticalLayout.addWidget(self.fan1on)
        self.fan2on = QtGui.QPushButton(self.layoutWidget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fan2on.sizePolicy().hasHeightForWidth())
        self.fan2on.setSizePolicy(sizePolicy)
        self.fan2on.setMinimumSize(QtCore.QSize(20, 15))
        self.fan2on.setMaximumSize(QtCore.QSize(120, 40))
        self.fan2on.setStyleSheet(_fromUtf8("background-color: rgb(12, 255, 28);"))
        self.fan2on.setObjectName(_fromUtf8("fan2on"))
        self.verticalLayout.addWidget(self.fan2on)
        self.layoutWidget_3 = QtGui.QWidget(self.tab_2)
        self.layoutWidget_3.setGeometry(QtCore.QRect(270, 140, 121, 271))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.light1off = QtGui.QPushButton(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.light1off.sizePolicy().hasHeightForWidth())
        self.light1off.setSizePolicy(sizePolicy)
        self.light1off.setMinimumSize(QtCore.QSize(20, 15))
        self.light1off.setMaximumSize(QtCore.QSize(120, 40))
        self.light1off.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        self.light1off.setObjectName(_fromUtf8("light1off"))
        self.verticalLayout_2.addWidget(self.light1off)
        self.light2off = QtGui.QPushButton(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.light2off.sizePolicy().hasHeightForWidth())
        self.light2off.setSizePolicy(sizePolicy)
        self.light2off.setMinimumSize(QtCore.QSize(20, 15))
        self.light2off.setMaximumSize(QtCore.QSize(120, 40))
        self.light2off.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        self.light2off.setObjectName(_fromUtf8("light2off"))
        self.verticalLayout_2.addWidget(self.light2off)
        self.light3off = QtGui.QPushButton(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.light3off.sizePolicy().hasHeightForWidth())
        self.light3off.setSizePolicy(sizePolicy)
        self.light3off.setMinimumSize(QtCore.QSize(20, 15))
        self.light3off.setMaximumSize(QtCore.QSize(120, 40))
        self.light3off.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        self.light3off.setObjectName(_fromUtf8("light3off"))
        self.verticalLayout_2.addWidget(self.light3off)
        self.fan1off = QtGui.QPushButton(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fan1off.sizePolicy().hasHeightForWidth())
        self.fan1off.setSizePolicy(sizePolicy)
        self.fan1off.setMinimumSize(QtCore.QSize(20, 15))
        self.fan1off.setMaximumSize(QtCore.QSize(120, 40))
        self.fan1off.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        self.fan1off.setObjectName(_fromUtf8("fan1off"))
        self.verticalLayout_2.addWidget(self.fan1off)
        self.fan2off = QtGui.QPushButton(self.layoutWidget_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fan2off.sizePolicy().hasHeightForWidth())
        self.fan2off.setSizePolicy(sizePolicy)
        self.fan2off.setMinimumSize(QtCore.QSize(20, 15))
        self.fan2off.setMaximumSize(QtCore.QSize(120, 40))
        self.fan2off.setStyleSheet(_fromUtf8("background-color: rgb(255, 0, 0);"))
        self.fan2off.setObjectName(_fromUtf8("fan2off"))
        self.verticalLayout_2.addWidget(self.fan2off)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        raiot.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(raiot)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu = QtGui.QMenu(self.menubar)
        self.menuMenu.setObjectName(_fromUtf8("menuMenu"))
        raiot.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(raiot)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        raiot.setStatusBar(self.statusbar)
        self.actionAbout = QtGui.QAction(raiot)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionExit = QtGui.QAction(raiot)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuMenu.addAction(self.actionAbout)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(raiot)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("activated()")), raiot.close)
        QtCore.QMetaObject.connectSlotsByName(raiot)

    def retranslateUi(self, raiot):
        raiot.setWindowTitle(_translate("raiot", "RAIOT Office Automation", None))
        self.doorunlock.setText(_translate("raiot", "UNLOCK", None))
        self.doorlock.setText(_translate("raiot", "LOCK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("raiot", "Door Lock", None))
        self.light1on.setText(_translate("raiot", "Light 1 ON", None))
        self.light2on.setText(_translate("raiot", "Light 2 ON", None))
        self.light3on.setText(_translate("raiot", "Light 3 ON", None))
        self.fan1on.setText(_translate("raiot", "Fan 1 ON", None))
        self.fan2on.setText(_translate("raiot", "Fan 2 ON", None))
        self.light1off.setText(_translate("raiot", "Light 1 OFF", None))
        self.light2off.setText(_translate("raiot", "Light 2 OFF", None))
        self.light3off.setText(_translate("raiot", "Light 3 OFF", None))
        self.fan1off.setText(_translate("raiot", "Fan 1 OFF", None))
        self.fan2off.setText(_translate("raiot", "Fan 2 OFF", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("raiot", "Office Automation", None))
        self.menuMenu.setTitle(_translate("raiot", "Menu", None))
        self.actionAbout.setText(_translate("raiot", "About", None))
        self.actionAbout.setShortcut(_translate("raiot", "Ctrl+A", None))
        self.actionExit.setText(_translate("raiot", "Exit", None))
        self.actionExit.setShortcut(_translate("raiot", "Ctrl+X", None))
        self.doorlock.clicked.connect(lambda:dooropen(self.doorlock))
        self.doorunlock.clicked.connect(lambda:doorclose(self.doorunlock))
        self.light1on.clicked.connect(lambda:light1on(self.light1on))
        self.light2on.clicked.connect(lambda:light2on(self.light2on))
        self.light3on.clicked.connect(lambda:light3on(self.light3on))
        self.fan1on.clicked.connect(lambda:fan1on(self.fan1on))
        self.fan2on.clicked.connect(lambda:fan2on(self.fan1on))
        self.light1off.clicked.connect(lambda:light1off(self.light1off))
        self.light2off.clicked.connect(lambda:light2off(self.light2off))
        self.light3off.clicked.connect(lambda:light3off(self.light3off))
        self.fan1off.clicked.connect(lambda:fan1off(self.fan1off))
        self.fan2off.clicked.connect(lambda:fan2off(self.fan2off))

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    raiot = QtGui.QMainWindow()
    ui = Ui_raiot()
    ui.setupUi(raiot)
    raiot.show()
    sys.exit(app.exec_())

