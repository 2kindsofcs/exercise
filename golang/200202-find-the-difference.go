import "strings"

func findTheDifference(s string, t string) byte {
    alphabets := "abcdefghijklmnopqrstuvwxyz"
    var letterCounts [26]int
    for _, element := range s {
        index := strings.Index(alphabets, string(element))
        letterCounts[index] += 1
    }
    for _, element := range t {
        index := strings.Index(alphabets, string(element))
        letterCounts[index] -= 1
        if letterCounts[index] < 0 {
            return byte(element)
        }
    }
    return byte(0)
}

// Runtime: 0 ms, faster than 100.00% of Go online submissions for Find the Difference.
// Memory Usage: 2.2 MB, less than 100.00% of Go online submissions for Find the Difference.
