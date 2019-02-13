class queue {
    constructor() {
        this.dataStore = [];
    }
    enqueue(element) {
        this.dataStore.push(element);
    }
    dequeue(element) {
        this.dataStore.shift(element);
    }
    front() {
        return this.dataStore[0];
    }
    back() {
        return this.dataStore[this.dataStore.length - 1];
    }
    empty() {
        return this.dataStore===[];
    }
}

