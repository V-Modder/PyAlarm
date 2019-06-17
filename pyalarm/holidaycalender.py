import json
import re
import requests
from datetime import datetime


class HolidayCalendar:
    __timetasticBaseUrl = "https://app.timetastic.co.uk"

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def isHoliday(self, date):
       session = requests.session()
       requestToken = self.__recieveRequestToken(session)
       self.__login(session, requestToken)
       wallchartResponse = session.get(self.__timetasticBaseUrl + "/WallChart/GetCalendarData/?userId=423622&year=" + str(date.year) + "&_=1560027332987")
       return self.__parseResponse(wallchartResponse.text, date)

    def isHolidayToday(self):
        return self.isHoliday(datetime.now())

    def __recieveRequestToken(self, session):
        loginPageResponse = session.get(self.__timetasticBaseUrl + "/login")
        return self.__extractRequestToken(loginPageResponse.text)
    
    def __extractRequestToken(self, loginPage):
        reg = re.compile(r'__RequestVerificationToken" type="hidden" value="(.*)"')
        match = reg.search(loginPage)
        return match.groups()[0]
    
    def __login(self, session, requestToken):
        loginData = self.__createLoginData(requestToken)
        session.post(self.__timetasticBaseUrl + "/Account/login?returnurl=/calendar", data=loginData)

    def __createLoginData(self, requestToken):
        loginData = {"Email": "j.ewers@setlog.com",
            "Password": "Vektore",
            "__RequestVerificationToken": requestToken}
        return loginData
    
    def __parseResponse(self, wallchartResponse, date):
        wallchart = json.loads(wallchartResponse)
        givenMonth = date.month
        matchingMonth = None
        for month in wallchart["months"]:
            if month["monthNum"] == givenMonth:
                matchingMonth = month
        
        if matchingMonth is None:
            return False
        return self.__nonWorkingDaysAreToday(matchingMonth["nonworkingdays"], date.day) or self.__holdidaysAreToday(matchingMonth["holidays"], date.day)
            
    def __nonWorkingDaysAreToday(self, nonWorkingDays, day):
        for nonWorkingDay in nonWorkingDays:
            if nonWorkingDay["dayOffset"] == day - 1:
                return True
        return False

    def __holdidaysAreToday(self, holidays, day):
        for holiday in holidays:
            if holiday["day"] + 1 == day and (holiday["am_lt_name"] == "Holiday" or holiday["am_lt_name"] == "Sick Leave"):
                return True
        return False
