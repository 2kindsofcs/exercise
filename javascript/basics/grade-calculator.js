let gradeCalculator = function (score, totalscore) {
    let percent = score / totalscore * 100;
    let grade; 
    if (percent > 100 || percent < 0){
        return "you cheated";
    }
    else if (90 <= percent){  //else if는 "앞의 조건이 아닐 경우"라는 뜻을 포함하고 있기 때문에 여기서 100 이하인지는 체크할 필요가 없음
        grade = 'A';
    }
    else if (80 <= percent){ // 여기도 마찬가지로 90 미만인 것이 이미 확인되었으므로 && percent<=90 같은 걸 적어 줄 필요가 없음
        grade = 'B';
    }
    else if (70 <= percent){
        grade = 'C';
    }
    else if (60 <= percent){
        grade = 'D';
    }
    else {
        grade = 'F';
    }
    return `You got a ${grade}(${percent}%)!`
}
console.log(gradeCalculator(60,100))