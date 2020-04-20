package main

import (
	"github.com/aws/aws-lambda-go/lambda"
	"math/rand"
)

type QuestionEvent struct {
	Question string `json:"question"`
}

type GodoongResponse struct {
	Answer string `json:"answer"`
}

func HandleRequest(event QuestionEvent) (GodoongResponse, error) {
	var answer string
	num := rand.Intn(10)
	if num % 2 == 0 {
		answer = "yes"
	} else {
		answer = "no"
	}
	return GodoongResponse{answer}, nil
}

func main() {
	lambda.Start(HandleRequest)
}
