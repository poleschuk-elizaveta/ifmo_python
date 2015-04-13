import clock
from PyQt4 import QtGui, QtCore, uic
import sys
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
        #self.threadForAlarm = Thread(target=self.alarmClock.set)
        #self.urlLine.textEdited

        self.alarmTime.setTime(QtCore.QTime.currentTime())
        self.setAlarmClock.clicked.connect(self.timeForAlarm)
        self.cancel.clicked.connect(self.cancelAlarm)

    def timeForAlarm(self):
        self.alarmClock = clock.Alarm(str(self.alarmTime.time().toString()))
        self.alarmClock.isCanceled = False
        self.threadForAlarm = Thread(target=self.alarmClock.set)
        self.threadForAlarm.daemon = True
        self.threadForAlarm.start()
        #self.threadForAlarm.run()
        #self.alarmClock.set()
        self.alarmClock.chooseASong(str(self.urlLine.textEdited))



    def cancelAlarm(self):
        #self.threadForAlarm.kill()
        self.alarmClock.isCanceled = True
        print "Cancel!"
        #self.alarmClock.clear
app = QtGui.QApplication(sys.argv)
widget = AlarmClock()
widget.show()

sys.exit(app.exec_())