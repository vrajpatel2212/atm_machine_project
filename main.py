name = input("Enter your name:")
print()
print(name,"WELCOME TO THE ATM\n")
user_input = int(input("Enter your PIN:"))
PIN = 2212
if user_input == PIN:
  print("Your PIN is correct. \n You have to your account.")
else:
  print("Your PIN is incorrect. \n You can't access to your account. \n Try again.")
  print()
  for i in range(3):
    user_input = int(input("Enter your PIN again:"))
    if user_input == PIN:
      print()
      print("Your PIN is correct. \n You have to your account.")
      break
    else:
      print("Your PIN is incorrect. \n You can't access to your account. \n Try again.")
      print("You have",2-i,"Chances left")
      print()
      if i == 2:
        print("You have no chance left. \nYou can't access to your account \nPlease try again later.")
        exit()
balance = 20000
print("Your balance is: ", balance)
print()
user_input = input("What do you want to do? \n1. Withdraw money \n2. Deposit money \n3. Check balance \n What do you want to do?(1/2/3):")
if user_input == "1":
  print()
  print("You want to withdraw money")
  money = int(input("Enter the amount of money you want to withdraw: "))
  if money < 100:
    print()
    print("You can't withdraw money below our minimum limit")
    print("Minimum limit is: 100")
  elif money < balance:
    print()
    print("You have withdrawn", money, "from your account")
    print("Your remaining balance is:", balance - money)
  elif money > balance:
    print()
    print("You don't have sufficient balance")
    print("Your balance is", balance)
  else:
    print()
    print("This amount is same as your balance")
    user_input = input("Do you still want to withdraw money?(yes/no):")
    if user_input == "yes":
      print()
      print("You have withdrawn", money, "from your account")
      print("Your remaining balance is:", balance - money)
    else:
      print()
      print("That's okay")
      print("Thank you for visiting th ATM")
      print("Vist us again")
      print("Have a great day!")
elif user_input == "2":
  print()
  print("You want to deposit money.")
  money = int(input("How much money do you wnat to deposit:"))
  print("You have deposited", money, "to your account")
  print("Your balance is:", balance + money)
else:
  print("Your balance is:",balance)
