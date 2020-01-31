package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func() int {
	num1, num2 := -1, 1
	return func() int {
		result := num1 + num2
		num1 = num2
		num2 = result
		return result
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}

// https://tour.golang.org/moretypes/26
