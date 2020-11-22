const results = document.querySelector('.results');
const topicField = document.getElementById('search-topic');
const newPostTopicField = document.getElementById('topic');
const newPostTextField = document.getElementById('text');

const dialog = document.getElementById('dialog');
const dialogMessage = document.getElementById('dialog-msg');
const searchButton = document.getElementById('search');
const submitButton = document.getElementById('submit');

function clearResults() {
	results.innerHTML = '';
}

function addToResults(result) {
	const p = document.createElement('p');
	p.className = 'lead result';
	p.innerText = result;
	results.appendChild(p);
}

/** Type can be either 'error' or 'success'. */
function showDialog(message, error) {
	dialog.style.display = 'block';
	if (error) {
		dialog.classList.add('alert-danger');
	} else {
		dialog.classList.add('alert-success');
	}
	dialogMessage.innerText = message;
}

function hideDialog() {
	dialog.style.display = 'none';
}

function getPosts(topic) {
	// Reset our state.
	clearResults();
	hideDialog();

	return fetch('/api/posts?topic='+topic)
		.then(r => {
			if (r.status === 200)
				return r.json()
			throw new Error(`Got status code ${r.status}`);
		})
		.then(posts => {
			if (posts.length === 0) {
				throw new Error('No results');
			}
			posts.map(addToResults);
		})
		.catch(err => showDialog(err.message, true));
}

function makePost(topic, postText) {
	// Reset our state.
	hideDialog();

	const options = {
		method: 'POST',
		headers: { 'Content-Type': 'application/json' },
		body: JSON.stringify({postText})
	};

	fetch('/api/posts?topic='+topic, options)
		.then(r => {
			if (r.status !== 200) {
				throw new Error(`Got status code ${r.status}`);
			}
			showDialog('Post Submitted', false);
		})
		.catch(err => showDialog(err.message, true));
}

searchButton.addEventListener('click', () => getPosts(topicField.value));
submitButton.addEventListener('click', () => {
	makePost(newPostTopicField.value, newPostTextField.value);
});
