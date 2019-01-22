let todo = ['lunch', 'reading', 'exercise', 'yoga', 'brewing'];

todo.splice(2,1);
todo.push("drink coffee");
todo.shift();

console.log(todo);
console.log(`you have ${todo.length-1} todos.`);
console.log(`todo 1: ${todo[1]}`);

todo.forEach(function (item, index){
    const num = index + 1
    console.log(`${num}.${item}`)
})