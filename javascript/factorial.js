import { stack } from './stack.js'

/** 
 * @param {number} number
 */

const factorial = function (number) {
    let numStack = new stack;
    let result = 1;
    if (typeof(number) != "number" || number < 1 ) {
        console.log("1 이상의 자연수를 입력하세요")
        return 
    }
    while (number > 0) {
        numStack.push(Math.floor(number))
        number--; 
    }
    while (numStack.top > -1) {
        result = result * numStack.pop();
    }
    return result
}
