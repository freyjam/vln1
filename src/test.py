import datetime

def reverseIsoformat(isotime, whatToChange, howMany): 
    dateTest = isotime[:4] + isotime[5:7] + isotime[8:10] + isotime[11:13] + isotime[14:16]
    if whatToChange == 'days':
        newTime = (datetime.datetime.strptime(str(dateTest),"%Y%m%d%H%M") + timedelta(days=howMany)).strftime("%Y%m%d%H%M")
    elif whatToChange =='minutes':
        newTime = (datetime.datetime.strptime(str(dateTest),"%Y%m%d%H%M") + timedelta(minutes=howMany)).strftime("%Y%m%d%H%M")
    year, months, days, hours, minutes = newTime[:4], newTime[4:6], newTime[6:8], newTime[8:10], newTime[10:12]
    return datetime.datetime(int(year), int(months), int(days), int(hours), int(minutes)).isoformat()



print(reverseIsoformat('2010-01-03T18:00:00', 'minutes', 30 ))




def getCurrentDateAndTimeISO(self):
    '''Returns the current date and time on iso format'''
    hours, minutes = str(datetime.now().strftime('%H:%M')).split(':')
    year, month, day = str(date.today()).split('-')
    return datetime(int(year), int(month), int(day), int(hours), int(minutes), 0).isoformat()
