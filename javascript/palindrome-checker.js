import { stack } from './stack.js'

/**
 * @param {String} string 
 */

let palindrom_checker = function (string) {
    let strStack = new stack ();
    let reverseStr = '';
    for (let i=0; i<string.length; i++) {
        strStack.push(string.charAt(i))
    }
    while (strStack.top > -1) {
        reverseStr += strStack.pop()
    }
    return reverseStr === string
}

console.log(palindrom_checker("Kook"))