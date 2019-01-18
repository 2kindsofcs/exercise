#!/bin/python3

import os
import sys


def timeConversion(s):
	hour = s[:2]
	am_pm = s[-2:]
	min_sec = s[2:-2]

	if am_pm == "AM" and hour == "12":
		hour = "00"
	elif am_pm == "PM" and hour != "12":
		hour = str(int(hour) + 12)
	return hour + min_sec

# AM and 12? -> hour=00 +minsec
# PM and not 12 -> hour+12  + minsec
# others: return hour + minsec
# 뭔가 반복되는 게 쌔하다 -> 변수에 담을 수 있는지 확인할 것
# 뭔가 반복되는 게 쌔하다(2) -> 사실상 한 가지 경우인데 너무 잘게 쪼개지 않았는지 확인할 것 (결국 앞의 것과 같은 맥락이지만)

# print(timeConversion("12:00:00AM"))
# print(timeConversion("01:20:00PM"))
# print(timeConversion("01:00:00AM"))
# print(timeConversion("04:23:00PM"))
# print(timeConversion("12:30:00PM"))


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
