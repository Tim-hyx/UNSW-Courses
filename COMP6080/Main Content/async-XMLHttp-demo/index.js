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

function getUserInfo(username) {
    // Get all posts for the user and use the renderResult function to display
    // each posts title and # of comments.
    // renderResult('fake post title', 0);
    // Valid users are listed here: https://jsonplaceholder.typicode.com/users
}