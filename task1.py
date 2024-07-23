#def timeshit():
pro=input("enter project=")
#date=eval(input("enter project date="))
project1=["client1","client2","persnol","in house"]
for i in project1:
    if(pro==i):
        print("poroject exist project starts date is 16-7-24")
        date=eval(input("enter project date="))
        if(date==16-7-24):
            print("date exist")
        else:
            print("dont exist")

        time=eval(input("enter time="))
        if time>=0 and time<=9:
            print("valid time")
        else:
            print("invalid time")

        text=input("enter comment=")

    else:
        print("project does not exist")
        break

print("project is:",pro) 
print("project date is:",date)
print("time is:",time)
print("comment:",text)

#timeshit()




