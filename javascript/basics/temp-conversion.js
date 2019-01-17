let fahrenheit = 32;
let celcius = (fahrenheit - 32) * 5/9;
let calvin = celcius + 273.15;

let fahrenheitConvert = function(fahrenheit) {
    let celcius = (fahrenheit - 32) * 5/9
    return celcius
}

console.log(fahrenheitConvert(45));

let temp = 80;
let temp2 = -10;
if (temp >=60 && temp <=90) {
    console.log("it's pretty nice out")    
} else if (temp > 90 || temp2 <= 0) {
    console.log("don't go outside")
}


