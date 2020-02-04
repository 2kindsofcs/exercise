import "sort"

func solution(citations []int) int {
    length := len(citations)
    sort.Ints(citations)
    for index, value := range citations {
        if value >= (length - index) {
            return length - index
        }
    }
    return 0
}

// https://programmers.co.kr/learn/courses/30/lessons/42747#
