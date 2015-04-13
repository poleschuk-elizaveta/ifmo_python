import time
from datetime import datetime
import webbrowser, os
import subprocess
class Clock():
    def __init__(self, alarm_time, isAlarm=True, isTimer=False):
        self.user_time = datetime.strptime(alarm_time, "%H:%M:%S")
        self.url = ''
        self.isCanceled = False

    def chooseASong(self, url):
        self.url = url
        print self.url

    def set(self):
        pass

    @property
    def clear(self):
        now = datetime.now().time()
        self.user_time = now
        return self

    def alarm(self, fromFile = False):
        print "Alarm!!! Get Up!!"
        try:
            if fromFile:
                os.startfile(self.url)
            else:
                webbrowser.open_new(self.url)
        except(AttributeError):
            print "You don't choose the song"

    def toSeconds(self, time_in_standart):
        time_in_second = time_in_standart.hour*60*60 + time_in_standart.minute*60 +time_in_standart.second
        return time_in_second

class Alarm(Clock):
    def __init__(self,  alarm_time):
        Clock.__init__(self,  alarm_time)
        print "I'm alarm"

    def set(self, fromFile = False):
        print "You set an alarm"
        while 1:
            now = datetime.now().time()
            if now.hour == self.user_time.hour and now.minute == self.user_time.minute:
                self.alarm(fromFile)
                break
            elif self.isCanceled:
                print "I'm canceled"
                break

class Timer(Clock):
    def __init__(self, time_to_break, alarm_time, final_time):
        Clock.__init__(self, alarm_time)
        self.time_to_break = datetime.strptime(time_to_break, "%H:%M:%S")
        self.final_time = datetime.strptime(final_time, "%H:%M:%S")
        print "I'm timer"

    def set(self, fromFile = False):
         while 1:
            now = datetime.now().time()
            if now.hour == self.final_time.hour and now.minute == self.final_time.minute:
                self.clear
                print "Exit of timing!"
                break
            elif self.isCanceled:
                print "I'm canceled"
                break
            else:
                time.sleep(self.toSeconds(self.user_time))
                self.alarm(fromFile)
                time.sleep(self.toSeconds(self.time_to_break))
