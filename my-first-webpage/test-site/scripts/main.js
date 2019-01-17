document.querySelector('p').onclick = function() {
    alert('Ouch! Stop poking me!');
}

var myImage = document.querySelector('img');
myImage.onclick = function() {
    var mySrc = myImage.getAttribute('src');
    if (mySrc === 'images/thiscs.jpg') {
        myImage.setAttribute ('src', 'images/Glendronachcs.jpg');
    } else {
        myImage.setAttribute ('src', 'images/thiscs.jpg');
    }
}