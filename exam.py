import csv
ans = ''
def ip():
    global ans
    with open('fund_database.csv', 'a', newline='') as fund_data:
        w = csv.writer(fund_data)
        ans = 'y'
        while ans == 'y':
            code = input("Enter unique code: ")
            print("Enter the following details")
            name = input("Student name: ")
            reason = input("Reason for payment \n(Donation - 1) \n(Fees - 2) \n(Event Charges - 3) \n(Others - 4) \n>")
            pay = input("Payment Method: ")
            amt = input("Amount Payed: ")
            user= [code, name, reason, pay, amt]
            w.writerows([user])
            ans = input("Do you want to add another record(y/n): ")


def output():
    print("Welcome to Student Fund Management System")
    print("What operation do you want to perform")
    while True:
        ch = int(input("1-Input data\n2-Update data\n3-Delete data\n4-Analyse data\n5-Show data\n6-Exit\n>"))
        if ch == 1:
            ip()
        elif ch == 2:
            update()
        elif ch == 3:
            delete()
        elif ch == 4:
            analyse()
        elif ch == 5:
            with open('fund_database.csv', 'r', newline='') as fund_data:
                data = csv.reader(fund_data)
                for i in data:
                    print(i)
        elif ch == 6:
            print("Exiting program")
            break
        else:
            print("Wrong choice entered")
            print("Enter correct choice")

def update():
    c = input("Enter the code of the student whose payment details are to be changed: ")
    with open("fund_database.csv", "r", newline="") as a:
        b = list(csv.reader(a))
        print(b)
    for i in b:
        if i[0] == str(c):
            print("Student name: ", i[1])
            print("Reason for payment: ", i[2])
            print("Payment method: ", i[3])
            print("Amount paid: Rs.", i[4])
            while True:
                ch = int(input("1-Students name\n2-Reason for payment\n3-Payment method\n4-Amount paid\n5-Done with updating data\n>"))
                if ch == 1:
                    i[1] = input("Enter new name: ")
                elif ch == 2:
                    i[2] = input("Enter new reason: ")
                elif ch == 3:
                    i[3] = input("Enter new payment method: ")#smth w i[3]
                elif ch == 4:
                    i[4] = input("Enter new amount paid: ")
                elif ch == 5:
                    break
                else:
                    print("Wrong choice entered")
            with open("fund_database.csv", "w", newline="") as a:
                w = csv.writer(a)
                w.writerows(b)
            print("Data updated successfully")
            break
    print("Code not found")

def analyse():
    met = input("Enter the type of analysis you want to do (avg/sum): ")
    with open("fund_database.csv", "r", newline="") as a:
        b = list(csv.reader(a))
    net = 0
    for i in b:
        net += float(i[-1])
    if met == 'avg':
        avg = net / len(b)
        print(f"The average amount received till date is {avg}")
    elif met == 'sum':
        print(f"The total sum of money received till date is {net}")
    else:
        print("Cannot understand. Please enter correct option.")

def delete():
    b = input("Enter the unique code of the record you would like to delete: ")
    with open("fund_database.csv", "r", newline="") as a:
        c = list(csv.reader(a))
        d = [i for i in c if i[0] != b]
    with open("fund_database.csv", "w", newline="") as a:
        w = csv.writer(a)
        w.writerows(d)

output()
