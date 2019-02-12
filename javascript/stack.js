export class stack {
    constructor() {
        this.dataStore = [];
        this.top = -1;
    }
    push(element){
        this.top++;
        this.dataStore[this.top] = element;
    }
    pop() {
        let value = this.dataStore[this.top];
        this.dataStore.splice(this.top, 1)     // dataStore가 배열이기 때문에 splice말고는 다른 방법이 없는 걸까? 
        this.top--;
        return value
    }
    peek() {
        return this.dataStore[this.top]
    }
    length() {
        return this.top
    }
    clear() {
        this.dataStore = [];
        this.top = -1;
    }
}

/**
 * @param {String} string 
 */

