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

