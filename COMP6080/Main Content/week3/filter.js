const numbers = [ 1, 2, 3, 4, 5, 6 ];

// All above 2
const newNumbers = numbers.filter(num => num > 2);
/*const newNumbers = [];
for (const number of numbers) {
	if (number > 2) {
		newNumbers.push(number);
	}
}*/
console.log(newNumbers);


// Double all the numbers
const newNumbers2 = numbers.map(num => num * 2);
console.log(newNumbers2);