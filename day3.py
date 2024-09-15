
print ("welcome for rollercoaster")
height= int(input("what is your height"))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("enter your age " ))

    if age <=12:
       bill = 5
       print("your tikcket $5") 

    elif age <= 18:
      bill = 7
      print("Your ticket prices $7")
    
    elif age <= 20:
       bill = 16
       print("your ticker price $16")
    
    elif age >=45: #and age <=50:
       bill = 25
       print("yout  ticket $ 25")
     
    else:
       bill = 12
       print("your ticket prices $12")
    
    want_picture = input("Do you want a picture taken? Type 'yes' or 'no':")
    
    if want_picture == "yes":

        bill += 3

    print(f"your bill total ${bill}")

else:
    print("you can not ride the rollercoaster")  
