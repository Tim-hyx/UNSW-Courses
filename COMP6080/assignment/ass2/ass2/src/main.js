import API from './api.js';
// A helper you may want to use when uploading new images to the server.
// import { fileToDataUrl } from './helpers.js';

// This url may need to change depending on what port your backend is running
// on.
// const api = 'http://127.0.0.1:5000';


// Example usage of makeAPIRequest method.
// api.makeAPIRequest('dummy/user')
//     .then(r => console.log(r));

// importing named exports we use brackets
import * as helper from './helpers.js';

const api = new API();

let bannerClass = document.querySelector('.banner');
bannerClass.style.alignItems = 'center';
bannerClass.style.justifyContent = 'center';
let mainRole = document.querySelector('main');
helper.addLogin(api, mainRole);
helper.addRegistration(api, mainRole);
