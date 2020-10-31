# Your hospital uses a format to represent temperatures (expressed in Celsius integer degrees)
# measured during the 12 months of the current year.
# the format is fixed:
# 5,6,7,12,16,25,26,22,18,10,5,5
# Write a program that asks the user a string containing 12 temperatures, computes and outputs
# a histogram plot of values using '*' for every 5 degrees, or False if string is not correct, or a value# is negative
# the histogram spans from 0 to 30 degrees.
# write the scale on left.
# Don't use find
#Example:


# 30:
# 25:      **
# 20:      ***
# 15:     *****
# 10:    *******
# 05: ************


N_OF_MONTHS = 12
temperatures = str(raw_input())
len = len(temperatures)
month = 0

i=0
prev=0
error = False

while i<len and not error:
    ch = temperatures[i]
    if ch == ",":
        s = temperatures[prev:i]
        if s.isdigit():
            t = int(s)
            prev=i+1
            month+=1
        else:
            error = True
    i += 1

if not error:    # take last number:
    s = temperatures[prev:i]
    if s.isdigit():
        t = int(s)
        month += 1
    else:
        error = True

if not error and month == N_OF_MONTHS:
# same loop but inside a loop for values between 0..30 in steps of 5:

    for degrees in range(30, 0, -5):    
        line = '{:0>2}'.format(degrees)  + ": "

        # same loop but no more checks, string is valid:
        i=0
        prev=0
        while i<len and not error:  # e che errore potremmo avere?
            ch = temperatures[i]
            if ch == ",":
                s = temperatures[prev:i]
                t = int(s)
                prev=i+1
                if t >= degrees:
                    line += "*"
                else:
                    line += " "
            i += 1

        #perche' c'era un if che mi pareva essere sempre vero?
        s = temperatures[prev:i]
        t = int(s)
        if t >= degrees:
            line += "*"
        else:
            line += " "

        print(line)
else:
    print(False)
