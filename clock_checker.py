import threading
# from gpiozero import Button
from datetime import datetime, timedelta
from gpiozero import Button, LED
import time

'''
This class creates a thread that runs a While loop, and every second checks if
it's wakeup time.
If the time is in wake up time range and the sensor is not closed -> Ring until the sensor closes
or the wake up time ends (depending on alarm_interval)
'''

class ClockChecker():

    def __init__(self):
        self.alarm_interval = 30
        self.th = threading.Thread(target=self.wait_for_clock, daemon=True).start()  # Creating thread, passing wait_for_clock func
        self.button = Button(2)
        self.buzzer = LED(17)
        self.running = True
        self.hour = None
        self.minute = None

    def define_time(self, hour, minute):  # Updates the time
        self.hour = int(hour)
        self.minute = int(minute)

    def wakeup_routine(self):  # When this func is triggered the buzzer starts ringing
        while not self.button.is_pressed:
            self.buzzer.value = 1
            time.sleep(0.5)
            self.buzzer.value = 0
            time.sleep(0.5)
            print('Ringing...')

    def wait_for_clock(self):
        while 1:
            if (self.hour is not None and self.minute is not None and self.running):  # Checks if the time has been set
                time_now = datetime.now().replace(second=0, microsecond=0)
                wake_up_time = datetime.now().replace(hour=self.hour, minute=self.minute, second=0, microsecond=0)  # Sets wakeup time
                wake_up_end = wake_up_time + timedelta(minutes=self.alarm_interval)  # Sets endtime for waking up
                if (time_now >= wake_up_time and time_now < wake_up_end):  # Checks if it's the time to wake up
                    self.wakeup_routine()
                    print("ALARM ON")
                else:
                    print("Looping...")
                    print("Time (now): ", time_now)
                    print("Wakeup time: ", self.hour, ":", self.minute)
            time.sleep(1)

    def stop_alarm(self):
        self.running = False

    def start_alarm(self):
        self.running = True

    def get_wakeup_hour(self):
        return str(self.hour, ":", self.minute)
