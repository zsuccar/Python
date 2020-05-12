x = 41

if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is greater than 20")
    if x > 30:
        print("x is greater than 30")
    else:
        print("not cond 1")
else:
    print("none of the values")

table = int(input("number of person: \n"))
if int(table) > 8:
    print("you have to wait")
else:
    print("table is ready")

checknumber = int(input("enter the number: \n"))
if checknumber % 10 == 0:
    print("the number is divided by 10")
else:
    print("the number is not divided by 10")

insertvalue = float(input("insert a value between 1 and 100 : \n"))
if insertvalue < 1 or  insertvalue > 100:
    print("invalid number")
elif insertvalue % 5 == 0:
    print("HI Five")
elif insertvalue%2 ==0:
    print("HiEven")
elif insertvalue%2 ==0 and insertvalue%5 ==0:
    print("HighFive and HighEven")
else:
    print("Good Job")