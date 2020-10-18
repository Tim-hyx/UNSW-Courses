let loading = document.createElement('div');
loading.innerHTML = 'Loading, please wait';
loading.style.fontSize = '25px';
document.body.appendChild(loading);
let xhr = new XMLHttpRequest();
xhr.open('GET', 'http://www.cse.unsw.edu.au/~cs6080/20T3/data/package.json')
xhr.send()
xhr.onload = (e) => {
    setTimeout(() => {
        loading.style.display = 'none';
        let data = JSON.parse(xhr.responseText);
        localStorage.setItem('data', JSON.stringify(data));
        let flexbox = document.createElement('div');
        flexbox.style.height = '100px';
        flexbox.style.width = '300px';
        document.body.appendChild(flexbox);
        document.body.style.fontSize = '25px';
        let leftbox = document.createElement('div');
        leftbox.style.height = '100px';
        leftbox.style.width = '150px';
        flexbox.appendChild(leftbox);
        let rightbox = document.createElement('div');
        rightbox.style.height = '100px';
        rightbox.style.width = '150px';
        flexbox.appendChild(rightbox);
        flexbox.style.display = 'flex';
        for (let i = 0; i < 3; i++) {
            let div1 = document.createElement('div');
            let div2 = document.createElement('div');
            let left = document.createTextNode(Object.keys(data)[i]);
            let right = document.createTextNode(Object.values(data)[i]);
            div1.appendChild(left)
            leftbox.appendChild(div1)
            div2.appendChild(right)
            rightbox.appendChild(div2)
        }
    }, 1000)
}
xhr.onerror = ((e) => {
    loading.style.display = 'none';
    let data = JSON.parse(localStorage['data']);
    let flexbox = document.createElement('div')
    flexbox.style.height = '100px';
    flexbox.style.width = '300px';
    document.body.appendChild(flexbox);
    document.body.style.fontSize = '25px';
    let leftbox = document.createElement('div');
    leftbox.style.height = '100px';
    leftbox.style.width = '150px';
    flexbox.appendChild(leftbox);
    let rightbox = document.createElement('div');
    rightbox.style.height = '100px';
    rightbox.style.width = '150px';
    flexbox.appendChild(rightbox);
    flexbox.style.display = 'flex';
    for (let i = 0; i < 3; i++) {
        let div1 = document.createElement('div');
        let div2 = document.createElement('div');
        let left = document.createTextNode(Object.keys(data)[i]);
        let right = document.createTextNode(Object.values(data)[i]);
        div1.appendChild(left)
        leftbox.appendChild(div1)
        div2.appendChild(right)
        rightbox.appendChild(div2)
    }
    let not_live = document.createElement('div');
    not_live.innerHTML = 'This data is not live.';
    document.body.appendChild(not_live);
})

try {
    xhr.send();
} catch (e) {
    xhr.onerror;
}