import moment from "moment";

let today = moment();
console.log(today.format("dddd"));
for (let i = 0; i < 13; i++) {
    console.log(today.subtract(1, "years").format("dddd"));
}