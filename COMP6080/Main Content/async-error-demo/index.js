import {GameState} from './game_state.js';

const gameState = new GameState();

document
  .getElementById('send-to-blue-button')
  .addEventListener('click', () => {
    gameState.moveBarToBlue();
  });
document
  .getElementById('send-to-orange-button')
  .addEventListener('click', () => {
    gameState.moveBarToOrange();
  });


function createBar() {
  const bar = document.createElement('div');
  bar.className = 'bar';
  return bar;
}

async function stackWorker(color) {
  const stack = document.querySelector(`.${color}`);
  while (true) {
    const bars = Array.from(stack.querySelectorAll('.bar'));
    let numBars = bars.length;

    while (numBars < gameState[color]) {
      stack.prepend(createBar())
      numBars++;
    }

    while (numBars > gameState[color]) {
      throw new Error('uhoh');
      bars.pop().remove();
      numBars--;
    }
    
    await gameState.nextUpdate();
  }
}

stackWorker('blue');
stackWorker('orange');