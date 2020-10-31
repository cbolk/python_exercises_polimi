# Write a program that asks the user a string containing only numeric characters, computes and outputs the corresponding integer value,
# or False if input contains non-numeric characters.

#Write it without using "int()" built-in cast.

BASE = 10
validInput = True
s = str(raw_input())
i = 0
powerOfTen=1
result = 0
while i<len(s) and validInput:
    digit = s[i]
    if digit<'0' or digit>'9':
        validInput = False
    else:
        intValue = ord(digit)-48   #magic ????
        result = result * BASE + intValue
        i += 1

if validInput:
    print(result)
else:
    print(validInput)
