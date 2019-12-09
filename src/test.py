import datetime
<<<<<<< HEAD
def reverseIsoformat(isotime, whatTime, number):
    year, month, day = isotime[:4], isotime[5:7] ,isotime[8:10]
    hour, minutes = isotime[11:13], isotime[14:16] 
    dateTest = year + month + day + hour + minutes
    if whatTime == 'days':
        tesst = (datetime.datetime.strptime(str(dateTest),"%Y%m%d%H%M") + datetime.timedelta(days=number)).strftime("%Y%m%d%H%M")
=======
>>>>>>> 646ac466a214212ca440c09357c26156e8c401cc

def reverseIsoformat(isotime, whatToChange, howMany): 
    dateTest = isotime[:4] + isotime[5:7] + isotime[8:10] + isotime[11:13] + isotime[14:16]
    if whatToChange == 'days':
        newTime = (datetime.datetime.strptime(str(dateTest),"%Y%m%d%H%M") + timedelta(days=howMany)).strftime("%Y%m%d%H%M")
    elif whatToChange =='minutes':
        newTime = (datetime.datetime.strptime(str(dateTest),"%Y%m%d%H%M") + timedelta(minutes=howMany)).strftime("%Y%m%d%H%M")
    year, months, days, hours, minutes = newTime[:4], newTime[4:6], newTime[6:8], newTime[8:10], newTime[10:12]
    return datetime.datetime(int(year), int(months), int(days), int(hours), int(minutes)).isoformat()


<<<<<<< HEAD
=======
    print('{}/{}/{} {}:{}'.format(tesst[:4],tesst[4:6], tesst[6:8], tesst[8:10], tesst[10:12]))
    #return int(year) int(month), int(day), int(hour), int(minutes)
>>>>>>> e3318de570dea283f93fb79a1c8539bf391b32ae

print(reverseIsoformat('2010-01-03T18:00:00', 'minutes', 30 ))



<<<<<<< HEAD
"""

    def getCurrentDateAndTimeISO(self):
        '''Returns the current date and time on iso format'''
        hours, minutes = str(datetime.now().strftime('%H:%M')).split(':')
        year, month, day = str(date.today()).split('-')
        return datetime(int(year), int(month), int(day), int(hours), int(minutes), 0).isoformat()
        """
=======

def getCurrentDateAndTimeISO(self):
    '''Returns the current date and time on iso format'''
    hours, minutes = str(datetime.now().strftime('%H:%M')).split(':')
    year, month, day = str(date.today()).split('-')
    return datetime(int(year), int(month), int(day), int(hours), int(minutes), 0).isoformat()
>>>>>>> 646ac466a214212ca440c09357c26156e8c401cc
