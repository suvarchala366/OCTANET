import time
print("Please Insert your Card")
time.sleep(5)
password=2003
pin=int(input("Enter your ATM pin"))
balance=1000
if pin==password:
    while True:
       print("""
           Invalid choice!Please Enter Valid choice
           1 == balance
           2 == withdraw_balance
           3 == deposit_balance
           4 == exit
           """
             )
       try:
          option=int(input("Enter your choice"))
       except:
          print("Invalid choice!Please Enter Valid choice")


       if option==1:
          print(f"Your Current Balance is {balance}")
          print("===================================================")
        
       if option==2:
          withdraw_amount=int(input("Enter your Withdraw Amount"))
          if withdraw_amount<=balance:
              balance=balance-withdraw_amount
              print(f"{withdraw_amount} is debited from your account")
              print(f"Your Balance is Updated!And your Updated Balance is {balance}")
              print("===================================================")
          else:
              balance=balance-withdraw_amount
              print(f"{withdraw_amount} is debited from your account")
              print(f"Your Balance is Updated!And your Updated Balance is {balance}")
              print("Insufficient amount to withdraw")
              print("===================================================")
       if option==3:
         deposit_amount=int(input("Please enter Deposit Amount"))
         balance=balance+deposit_amount
         print(f"{deposit_amount} is credited from your account")
         print(f"Your Balance is Updated!And your Updated Balance is {balance}")
         print("===================================================")

       if option==4:
         print("===================================================")
         break

else:
    print("You've Entered Wrong Pin! Please Check it!")
    print("===================================================")