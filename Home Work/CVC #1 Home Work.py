#Task 1
x = int(input("Input the month : "))

def days_month(index):
    month = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    d_31 = (1,3,5,7,8,10,12)

    if index in d_31:
        print(f"{month[index]} : 31 days")
    elif index == 2:
        print(f"{month[index]} : 28/29 days")
    else:
        print(f"{month[index]} : 30 days")

days_month(x)


#Task 2
y = int(input("Input the year : "))
m = int(input("Input the month : "))

def days_month(m, y):
    month = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    d_31 = (1,3,5,7,8,10,12)

    if m in d_31:
        print(f"{month[m]} : 31 days")
    elif m == 2:
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            print(f"{month[m]} : 29 days")
        else:
            print(f"{month[m]} : 28 days")
    else:
        print(f"{month[m]} : 30 days")
        
days_month(m, y)