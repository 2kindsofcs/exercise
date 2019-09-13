def solution(phone_book):
    # 접두가 되려면 최소 접두번호의 길이가 되어야 하고
    # 접두 첫 글자와 어휘 첫 글자가 다르면 체크할 필요가 없음
    answer = True
    prefixList = [ [] for _ in range(10) ]
    for number in phone_book:
        prefixList[ord(number[0])-48].append(number)
    for number in phone_book:
        for prefixNumber in prefixList[ord(number[0])-48]:
            if number[:len(prefixNumber)] == prefixNumber and number != prefixNumber:
                return False
    return answer
