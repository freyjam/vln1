import datetime
def reverseIsoformat(isotime, whatTime, number):
    year, month, day = isotime[:4], isotime[5:7] ,isotime[8:10]
    hour, minutes = isotime[11:13], isotime[14:16] 
    dateTest = year + month + day + hour + minutes
    if whatTime == 'days':
        tesst = (datetime.datetime.strptime(str(dateTest),"%Y%m%d%H%M") + datetime.timedelta(days=number)).strftime("%Y%m%d%H%M")

    elif whatTime =='minutes':
        tesst = (datetime.datetime.strptime(str(dateTest),"%Y%m%d%H%M") + datetime.timedelta(minutes=number)).strftime("%Y%m%d%H%M")
    print(isotime)
    print(tesst)

    year, month, day = isotime[:4], isotime[5:7] ,isotime[8:10]
    hour, minutes = isotime[11:13], isotime[14:16] 

    print('{}/{}/{} {}:{}'.format(tesst[:4],tesst[4:6], tesst[6:8], tesst[8:10], tesst[10:12]))
    #return int(year) int(month), int(day), int(hour), int(minutes)


timed = reverseIsoformat('2010-01-03T18:00:00', 'days', 30 )


"""

    def getCurrentDateAndTimeISO(self):
        '''Returns the current date and time on iso format'''
        hours, minutes = str(datetime.now().strftime('%H:%M')).split(':')
        year, month, day = str(date.today()).split('-')
        return datetime(int(year), int(month), int(day), int(hours), int(minutes), 0).isoformat()
        """