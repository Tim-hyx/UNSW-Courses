function greetings1(name) {
	return `Hello ${name}`;
}

const greetings2 = function(name) {
	return `Hello ${name}`;
}

const greetings3 = (name) => {
	return `Hello ${name}`;
}

function printThings(var1, var2) {
	console.log(var1());
	console.log(var2());
}

printThings(greetings2, greetings3);
