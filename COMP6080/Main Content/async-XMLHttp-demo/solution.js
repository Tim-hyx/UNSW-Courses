const API_URL = "https://jsonplaceholder.typicode.com";

let pendingRequests = 0;

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

function getData(url, callback) {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", API_URL + url);
    xhr.responseType = 'json';
    xhr.onload = function () {
        if (xhr.status === 200) {
            callback(xhr.response);
        } else {
            alert('oh noe something went wrong!');
        }
    };
    xhr.send();
}

function processPost(post) {
    getData('/comments?postId='+post.id, (comments) => {
        renderResult(post.title, comments.length);
        pendingRequests--;
        if (pendingRequests === 0) {
            console.log("Done!");
        }
    });
}

function processPostsForUser(userId) {
    getData('/posts?userId='+userId, (posts) => {
        pendingRequests = posts.length;
        for (const post of posts) {
            processPost(post);
        }
    });
}

function getUserInfo(username) {
    console.log("Loading...");
    getData('/users', (users) => {
        const user = users.find(user => user.username === username);
        if (user === undefined) {
            alert('That username does not exist!');
        } else {
            processPostsForUser(user.id);
        }
    });
}