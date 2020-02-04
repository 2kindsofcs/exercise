func solution(clothes [][]string) int {
    result := 1
    clothesDic := make(map[string][]string)
    for _, element := range clothes {
        category := element[1]
        if clothesDic[category] == nil {
            clothesDic[category] = make([]string, 0, 30)
        }
        clothesDic[category] = append(clothesDic[category], element[0])
    }
    for _, category := range clothesDic {
        result = result * (len(category) + 1)
    }
    result = result - 1
    return result
}

// https://programmers.co.kr/learn/courses/30/lessons/42578?language=go
