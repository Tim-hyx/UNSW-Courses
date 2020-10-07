document.addEventListener('DOMContentLoaded', () => {
    const myTimer = setInterval(addColours, 50);
    const gridDisplay = document.querySelector('.grid');
    const resultDisplay = document.getElementById('result');
    let squares = [];
    const width = 4;

    //create the playing board
    function createBoard() {
        for (let i = 0; i < width * width; i++) {
            let square = document.createElement('div');
            if (i === 0) square.innerHTML = 2;
            else square.innerHTML = 0;
            gridDisplay.appendChild(square);
            squares.push(square);
        }
    }

    createBoard()

    //generate a new number
    function generate() {
        let randomNumber = Math.floor(Math.random() * squares.length)
        let numbers = [2, 4]
        let randomGameNumber = Math.floor(Math.random() * numbers.length)
        if (squares[randomNumber].innerHTML == 0) {
            squares[randomNumber].innerHTML = numbers[randomGameNumber];
            checkForGameOver();
        } else generate()
    }

    function moveRight() {
        for (let i = 0; i < 16; i++) {
            if (i % 4 === 0) {
                let totalOne = squares[i].innerHTML;
                let totalTwo = squares[i + 1].innerHTML;
                let totalThree = squares[i + 2].innerHTML;
                let totalFour = squares[i + 3].innerHTML;
                let row = [parseInt(totalOne), parseInt(totalTwo), parseInt(totalThree), parseInt(totalFour)];
                let filteredRow = row.filter(num => num);
                let missing = 4 - filteredRow.length;
                let zeros = Array(missing).fill(0);
                let newRow = zeros.concat(filteredRow);
                squares[i].innerHTML = newRow[0];
                squares[i + 1].innerHTML = newRow[1];
                squares[i + 2].innerHTML = newRow[2];
                squares[i + 3].innerHTML = newRow[3];
            }
        }
    }

    function moveLeft() {
        for (let i = 0; i < 16; i++) {
            if (i % 4 === 0) {
                let totalOne = squares[i].innerHTML;
                let totalTwo = squares[i + 1].innerHTML;
                let totalThree = squares[i + 2].innerHTML;
                let totalFour = squares[i + 3].innerHTML;
                let row = [parseInt(totalOne), parseInt(totalTwo), parseInt(totalThree), parseInt(totalFour)];
                let filteredRow = row.filter(num => num);
                let missing = 4 - filteredRow.length;
                let zeros = Array(missing).fill(0);
                let newRow = filteredRow.concat(zeros);
                squares[i].innerHTML = newRow[0];
                squares[i + 1].innerHTML = newRow[1];
                squares[i + 2].innerHTML = newRow[2];
                squares[i + 3].innerHTML = newRow[3];
            }
        }
    }


    function moveUp() {
        for (let i = 0; i < 4; i++) {
            let totalOne = squares[i].innerHTML;
            let totalTwo = squares[i + width].innerHTML;
            let totalThree = squares[i + (width * 2)].innerHTML;
            let totalFour = squares[i + (width * 3)].innerHTML;
            let column = [parseInt(totalOne), parseInt(totalTwo), parseInt(totalThree), parseInt(totalFour)];
            let filteredColumn = column.filter(num => num);
            let missing = 4 - filteredColumn.length;
            let zeros = Array(missing).fill(0);
            let newColumn = filteredColumn.concat(zeros);
            squares[i].innerHTML = newColumn[0];
            squares[i + width].innerHTML = newColumn[1];
            squares[i + (width * 2)].innerHTML = newColumn[2];
            squares[i + (width * 3)].innerHTML = newColumn[3];
        }
    }

    function moveDown() {
        for (let i = 0; i < 4; i++) {
            let totalOne = squares[i].innerHTML;
            let totalTwo = squares[i + width].innerHTML;
            let totalThree = squares[i + (width * 2)].innerHTML;
            let totalFour = squares[i + (width * 3)].innerHTML;
            let column = [parseInt(totalOne), parseInt(totalTwo), parseInt(totalThree), parseInt(totalFour)];
            let filteredColumn = column.filter(num => num);
            let missing = 4 - filteredColumn.length;
            let zeros = Array(missing).fill(0);
            let newColumn = zeros.concat(filteredColumn);
            squares[i].innerHTML = newColumn[0];
            squares[i + width].innerHTML = newColumn[1];
            squares[i + (width * 2)].innerHTML = newColumn[2];
            squares[i + (width * 3)].innerHTML = newColumn[3];
        }
    }

    function combineRow() {
        for (let i = 0; i < 15; i++) {
            if (squares[i].innerHTML === squares[i + 1].innerHTML) {
                squares[i].innerHTML = parseInt(squares[i].innerHTML) + parseInt(squares[i + 1].innerHTML);
                squares[i + 1].innerHTML = 0;
            }
        }
        checkForWin()
    }

    function combineColumn() {
        for (let i = 0; i < 12; i++) {
            if (squares[i].innerHTML === squares[i + width].innerHTML) {
                squares[i].innerHTML = parseInt(squares[i].innerHTML) + parseInt(squares[i + width].innerHTML);
                squares[i + width].innerHTML = 0;
            }
        }
        checkForWin()
    }

    //assign functions to keyCodes
    function control(e) {
        if (e.keyCode === 37) {
            keyLeft()
        } else if (e.keyCode === 38) {
            keyUp()
        } else if (e.keyCode === 39) {
            keyRight()
        } else if (e.keyCode === 40) {
            keyDown()
        }
    }

    document.addEventListener('keyup', control)

    function keyRight() {
        moveRight()
        combineRow()
        moveRight()
        generate()
    }

    function keyLeft() {
        moveLeft()
        combineRow()
        moveLeft()
        generate()
    }

    function keyUp() {
        moveUp()
        combineColumn()
        moveUp()
        generate()
    }

    function keyDown() {
        moveDown()
        combineColumn()
        moveDown()
        generate()
    }

    //check for the number 2048 in the squares to win
    function checkForWin() {
        for (let i = 0; i < squares.length; i++) {
            if (squares[i].innerHTML == 2048) {
                resultDisplay.innerHTML = 'State : Win';
                document.removeEventListener('keyup', control);
                setTimeout(() => clear(), 3000);
            }
        }
    }

    //check if there are no zeros on the board to lose
    function checkForGameOver() {
        let zeros = 0;
        for (let i = 0; i < squares.length; i++) {
            if (squares[i].innerHTML == 0) {
                zeros++;
            }
        }
        let count = 0;
        if (zeros === 0) {
            for (let i = 0; i < 16; i++) {
                if (i === 0) {
                    if ((squares[i + 1].innerHTML !== squares[i].innerHTML) && (squares[i + 1].innerHTML !== squares[i].innerHTML)) {
                        count += 1;
                    }
                } else if (i === 3) {
                    if ((squares[i - 1].innerHTML !== squares[i].innerHTML) && (squares[i + 4].innerHTML !== squares[i].innerHTML)) {
                        count += 1;
                    }
                } else if (i === 12) {
                    if ((squares[i + 1].innerHTML !== squares[i].innerHTML) && (squares[i - 4].innerHTML !== squares[i].innerHTML)) {
                        count += 1;
                    }
                } else if (i === 15) {
                    if ((squares[i - 1].innerHTML !== squares[i].innerHTML) && (squares[i - 4].innerHTML !== squares[i].innerHTML)) {
                        count += 1;
                    }
                } else if ((i === 1) || (i === 2)) {
                    if ((squares[i - 1].innerHTML !== squares[i].innerHTML) && (squares[i + 1].innerHTML !== squares[i].innerHTML) && (squares[i + 4].innerHTML !== squares[i].innerHTML)) {
                        count += 1;
                    }
                } else if ((i === 13) || (i === 14)) {
                    if ((squares[i - 1].innerHTML !== squares[i].innerHTML) && (squares[i + 1].innerHTML !== squares[i].innerHTML) && (squares[i - 4].innerHTML !== squares[i].innerHTML)) {
                        count += 1;
                    }
                } else if ((i === 4) || (i === 8)) {
                    if ((squares[i + 4].innerHTML !== squares[i].innerHTML) && (squares[i + 1].innerHTML !== squares[i].innerHTML) && (squares[i - 4].innerHTML !== squares[i].innerHTML)) {
                        count += 1;
                    }
                } else if ((i === 7) || (i === 11)) {
                    if ((squares[i - 1].innerHTML !== squares[i].innerHTML) && (squares[i + 4].innerHTML !== squares[i].innerHTML) && (squares[i - 4].innerHTML !== squares[i].innerHTML)) {
                        count += 1;
                    }
                } else {
                    if ((squares[i - 1].innerHTML !== squares[i].innerHTML) && (squares[i + 4].innerHTML !== squares[i].innerHTML) && (squares[i - 4].innerHTML !== squares[i].innerHTML) && (squares[i + 1].innerHTML !== squares[i].innerHTML)) {
                        count += 1;
                    }
                }
            }
            if (count === 16) {
                resultDisplay.innerHTML = 'State : Lose';
                document.removeEventListener('keyup', control);
                setTimeout(() => clear(), 3000);
            }
        }
    }

    //clear timer
    function clear() {
        clearInterval(myTimer)
    }

    //add colours
    function addColours() {
        for (let i = 0; i < squares.length; i++) {
            if (squares[i].innerHTML == 0) squares[i].style.color = '#cdc1b4';
            else squares[i].style.color = '#776e65';
            if (squares[i].innerHTML == 0) squares[i].style.backgroundColor = '#cdc1b4';
            else if (squares[i].innerHTML == 2) squares[i].style.backgroundColor = '#eee4da';
            else if (squares[i].innerHTML == 4) squares[i].style.backgroundColor = '#ede0c8';
            else if (squares[i].innerHTML == 8) squares[i].style.backgroundColor = '#f2b179';
            else if (squares[i].innerHTML == 16) squares[i].style.backgroundColor = '#f59563';
            else if (squares[i].innerHTML == 32) squares[i].style.backgroundColor = '#e8c064';
            else if (squares[i].innerHTML == 64) squares[i].style.backgroundColor = '#f65e3b';
            else if (squares[i].innerHTML == 128) squares[i].style.backgroundColor = '#edcf72';
            else if (squares[i].innerHTML == 256) squares[i].style.backgroundColor = '#ead79c';
            else if (squares[i].innerHTML == 512) squares[i].style.backgroundColor = '#76daff';
            else if (squares[i].innerHTML == 1024) squares[i].style.backgroundColor = '#beeaa5';
            else if (squares[i].innerHTML == 2048) squares[i].style.backgroundColor = '#d7d4f0';
        }
    }

    addColours()
})