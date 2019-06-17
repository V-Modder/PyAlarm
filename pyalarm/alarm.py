class Alarm:
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
    ALLDAYS = [MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY]

    def __init__(self, weekdays=ALLDAYS, hour=8, minute=0):
        self.__weekdays = weekdays
        self.__hour = hour
        self.__minute = minute

    def getWeekdays(self):
        return self.__weekdays
    
    def getHour(self):
        return self.__hour
    
    def setHour(self, hour):
        self.__hour = hour
    
    def getMinute(self):
        return self.__minute

    def setMinute(self, minute):
        self.__minute = minute

    def presentationString(self):
        return "{}:{} at {}".format(self.__hour, self.__minute, self.__getWeekdaysString())

    def __getWeekdaysString(self):
        result = ""
        i = 0
        for day in self.__weekdays:
            if i > 0:
                result += ". "
            result += self.__getWeekdayName(day)
            i += 1
        return result

    def __getWeekdayName(self, day):
        if day == 0:
            return "Monday"
        elif day == 1:
            return "Tuesday"
        elif day == 2:
            return "Wednesday"
        elif day == 3:
            return "Thursday"
        elif day == 4:
            return "Friday"
        elif day == 5:
            return "Saturday"
        elif day == 6:
            return "Sunday"