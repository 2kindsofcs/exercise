// 메소드 만들어보기 

let restaurant = {
    name: 'ASB',
    guestCapacity: 75,
    guestCount: 0,
    checkAvailability: function (partySize) {
        let seatsLeft = this.guestCapacity - this.guestCount
        return partySize <= seatsLeft
    },
    seatParty: function (partySize) {
        this.guestCount = this.guestCount + partySize
    },
    removeParty: function (partySize) {
        this.guestCount = this.guestCount - partySize
    }
}

restaurant.seatParty(72);
console.log(restaurant.checkAvailability(4))


// 내장 메소드 사용하기 

let isValidPassword = function (password) { 
    return (password.length > 8 && !password.includes('password')){ // ===false 대신 앞에 ! 붙여서 보다 간결하게
    // 위 두 조건이 동시에 충족되지 않았을 경우, false를 리턴하는 것 외의 행위가 전혀 없으므로
    // 이 조건 판단의 결과 자체를 그대로 return해도 상관이 없다. 
}

console.log(isValidPassword("23423423password344"))