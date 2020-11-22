const API_URL = "https://jsonplaceholder.typicode.com";

document.querySelector('button').addEventListener('click', () => {
    for (const row of document.querySelectorAll('tr:not(:first-child)')) {
        row.remove();
    }
    getUserInfo(document.querySelector('input').value);
});

function createCol(text) {
    const col = document.createElement('td');
    col.innerText = text;
    return col;
}

function renderResult(postTitle, numComments) {
    const table = document.querySelector('table');
    const row = document.createElement('tr');
    row.appendChild(createCol(postTitle));
    row.appendChild(createCol(numComments));
    table.appendChild(row);
}

async function getUserInfo(username) {
    let r = await fetch(API_URL+'/users');
    const users = await r.json();
    const user = users.find(user => user.username === username);
    if (user === undefined) {
        alert('User not found :(');
    }

    r = await fetch(`${API_URL}/posts?userId=${user.id}`);
    const posts = await r.json();
    for (const post of posts) {
        r = await fetch(`${API_URL}/comments?postId=${post.id}`);
        const numComments = (await r.json()).length;
        renderResult(post.title, numComments);
    }
}