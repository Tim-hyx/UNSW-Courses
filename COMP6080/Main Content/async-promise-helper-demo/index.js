const outputDomNode = document.getElementById("output");
const time = {};
const API_URL = "https://jsonplaceholder.typicode.com/comments";

/**
 * Returns a different set of 3 urls to fetch every time it's
 * called to prevent caching from effecting results.
 */
function getRequestUrls() {
  const ids = [
    Math.floor(Math.random() * 500),
    Math.floor(Math.random() * 500),
    Math.floor(Math.random() * 500),
  ];
  return ids.map((id) => `${API_URL}?id=${id}`);
}

/**
 * Returns a promise that resolves with a json object which was
 * fetched from path then decoded.
 */
function getJSON(path) {
  return fetch(path).then((response) => response.json());
}

/** Prints to output. */
function printToOutput(msg) {
  const text = document.createElement("h5");
  text.innerText = msg;
  outputDomNode.appendChild(text);
}

/** Prints to output with a lighter text color. */
function printLightToOutput(msg) {
  const text = document.createElement("p");
  text.className = "lead";
  text.innerText = msg;

  outputDomNode.appendChild(text);
}

function clearOutput() {
  outputDomNode.innerHTML = "";
}

function togetherGet() {
  clearOutput();
  time.start = Date.now();
  // Form a list of Promises where we are getting
  // serveral users.
  const listOfPromises = getRequestUrls().map(getJSON);
  // Run them all at the same time and once all are done, display them.
  Promise.all(listOfPromises)
    .then((results) => results.map((result) => printToOutput(result[0].email)))
    .then(finishRequestTiming);
}

function synchronousGet() {
  clearOutput();
  time.start = Date.now();

  // This is going to take longer as we're
  // going to process one request at a time.
  getRequestUrls()
    .reduce((requests, uri) => {
      return requests
        .then(() => getJSON(uri))
        .then((result) => printToOutput(result[0].email));
    }, Promise.resolve(null))
    .then(finishRequestTiming);
}

function finishRequestTiming() {
  // mark the end of the request.
  time.end = Date.now();
  const delta = time.end - time.start;
  printLightToOutput(`Took ${delta} ms`);
}

document.getElementById("all").addEventListener("click", togetherGet);
document.getElementById("notAll").addEventListener("click", synchronousGet);
