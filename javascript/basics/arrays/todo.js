let todo = ['lunch', 'reading', 'exercise', 'yoga', 'brewing'];

let objectConverter = function(list) {
    let result = []
    for (count = 0; count < list.length; count++){
        let value = {job: list[count], done: false}
        result.push(value)
    }
    return result
}
todo = objectConverter(todo);
todo[3].done = true;

const getThingsToDo = function(list) {
    return list.filter(function (element) {
        return !element.done // element.done === false보다 직관적이므로 훨씬 가독성이 좋다.  
    })
}
console.log(todo)
console.log(getThingsToDo(todo))

// let deleteTodo = function(list, valuetodelete) {
//     let index = list.findIndex(function(element) {
//         return valuetodelete.toLowerCase() === element.job.toLowerCase()  
//     })
//     if (index > -1) // 만약 찾는 값이 todo 리스트 안에 확실히 있었을 경우. (찾지 못했다면 -1을 반환했을테니)
//     list.splice(index, 1);
// }

// console.log(todo);
// deleteTodo(todo,'lunch');
// console.log(todo);

// todo.splice(2,1);
// todo.push("drink coffee");
// todo.shift();

// console.log(todo);
// console.log(`you have ${todo.length-1} todos.`);
// console.log(`todo 1: ${todo[1]}`);

// todo.forEach(function (item, index){
//     const num = index + 1
//     console.log(`${num}.${item}`)
// })

// for (let count = 0; count < todo.length; count++){
//     console.log(`${count + 1}. ${todo[count]}`)
// }