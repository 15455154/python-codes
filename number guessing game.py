print("Hi, Mister! This is the bio data collector.")
print("I will collect a few of your details. Let's start!")
user_number = input("please enter your phone number")
user_name = input("Please enter your name: ")
user_dob = input("What is your date of birth: ")
user_age = input("What is your age: ")
user_quali = input("What is your qualification: ")
user_blood = input("What is your blood type: ")
user_height = float(input("What is your height (in meters): "))
user_weight = int(input("What is your weight (in kilograms): "))
user_nationality = input("What is your nationality: ")
user_sex = input("What is your gender: ")
user_password = input("please create a password")
BMI = user_weight / (user_height ** 2)

if BMI < 18.5:
    print("your BMI is Underweight")
elif 18.5 <= BMI < 25:
    print("your BMI is Normal")
elif 25 <= BMI < 30:
    print("your BMI is Overweight")
else:
    print("your BMI is Obese")

user_qus = input("What information do you need (e.g., name, birth date, etc.): ")
user_enter = input("please enter your password")
if user_enter == user_password: 
 if user_qus == "name":
    print(user_name)
 elif user_qus == "number":
    print(user_number)
 elif user_qus == "birth date":
    print(user_dob)
 elif user_qus == "age":
    print(user_age)
 elif user_qus == "qualification":
    print(user_quali)
 elif user_qus == "blood group":
    print(user_blood)
 elif user_qus == "height":
    print(user_height)
 elif user_qus == "weight":
    print(user_weight)
 elif user_qus == "nationality":
    print(user_nationality)
 elif user_qus == "gender":
    print(user_sex)
 elif user_qus == "close":

  print("Thank you for using the bio data collector!")

user_qus = input("What information do you need (e.g., name, birth date, etc.): ")

if user_qus == "name":
    print(user_name)
elif user_qus == "birth date":
    print(user_dob)
elif user_qus == "age":
    print(user_age)
elif user_qus == "qualification":
    print(user_quali)
elif user_qus == "blood group":
    print(user_blood)
elif user_qus == "height":
    print(user_height)
elif user_qus == "weight":
    print(user_weight)
elif user_qus == "nationality":
    print(user_nationality)
elif user_qus == "gender":
    print(user_sex)
elif user_qus == "close":
    print("Thank you for using the bio data collector!")

    user_qus = input("What information do you need (e.g., name, birth date, etc.): ")

if user_qus == "name":
    print(user_name)
elif user_qus == "birth date":
    print(user_dob)
elif user_qus == "age":
    print(user_age)
elif user_qus == "qualification":
    print(user_quali)
elif user_qus == "blood group":
    print(user_blood)
elif user_qus == "height":
    print(user_height)
elif user_qus == "weight":
    print(user_weight)
elif user_qus == "nationality":
    print(user_nationality)
elif user_qus == "gender":
    print(user_sex)
elif user_qus == "close":
    print("Thank you for using the bio data collector!")
 