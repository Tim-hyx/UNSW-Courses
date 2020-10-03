document.getElementsByName("firstname")[0].addEventListener("change", firstcheck);
document.getElementsByName("lastname")[0].addEventListener("change", lastcheck);
document.getElementsByName("dateofbirth")[0].addEventListener("change", datecheck);
document.getElementById("remove").addEventListener("click", delete_all);

let cities = [];
for (let i = 1; i <= 3; i++) {
    let city = document.getElementById("city" + i);
    city.addEventListener("change", (event) => {
        if (city.checked === true) {
            cities.push(city.value);
        } else {
            cities = cities.filter((e) => e !== city.value);
        }
    })
}

document.getElementsByName("area")[0].addEventListener("click", print);

function firstcheck() {
    let firstname = document.getElementsByName("firstname")[0].value;
    if ((firstname.length < 3) || (firstname.length > 50)) {
        document.getElementsByName("area")[0].innerHTML = "Please input a valid firstname";
    }
}

function lastcheck() {
    let lastname = document.getElementsByName("lastname")[0].value;
    if ((lastname.length < 3) || (lastname.length > 50)) {
        document.getElementsByName("area")[0].innerHTML = "Please input a valid lastname";
    }
}

function datecheck() {
    const re = new RegExp("^([0-9]{2})[./]{1}([0-9]{2})[./]{1}([0-9]{4})$");
    let date = document.getElementsByName("dateofbirth")[0].value;
    let strDataValue;
    let infoValidation = true;
    if ((strDataValue = re.exec(date)) != null) {
        let i;
        i = parseFloat(strDataValue[3]);
        if (i <= 0 || i > 9999) {
            infoValidation = false;
        }
        i = parseFloat(strDataValue[2]);
        if (i <= 0 || i > 12) {
            infoValidation = false;
        }
        i = parseFloat(strDataValue[1]);
        if (i <= 0 || i > 31) {
            infoValidation = false;
        }
    } else {
        infoValidation = false;
    }
    if (!infoValidation) {
        document.getElementsByName("area")[0].innerHTML = "Please input a valid date of birth";
    }
    return infoValidation;
}

function delete_all() {
    document.getElementsByName("firstname")[0].value = "";
    document.getElementsByName("lastname")[0].value = "";
    document.getElementsByName("dateofbirth")[0].value = "";
    let obj = document.getElementsByName("animal")[0];
    obj.options[0].selected = true;
    for (let i = 1; i <= 3; i++) {
        document.getElementById("city" + i).checked = false;
    }
    document.getElementsByName("area")[0].value = "";
}

function getage(birthday) {
    let age1 = Date.now() - birthday.getTime();
    let age2 = new Date(age1);
    return Math.abs(age2.getUTCFullYear() - 1970);
}

function print() {
    let firstname = document.getElementsByName("firstname")[0].value;
    let lastname = document.getElementsByName("lastname")[0].value;
    let date = document.getElementsByName("dateofbirth")[0].value;
    let age = getage(new Date(date));
    let animal = document.getElementsByName("animal")[0];
    let animal_text = animal.options[animal.selectedIndex].text;
    let ct;
    if (cities.length === 0) {
        ct = "no cities";
    } else {
        ct = cities.join();
    }
    document.getElementsByName("area")[0].innerHTML = `Hello ${firstname} ${lastname}, you are ${age} years old, your favourite animal is ${animal_text} and you've lived in ${ct}`;
}
