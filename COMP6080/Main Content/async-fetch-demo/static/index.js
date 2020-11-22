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

	// Get the posts from /api/posts?topic=<topic>.
	// Remember to handle errors. You can add a post
	// to the results div via addToResults and show
	// an error dialog with showDialog(errorMessage, true);
}

function makePost(topic, postText) {
	// Reset our state.
	hideDialog();

	// Create a new post by making a POST request to
	// /api/posts?topic=<topic>. Remember to handle errors
	// and show a success dialog when when finished.
	// You can show an success dialog with showDialog(message, false);
}


searchButton.addEventListener('click', () => getPosts(topicField.value));
submitButton.addEventListener('click', () => {
	makePost(newPostTopicField.value, newPostTextField.value);
});
