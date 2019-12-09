    def printWorkSchedule(self, ssn):
        #Gets a tuple consisting of an instance of a staff member and their designated voyages
        ret_str = "####\nWork Schedule\n####\n"
        work_plan_tuple = self.printer.getWorkScheduleForCrewMember(ssn)
        staff = work_plan_tuple[0]
        staff_info = "\n{:<20} {:<15} {:<15} {:<20}".format(staff.name, staff.ssn, staff.role, staff.rank)
        frame = "\n" + "=" * len(staff_info)

        schedule = ""
        plan = work_plan_tuple[1]
        if len(plan) == 0:
            schedule = "\nNo voyages for the upcoming week."
        for entry in plan:
            departureDate, departureTime = entry.departure
            arrivalDate, arrivalTime = entry.arrival
            schedule += "\n{:<15} {:<15} {:<11} {:<5}\n{:>43} {:>5}".format(departureDate, entry.destinationAirport, "Departure: ", departureTime, "Arrival: ", arrivalTime)

        ret_str += frame + staff_info + frame + schedule
        print(ret_str)

<<<<<<< HEAD
=======
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
>>>>>>> c8e58cf02c07bbe7952daca492de3c826d8b77f9
