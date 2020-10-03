import moment from "moment";

let today = moment();
let start_hour=today.hour();
let friday;
if (moment().weekday() >= 5) {
    let next_nine = moment().add(1, "week").day(5).set({hour: 9, minute: 0, second: 0});
    friday = moment.duration(next_nine.diff(moment())).asSeconds();
} else {
    let next_nine = moment().day(5).set({hour: 9, minute: 0, second: 0});
    friday = moment.duration(next_nine.diff(moment())).asSeconds();
}

console.log(`The day started ${start_hour} hours ago. One week ago it was ${today.clone().subtract(7, "days").format("dddd")} at ${today.clone().subtract(7, "days").format("hh:mm a")}. Today's date is ${today.format("DD/MM/YYYY")}. There are exactly ${Math.round(friday)} seconds until 9am on Friday.`);