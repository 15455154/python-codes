print("hi mister this is the bio data collector")
print("i will collect few of your details")
print("okey lets start")

user_name = input("PLEASE Enter your name MR :")
user_dob = input("What is your date of birth :")
user_age = input("What is your age :")
user_quali = input("What is your qualification :")
user_blood = input("what is your blood type :")
user_height = input("what is your height :")
user_weight = input("What is your weight :")
user_nationality = input("What is your nationality :")
user_sex = input("what is your gender :")

user_qus = input("What do you need: ")



if user_qus == "name" :
   print(user_name)   

if user_qus == "birth date":
 print(user_dob)

if user_qus == "age":
 print(user_age)

if user_qus == "qualification":
 print(user_quali)

if user_qus == "blood group":
 print(user_blood)
 
if user_qus == "height":
 print(user_height)
 
if user_qus == "weight":
 print(user_weight)
 
if user_qus =="nationlality":
 print(user_nationality)
 
if user_qus == "gender":
 print(user_sex)
if user_qus == "close":
 quit()
