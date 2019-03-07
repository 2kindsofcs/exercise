# https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=next-challenge&h_v=zen


def migratoryBirds(arr):
    totalNums = []
    for i in range(0,5):
        totalNums.append(arr.count(i+1))
    return (totalNums.index(max(totalNums))+1)