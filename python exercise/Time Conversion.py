#!/bin/python3

import os
import sys

# 선생님이 보너스(?)로 만약 자기라면 이렇게 더 고칠 거라고 하셨다. 
# hour을 처음부터 정수로 만들고 후반부에 format함수로 깔끔하게 정리하는 것.

def timeConversion(s):
	hour = int(s[:2])
	is_am = s[-2:] == "AM"
	min_sec = s[2:-2]

	if is_am and hour == 12:
		hour = 0
	elif not is_am and hour != 12:
		hour = hour + 12
	return "{0:02}".format(hour) + min_sec


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
