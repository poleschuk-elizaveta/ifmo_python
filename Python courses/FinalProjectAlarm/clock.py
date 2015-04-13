import time
from datetime import datetime
import webbrowser

class Clock():
    def __init__(self, alarm_time, isAlarm=True, isTimer=False):
        self.user_time = datetime.strptime(alarm_time, "%H:%M:%S")
        self.url = ''

    def chooseASong(self, url):
        self.url = url
        return self.url

    def set(self):
        pass

    @property
    def clear(self):
        now = datetime.now().time()
        self.user_time = now
        return self

    def alarm(self):
        pass

    def toSeconds(self, time_in_standart):
        time_in_second = time_in_standart.hour*60*60 + time_in_standart.minute*60 +time_in_standart.second
        return time_in_second

class Alarm(Clock):
    def __init__(self,  alarm_time):
        Clock.__init__(self,  alarm_time)
        self.isCanceled = False
        print "I'm alarm"

    def set(self):
        print "You set an alarm"
        #my_time = time.mktime(tm_hour=self.hour, tm_min=self.minute)
        #time.strftime("%H:%M:%S", now)
        while 1:
            now = datetime.now().time()
            if now.hour == self.user_time.hour and now.minute == self.user_time.minute:
                self.alarm()
                break
            elif self.isCanceled:
                print "I'm canceled"
                break
        """now_time_in_seconds = self.toSeconds(datetime.now())
        seconds_in_one_day = 24*60*60
        user_time_in_seconds = self.toSeconds(self.user_time)
        if now_time_in_seconds > user_time_in_seconds:
            # usertime already passed today, set for tomorrow
            secs_to_midnight = (seconds_in_one_day - now_time_in_seconds)
            # 186400 -> seconds in 1 day
            sleep_time = secs_to_midnight + user_time_in_seconds
        else:
            # Time is for today
            sleep_time = user_time_in_seconds - now_time_in_seconds
        time.sleep(sleep_time)
        self.alarm()"""

    def alarm(self):
        print "Alarm!!! Get Up!!"
        try:
            webbrowser.get('mozilla').open_new(self.url)
        except(AttributeError):
            print "You don't choose the song"

class Timer(Clock):
    def __init__(self, time_to_break, alarm_time, final_time):
        Clock.__init__(self, alarm_time)
        #super(Timer, self).__init__(alarm_time)
        self.time_to_break = datetime.strptime(time_to_break, "%H:%M:%S")
        self.final_time = datetime.strptime(final_time, "%H:%M:%S")
        print "I'm timer"

    def set(self):
         while 1:
            now = datetime.now().time()
            if now.hour == self.final_time.hour and now.minute == self.final_time.minute:
                self.clear
                print "Exit of timing!"
                break
            else:
                time.sleep(self.toSeconds(self.user_time))
                self.alarm()
                time.sleep(self.toSeconds(self.time_to_break))
    def alarm(self):
        print "Time to break!!!"
        open(self.url)