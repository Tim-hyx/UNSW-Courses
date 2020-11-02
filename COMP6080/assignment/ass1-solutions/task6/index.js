const CITIES = ['sydney', 'melbourne', 'adelaide'];

const getAge = (dateString) => {
    if (dateString.match("[0-9]{2}/[0-9]{2}/[0-9]{4}")) {
        const values = dateString.split("/");
        const date = new Date(Date.parse(`${values[2]}-${values[1]}-${values[0]}`));

        if (!isNaN(date)) {
            const age = (new Date(Date.now() - date)).getUTCFullYear() - 1970;
            return age;
        }
    }
    return -1;
}

const getNewValue = () => {
    const form = document.getElementById('user-form');
    
    const firstName = form.elements['first-name'].value;
    if (!firstName || firstName.length < 3 || firstName.length > 50) {
        return "Please input a valid firstname";
    }

    const lastName = form.elements['last-name'].value;
    if (!lastName || lastName.length < 3 || lastName.length > 50) {
        return "Please input a valid lastname";
    }

    const age = getAge(form.elements['date-of-birth'].value);
    if (age < 0) {
        return "Please enter a valid date of birth";
    }

    const animal = form.elements['animal'].value;
    const cities = CITIES.filter(c => form.elements[c].checked).map(c => form.elements[c].value);

    return `Hello ${firstName} ${lastName}, ` +
                    `you are ${age} years old, your favourite animal is ${animal} ` +
                    `and you've lived in ${cities.length > 0 ? cities.join(', ') : 'no cities'}.`;
}

const handleChange = () => document.getElementById('data').value = getNewValue();

document.getElementById('removeButton').addEventListener('click', _ => {
    document.getElementById('user-form').reset();
    document.getElementById('data').textBox.value = '';
});