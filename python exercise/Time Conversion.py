#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == "PM":
        if s[0:2] == "12":
            return s[0:8]
        else:
            hour = int(s[0:2]) + 12
            result = str(hour) + s[2:8]
            return result
    else:
        return s[0:8]


    # if iis am then leave it alone
    # if its pm then plus 12(h)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
