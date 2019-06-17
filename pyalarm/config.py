import os
import pickle

class Config:
    __CONFIG_FILE_PATH = "pyAlarm.cfg"

    def __init__(self): 
        if os.path.isfile(self.__CONFIG_FILE_PATH):
            with open(self.__CONFIG_FILE_PATH, "rb") as cfgFile:
                cfg = pickle.load(cfgFile)
                self.__alarms = cfg.__alarms
                self.__holidayUser = cfg.__holidayUser
                self.__holidayPassword = cfg.__holidayPassword
        else:
            self.__alarms = []
            self.__holidayUser = ""
            self.__holidayPassword = ""

    def save(self):
        with open(self.__CONFIG_FILE_PATH, "wb") as cfgFile:
            pickle.dump(self, cfgFile)

    def getAlarms(self):
        return self.__alarms
    
    def setAlarms(self, alarms):
        self.__alarms = alarms
    
    def getHolidayUser(self):
        return self.__holidayUser
    
    def getHolidayPassword(self):
        return self.__holidayPassword