const result = [];
let str = "";
for (let j = 0; j < 30; j++) {
    const s = [];
    const hexDigits = "0123456789abcdef";
    for (let i = 0; i < 36; i++) {
        s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
    }
    s[14] = "4";  // bits 12-15 of the time_hi_and_version field to 0010
    s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1);  // bits 6-7 of the clock_seq_hi_and_reserved to 01
    s[8] = s[13] = s[18] = s[23] = "-";
    let string = "";
    for (let n = 0; n < 36; n++) {
        string += s[n];
        str += s[n];
    }
    result.push(string);
}
result.sort();
for (let n = 0; n < 30; n++) {
    console.log(result[n]);
}


const obj = {};
for (let i = 0; i < str.length; i++) {
    if (str[i] !== "-") {
        let key = str[i];//key stores every string
        if (obj[key]) {//check if there's value in it
            obj[key]++;
        } else {
            obj[key] = 1;//obj[w]=1
        }
    }
}
let items = Object.keys(obj).map(function (key) {
    return [key, obj[key]];
});

// Sort the array based on the second element
items.sort(function (first, second) {
    return second[1] - first[1];
});

// Create a new array with only the first 5 items
let first_five = "";
for (let i in items.slice(0, 5)) {
    first_five += items[i][0];
    first_five += " ";
}
console.log(first_five);
