function wait(ms) {
	return new Promise(resolve => setTimeout(resolve, ms));
}

function hack() {
    const output = document.getElementById("output")
    wait(300)
        .then(() => {
            output.innerText += 'h'
            return wait(300);
        })
        .then(() => {
            output.innerText += 'a'
            return wait(300);
        })
        .then(() => {
            output.innerText += 'c'
            return wait(300);
        })
        .then(() => {
            output.innerText += 'k'
            return wait(300);
        });
}

document.getElementById('hack').addEventListener('click', hack)