#code updated very soon
#password validation project
#mini project
#condition
#length of the password should be in between 6 to 12 both included
#atleast one [a-z]
#atleast one [A-Z]
#atleast one [0-9]
#atleast one [@#$%&]
import re
import sys
pwd = input("enter the password")
while True:
    if len(pwd)<6 or len(pwd)>12:
        break
    elif not re.search('[a-z]',pwd):
        break
    elif not re.search('[0-9]',pwd):
        break
    elif not re.search('[A-Z]',pwd):
        break
    elif not re.search('[@#$%&]',pwd):
        break
    elif re.search('\s',pwd):
        break
    else:
        print("valid password:",pwd)
        sys.exit()

print("invalid password:",pwd)

#here we completed our project successfully.###
# it was a mini project
#hence it can be proved







