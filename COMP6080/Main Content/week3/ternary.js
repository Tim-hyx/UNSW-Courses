const a = 5;

/*let even = false;
if (a % 2 === 0) {
	even = true;
}*/

// A. Your condition is small
// B. The point of your "decision" is to assign a value
// const even = (a % 2 === 0 ? true : false);
const even = a % 2 === 0;

console.log('even', even);