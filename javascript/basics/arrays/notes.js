const notes = [{
    title: 'My next trip',
    body: 'I;d like to go to Spain'
}, {
    title: 'Habbits to work on',
    body: 'Exercise. Eating a bit better.'
}, {
    title: 'Office modification',
    body: 'Get a new seat'
}]

const findNote = function (notes, noteTitle) {
    const index = notes.findIndex(function (note, index) {
        return note.title.toLowerCase() === noteTitle.toLowerCase()
    })
    return notes[index]
}

const note = findNote(notes, 'My next trip')
console.log(note)

// console.log(notes.pop())
// notes.push("my new note!")

// console.log(notes.shift())
// notes.unshift('my first note')

// notes.splice(1,0,"aye!")
// console.log(notes)

// notes.forEach(function (item, index) {
//     console.log(item)
// })

// for (let count = 0; count <= 2; count = count +1) {
//     console.log(count)
// }

// for (let count = notes.length - 1; count >= 0; count--) {
//     console.log(notes[count])
// }

// console.log(notes.indexOf('Note 1'))