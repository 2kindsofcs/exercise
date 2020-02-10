package main

import (
	"fmt"
	"golang.org/x/tour/tree"
	"sort"
)

// Walk walks the tree t sending all values
// from the tree to the channel ch.
func Walk(t *tree.Tree, ch chan int) {
	queue := make([]*tree.Tree, 0)
	queue = append(queue, t)
	for len(queue) > 0 {
		el := queue[0]
		ch <- el.Value
		if el.Left != nil { // python이면 그냥 바로 if el.Left 해서 있으면 True고 없으면 False일텐데 ...
			queue = append(queue, el.Left)
		}
		if el.Right != nil {
			queue = append(queue, el.Right)
		}
		queue = queue[1:]
	}
	// 닫아주지 않으면 deadlock 에러
	close(ch) 
}

// Same determines whether the trees
// t1 and t2 contain the same values.
func Same(t1, t2 *tree.Tree) bool {
	ch1, ch2 := make(chan int), make(chan int)
	go Walk(t1, ch1)
	go Walk(t2, ch2)
	slice1, slice2 := make([]int, 0), make([]int, 0)
	
	// for <Initialize>; <condition>; <increment>  라는 걸 명심하자.
	for {
		v1, v2 := <-ch1, <-ch2 
		if v1 == 0 && v2 == 0 {
			break
		}
		slice1 = append(slice1, v1)
		slice2 = append(slice2, v2)
	}

	sort.Ints(slice1)
	sort.Ints(slice2)
	
	length := len(slice1)
	result := true
	
	for i:=0; i<length; i++ {
		if slice1[i] != slice2[i] {
			result = false
		}
	}
	
	return result
}

func main() {
	fmt.Println(Same(tree.New(1), tree.New(1)))
	fmt.Println(Same(tree.New(1), tree.New(2)))
}
