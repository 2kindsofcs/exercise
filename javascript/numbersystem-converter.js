import { stack } from './stack.js'

// 2진수부터 9진수까지만 동작

let converter = function(number, base) {
    let numStack = new stack();
    let n = number;
    let result = "";
    while (n > 0) {
        numStack.push(n % base);
        n = Math.floor(n/base);
    }
    while (numStack.top > -1) {
        result += String(numStack.pop())
    }
    return result;
}

console.log(converter(32,2));


