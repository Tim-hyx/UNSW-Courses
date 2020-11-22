let startTime = 0;
let counter = 0;

function tick() {
    const outputOne = document.getElementById('timer-output-1');
    const outputTwo = document.getElementById('timer-output-2');
    // This one assumes tick() is called once every second.
    outputOne.innerText = (++counter).toFixed(2);
    // This one does not and simply logs the time since we started.
    outputTwo.innerText = ((Date.now() - startTime)/1000).toFixed(2);
}

function start() {
    startTime = Date.now();
    setInterval(tick, 1000);
}

function factorial(n) {
  let result = n;
  while (n > 0) {
    result *= n--;
  }
  return result;
}

function heavy() {
	factorial(9999999999);
}

document.getElementById('start').addEventListener('click', start);
document.getElementById('heavy').addEventListener('click', heavy);