class Stack {
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

let testStack = new Stack();
for (let i=0; i<5; i++) {
    testStack.push(i)
}
console.log(testStack.peek());
console.log(testStack.dataStore);
console.log(testStack.pop());
console.log(testStack.dataStore);
