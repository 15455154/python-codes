import pandas as pd

print("Hi, Mister! This is the bio data collector.")
print("I will collect a few of your details. Let's start!")

user_number = input("Please enter your phone number: ")
user_name = input("Please enter your name: ")
user_dob = input("What is your date of birth: ")
user_city = input("What is your city name: ")
user_age = input("What is your age: ")
user_quali = input("What is your qualification: ")
user_blood = input("What is your blood type: ")
user_height = float(input("What is your height (in meters): "))
user_weight = int(input("What is your weight (in kilograms): "))
user_nationality = input("What is your nationality: ")
user_sex = input("What is your gender: ")
user_password = input("Please create a password: ")

user_qus = input("What information do you need (e.g., name, birth date, etc.): ")

er_enter = input("Please enter your password: ")
if er_enter == user_password:
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
        print("Thank you for using the bio data collector!")
else:
    print("Incorrect password!")

# Create a DataFrame with the collected data
data = {
    'Name': [user_name],
    'Age': [user_age],
    'City': [user_city],
    'Date of Birth': [user_dob],
    'Phone Number': [user_number],
    'Qualification': [user_quali],
    'Blood Type': [user_blood],
    'Height': [user_height],
    'Weight': [user_weight],
    'Nationality': [user_nationality],
    'Gender': [user_sex]
}

df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
excel_file = 'bio_data.xlsx'
df.to_excel(excel_file, index=False)

print(f"Data has been saved to {excel_file}")
