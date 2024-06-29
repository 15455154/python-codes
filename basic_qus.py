ans = input("your school is VVS .   True or false: ")
#cretes a variable in which a input from a user is stored
ans = ans.lower()
#makes the answer to smaller case
if ans == "true" :
    print("yes you are absolutely correct")
#cheaks the answer and if true prints
else:#if NOT true
    print("Sorry your wrong please try again")
    ans = input("your school is VVS .   True or false: ")
    ans = ans.lower() 
    if ans == "true" :
        # if answer is correct print yes you are absolutely correct
     print("yes you are absolutely correct")
     # if answer is wrong print Sorry your wrong please try again
    else:
     print("Sorry your wrong please try again")
