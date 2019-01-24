let randomNumber = Math.floor(Math.random() * 100) + 1;
const guesses = document.querySelector('.guesses');
const lastResult = document.querySelector('.lastResult');
const lowOrHi = document.querySelector('.lowOrHi');
const 술양Submit = document.querySelector('.술양Submit');
const guessField소주잔 = document.querySelector('.guessField소주잔');
const 소주도수 = 17
const 파우스트알콜양 = ((30 * 0.4) + (30 * 0.755) + (15 * 0.2))
// let guessCount = 1;
let resetButton;
function alcoholCal() {
  if (Number(guessField소주잔.value) >=0 && Number(guessfield소주병.value) >= 0){
    let 소주잔술양 = Number(guessField소주잔.value) * 50
    let 소주병술양 = Number(guessfiled소주병.value) * 360
    let 파우스트환산값 = ((소주잔술양 + 소주병술양) * 소주도수 * 0.01) / 파우스트알콜양
  }
  guesses결과.textContent = `계산 결과: 파우스트 약 ${파우스트환산값.toFixed(1)}잔을 드신 것과 같습니다.`;

  if (파우스트환산값 >= 4) {
    lastResult조언.textContent = '당신의 간, 괜찮으십니까?';
    lastResult.style.backgroundColor = 'red';
    lowOrHi.textContent = '';

  set계산완료();
  }
}
guessSubmit.addEventListener('click', alcoholCal);

function set계산완료() {
  guessField.disabled = true;
  guessSubmit.disabled = true;
  resetButton = document.createElement('button');
  resetButton.textContent = 'Start new game';
  document.body.appendChild(resetButton);
  resetButton.addEventListener('click', reset계산);
}
function reset계산() {
  guessCount = 1;
  const resetParas = document.querySelectorAll('.resultParas p');
  for(let i = 0 ; i < resetParas.length ; i++) {
    resetParas[i].textContent = '';
  }
  resetButton.parentNode.removeChild(resetButton);
  guessField.disabled = false;
  guessSubmit.disabled = false;
  guessField.value = '';
  guessField.focus();
  lastResult.style.backgroundColor = 'white';
  randomNumber = Math.floor(Math.random() * 100) + 1;
}