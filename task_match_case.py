http_status = 400
if http_status == 400:
    print("Bad Request")
elif http_status == 403:
    print("Forbidden")
elif http_status == 404:
    print("Not Found")
else:
    print("Other")


day = "Monday"
if day == "Sunday":
    print("Take it easy")
elif day == "Monday":
    print("Go to work")
elif day == "Tuesday":
    print("Work + Hobbies")
elif day == "Wednesday":
    print("Meetings")
elif day == "Thursday":
    print("Presentations")
elif day == "Friday":
    print("Interviews and party")
elif day == "Saturday":
    print("Time to do sports")