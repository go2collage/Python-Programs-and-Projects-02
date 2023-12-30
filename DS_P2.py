# Python Program / Project

balance = 0
a = 0           #Amount
d = []          #Deposited
w = []          #Withdrawal
num = 0
W = 0
D = 0

def deposit(num):
    global balance
    balance += num

def withdrawal(num):
    global balance
    balance -= num

while a != "Exit":
    a = input("Enter W for Withdrawal.\nEnter D for deposit. \nEnter 'Exit' to view the passbook details....\n")
    if (a == "W" or a == "w"):
        b = int(input("Enter withdrawal amount : "))
        if balance > b:
            w.append(b)
            withdrawal(b)
        else:
            print("You don't have Sufficient Balance. \nPlease Try Again Leter...\n")
    elif(a == "D" or a == "d"):
        c = int(input("Enter Depoit amount : "))
        deposit(c)
        d.append(c)

print("Your balance Remaining: ",balance)
print("Deposited Amount: ",d)
print("Withdrawal Amount: ",w)