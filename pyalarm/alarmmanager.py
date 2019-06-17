from datetime import datetime

from pyalarm.config import Config

class AlarmManager:
    def __init__(self, config):
        self.config = config

    def alarmAvailable(self, currentDateTime):
        triggerAlarm = False

        for alarm in self.config.getAlarms():
            triggerAlarm |= self.__compareDate(currentDateTime, alarm)

        return triggerAlarm

    def __compareDate(self, datetime, alarm):
        result = True
        result &= datetime.weekday() in alarm.getWeekdays()
        result &= datetime.hour == alarm.getHour()
        result &= datetime.minute == alarm.getMinute()
        result &= datetime.second == 0

        return result