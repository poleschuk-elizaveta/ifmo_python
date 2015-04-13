#coding: utf-8
import clock
from PyQt4 import QtGui, QtCore, uic
import sys, os
from threading import Thread
url = "http://www.youtube.com/watch?v=-gZ25MYwWpM"

"""my_alarm = clock.Alarm("00:05:20")
my_alarm.chooseASong(url)
my_alarm.set()
print my_alarm.clear"""

"""my_timer = clock.Timer("00:00:06","00:00:06","01:10:00")
my_timer.chooseASong(url)
my_timer.set()
my_timer.clear"""
class AlarmClock(QtGui.QWidget):
    def __init__(self):
        super(AlarmClock, self).__init__()
        uic.loadUi("alarmClock.ui", self)
        self.alarmClock = None
        self.fromFile = False

        #alarm
        self.alarmTime.setTime(QtCore.QTime.currentTime())
        self.fromFileButton.clicked.connect(self.openFile)
        self.setAlarmClock.clicked.connect(self.timeForAlarm)
        self.cancel.clicked.connect(self.cancelAlarm)

        #timer
        self.timerClock = None
        self.fromFileButton_2.clicked.connect(self.openFile2)
        self.setTimerClock.clicked.connect(self.timeForTimer)
        self.cancel_2.clicked.connect(self.cancelTimer)

    def timeForAlarm(self):
        self.alarmClock = clock.Alarm(str(self.alarmTime.time().toString()))
        self.alarmClock.isCanceled = False
        self.threadForAlarm = Thread(target=self.alarmClock.set, args=(self.fromFile, ))
        self.threadForAlarm.daemon = True
        self.threadForAlarm.start()
        self.alarmClock.chooseASong(self.urlLine.text())

    def timeForTimer(self):
        self.timerClock = clock.Timer(str(self.timeForBreak.time().toString()),
                                      str(self.userTime.time().toString()),
                                      str(self.finalTime.time().toString()))
        self.timerClock.isCanceled = False
        self.threadForTimer = Thread(target=self.timerClock.set, args=(self.fromFile, ))
        self.threadForTimer.daemon = True
        self.threadForTimer.start()
        self.timerClock.chooseASong(self.urlLine_2.text())

    def openFile(self):
        self.fromFile = True
        try:
            fileFullPath = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
            filePath = os.path.split(os.path.normpath(str(fileFullPath)))[0]
            fileName = os.path.split(os.path.normpath(str(fileFullPath)))[1]
            os.chdir(filePath)
            self.urlLine.setText(fileName)
        except UnicodeEncodeError:
            self.show_modal_window()
    def openFile2(self):
        self.fromFile = True
        try:
            fileFullPath = QtGui.QFileDialog.getOpenFileName(self, 'Open file', '/home')
            filePath = os.path.split(os.path.normpath(str(fileFullPath)))[0]
            fileName = os.path.split(os.path.normpath(str(fileFullPath)))[1]
            os.chdir(filePath)
            self.urlLine_2.setText(fileName)
        except UnicodeEncodeError:
            self.show_modal_window()

    def cancelAlarm(self):
        try:
            self.alarmClock.isCanceled = True
            print "Cancel Alarm!"
        except AttributeError:
            return
    def cancelTimer(self):
        try:
            self.timerClock.isCanceled = True
            print "Cancel Timer!"
        except AttributeError:
            return

    def show_modal_window(self):
        global modalWindow
        modalWindow = QtGui.QWidget(self, QtCore.Qt.Window)
        uic.loadUi("dialog2.ui", modalWindow)
        #modalWindow.setWindowTitle("")
        #modalWindow.resize(200, 50)
        modalWindow.setWindowModality(QtCore.Qt.WindowModal)
        modalWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
        #modalWindow.move(self.geometry() .center() - modalWindow.rect() .center() - QtCore.QPoint(4, 30))
        modalWindow.show()

app = QtGui.QApplication(sys.argv)
widget = AlarmClock()
widget.setFixedSize(400, 300)
widget.show()

sys.exit(app.exec_())