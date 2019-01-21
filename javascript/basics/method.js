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
    if (password.length > 8 && password.includes('password') === false){
        return true
    }
    else {
        return false
    }
}

console.log(isValidPassword("23423423password344"))