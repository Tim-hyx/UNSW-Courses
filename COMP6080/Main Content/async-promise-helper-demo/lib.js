
const outputDomNode = document.getElementById('output');

Library = {
  getJSON(path) {
    return fetch(path).then(response => response.json());
  },

  print(msg) {
    const text = document.createElement('h5');
    text.innerText = msg;
    outputDomNode.appendChild(text);
  },

  printLight(msg, top) {
    const text = document.createElement('p');
    text.className = 'lead';
    text.innerText = msg;

    /* is prepend standard? */
    if (top) {
      outputDomNode.prepend(text);
    } else {
      outputDomNode.appendChild(text);
    }
  },

  clearOutput() {
    document.getElementById('output').innerHTML = '';
  }
};
