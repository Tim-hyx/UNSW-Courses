/**
 * Given a js file object representing a jpg or png image, such as one taken
 * from a html file input element, return a promise which resolves to the file
 * data as a data url.
 * More info:
 *   https://developer.mozilla.org/en-US/docs/Web/API/File
 *   https://developer.mozilla.org/en-US/docs/Web/API/FileReader
 *   https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs
 *
 * Example Usage:
 *   const file = document.querySelector('input[type="file"]').files[0];
 *   console.log(fileToDataUrl(file));
 * @param {File} file The file to be read.
 * @return {Promise<string>} Promise which resolves to the file as a data url.
 */
// export function fileToDataUrl(file) {
//     const validFileTypes = [ 'image/jpeg', 'image/png', 'image/jpg' ]
//     const valid = validFileTypes.find(type => type === file.type);
//     // Bad data, let's walk away.
//     if (!valid) {
//         throw Error('provided file is not a png, jpg or jpeg image.');
//     }
//
//     const reader = new FileReader();
//     const dataUrlPromise = new Promise((resolve,reject) => {
//         reader.onerror = reject;
//         reader.onload = () => resolve(reader.result);
//     });
//     reader.readAsDataURL(file);
//     return dataUrlPromise;
// }


let USER_DATA;

//    Takes a list and returns the first null or empty string encountered, Otherwise returns true;
function isAnyStringEmpty(list) {
    for (let i = 0; i < list.length; i++) {
        if (list[i] === '' || list[i] == null) {
            return i;
        }
    }
    return false;
}


// Login

// Takes an element where login needs to be setup with div options
export function addLogin(api, parentElement) {
    let loginDiv = document.createElement('div');
    loginDiv.setAttribute('class', 'loginContainer');
    loginDiv.setAttribute('id', 'frontpageUnamePass');

    //Create input field for username and add it to loginDiv
    let uname = document.createElement('label');
    uname.setAttribute('for', 'loginUsername');
    let uname_label = document.createElement('b');
    let uname_text = document.createTextNode('Username');
    uname_label.appendChild(uname_text);
    uname.appendChild(uname_label);
    uname.style.color = '#1ec503';
    let unamePlaceHolderText = document.createElement('input');
    unamePlaceHolderText.setAttribute('class', 'login-field');
    unamePlaceHolderText.setAttribute('id', 'loginUsername');
    unamePlaceHolderText.setAttribute('type', 'text');
    unamePlaceHolderText.setAttribute('placeholder', 'Enter Username');
    unamePlaceHolderText.setAttribute('name', 'uname');
    unamePlaceHolderText.setAttribute('require', true);
    loginDiv.appendChild(uname);
    loginDiv.appendChild(unamePlaceHolderText);

    //Create input field for password and add it to loginDiv
    let upass = document.createElement('label');
    upass.setAttribute('for', 'loginPassword');
    let upass_label = document.createElement('b');
    let upass_text = document.createTextNode('Password');
    upass_label.appendChild(upass_text);
    upass.appendChild(upass_label);
    upass.style.color = '#1ec503';
    let upassPlaceHolderText = document.createElement('input');
    upassPlaceHolderText.setAttribute('class', 'login-field');
    upassPlaceHolderText.setAttribute('id', 'loginPassword');
    upassPlaceHolderText.setAttribute('type', 'password');
    upassPlaceHolderText.setAttribute('placeholder', 'Enter Password');
    upassPlaceHolderText.setAttribute('name', 'pswd');
    upassPlaceHolderText.setAttribute('require', true);
    loginDiv.appendChild(upass);
    loginDiv.appendChild(upassPlaceHolderText);

    //Registration button is created but in a hidden mode, to unhidden call addRegistration
    let regBtn = document.createElement('button');
    regBtn.setAttribute('id', 'registrationBtn');
    regBtn.setAttribute('type', 'submit');
    regBtn.style.display = 'none';
    regBtn.textContent = 'Register';
    loginDiv.appendChild(regBtn);

    //Login button
    let loginBtn = document.createElement('button');
    loginBtn.setAttribute('id', 'submitLoginBtn');
    loginBtn.setAttribute('type', 'submit');
    loginBtn.textContent = 'Login';
    loginDiv.appendChild(loginBtn);
    parentElement.appendChild(loginDiv);

    let submitbtn = document.getElementById('submitLoginBtn');
    let username = document.getElementsByName('uname');
    let password = document.getElementsByName('pswd');
    submitbtn.addEventListener('click', async function () {
        let uname = username[0].value;
        let pswd = password[0].value;

        if (uname == null || uname === '' || pswd == null || pswd === '') {
            if (document.getElementById('emptyLoginField') != null) {
                document.getElementById('emptyLoginField').remove();
            }
            let error = document.createElement('p');
            error.setAttribute('id', 'emptyLoginField');
            error.style.color = 'red';
            error.textContent = 'Username or Password Field Empty.';
            document.getElementById('loginPassword').after(error);
        } else {
            let creds = {
                username: username[0].value,
                password: password[0].value
            }
            let result = await checkCredentials(api, creds);
            if (result === true) {
                //removes the loginDiv
                if (document.getElementById('frontpageUnamePass')) {
                    document.getElementById('frontpageUnamePass').remove();
                }
                navigation(api, parentElement);
                await feed(api, parentElement);
            }
        }
    });
}

//  Takes a object with user input username and password checks with local users.json file
function checkCredentials(api, credential) {
    return api.postLogin({
        'username': credential.username,
        'password': credential.password
    })
        .then((resp) => {
            if (resp === 200) {
                return true;
            } else {
                if (document.getElementById('incorrectUnamePass') != null) {
                    document.getElementById('incorrectUnamePass').remove();
                }
                let error = document.createElement('p');
                error.setAttribute('id', 'incorrectUnamePass');
                error.style.color = 'red';
                error.textContent = 'Invalid Username/Password';
                document.getElementById('loginPassword').after(error);
                return false;
            }
        });
}

// Registration Form
async function registrationSubmitBtnClicked(api) {
    let slaveName = document.getElementsByName('slaveName')[0].value;
    let newUname = document.getElementsByName('newUname')[0].value;
    let uEmailAddress = document.getElementsByName('uEmailAddress')[0].value;
    let newPassword = document.getElementsByName('newPassword')[0].value;
    let confirmNewPassword = document.getElementsByName('confirmNewPassword')[0].value;

    if (isAnyStringEmpty([slaveName, newUname, uEmailAddress, newPassword, confirmNewPassword]) !== false) {
        if (document.getElementById('formFieldError') != null) {
            document.getElementById('formFieldError').remove();
        }
        let error = document.createElement('p');
        error.setAttribute('id', 'formFieldError');
        error.style.color = 'red';
        error.textContent = 'Incorrect Input.';
        document.getElementById('confirmNewUserPassword').after(error);
    } else {
        let retVal1 = newPassword === confirmNewPassword;
        let re = /^(([^<>()\[\]\\.,;:\s@']+(\.[^<>()\[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        let retVal2 = re.test(String(uEmailAddress).toLowerCase());
        if (retVal1 && retVal2) {
            let registrationObject = {
                'username': newUname,
                'password': confirmNewPassword,
                'email': uEmailAddress,
                'name': slaveName
            }
            let response = await api.postRegistration(registrationObject);
            if (response.status === 200) {
                document.getElementById('userDisplay').remove();
                if (document.getElementById('frontpageUnamePass')) {
                    document.getElementById('frontpageUnamePass').remove();
                }
                navigation(api, document.querySelector('main'));
                await feed(api, document.querySelector('main'));
            } else {
                if (document.getElementById('formFieldError') != null) {
                    document.getElementById('formFieldError').remove();
                }
                let error = document.createElement('p');
                error.setAttribute('id', 'formFieldError');
                error.style.color = 'red';
                error.textContent = 'Username not available.';
                document.getElementById('confirmNewUserPassword').after(error);
            }
        } else {
            if (!retVal1) {
                if (document.getElementById('formFieldError') != null) {
                    document.getElementById('formFieldError').remove();
                }
                let error = document.createElement('p');
                error.setAttribute('id', 'formFieldError');
                error.style.color = 'red';
                error.textContent = 'Passwords Do Not Match.';
                document.getElementById('confirmNewUserPassword').after(error);
            } else if (!retVal2) {
                if (document.getElementById('formFieldError') != null) {
                    document.getElementById('formFieldError').remove();
                }
                let error = document.createElement('p');
                error.setAttribute('id', 'formFieldError');
                error.style.color = 'red';
                error.textContent = 'Incorrect Email.';
                document.getElementById('confirmNewUserPassword').after(error);
            }
        }
    }
}

export function addRegistration(api, parentElement) {
    let regBtn = parentElement.querySelector('#registrationBtn');
    let submitBtn = parentElement.querySelector('#submitLoginBtn');
    //Checks for a loginDiv
    if (regBtn != null) {
        //Unhides registration button if loginDiv is found
        regBtn.style.display = 'inline';
        submitBtn.style.display = 'inline';
    } else {
        // creates a registration button  and returns it if loginDiv is not found
        return;
    }

    regBtn.addEventListener('click', function () {
        let regcontainer = document.createElement('div');
        regcontainer.setAttribute('class', 'regcontainer');
        let regPageHeader = document.createElement('h1');
        regPageHeader.setAttribute('id', 'registrationPage');
        regPageHeader.style.color = '#1ec503';
        regPageHeader.textContent = 'Register';
        document.getElementById('frontpageUnamePass').remove();
        let formDiv = document.createElement('div');
        formDiv.setAttribute('id', 'userDisplay');
        regcontainer.appendChild(regPageHeader);
        formDiv.appendChild(regcontainer);
        populateRegistrationForm(regcontainer);
        parentElement.appendChild(formDiv);
        let submitRegBtn = formDiv.querySelector('#submitRegBtn');
        submitRegBtn.addEventListener('click', registrationSubmitBtnClicked.bind(null, api));
    });
}

// creates fields to take in new user information and submit form button is created
function populateRegistrationForm(formDiv) {
    //Official Name
    let slaveName = document.createElement('label');
    slaveName.setAttribute('for', 'officalName');
    let slaveName_label = document.createElement('b');
    let slaveName_text = document.createTextNode('Official Name');
    slaveName_label.appendChild(slaveName_text);
    slaveName.appendChild(slaveName_label);
    slaveName.style.color = '#1ec503';
    let slaveNamePlaceHolderText = document.createElement('input');
    slaveNamePlaceHolderText.setAttribute('class', 'registration-field');
    slaveNamePlaceHolderText.setAttribute('id', 'officialName');
    slaveNamePlaceHolderText.setAttribute('type', 'text');
    slaveNamePlaceHolderText.setAttribute('placeholder', 'Your slave name');
    slaveNamePlaceHolderText.setAttribute('name', 'slaveName');
    slaveNamePlaceHolderText.setAttribute('require', true);
    formDiv.appendChild(slaveName);
    formDiv.appendChild(slaveNamePlaceHolderText);

    //Username
    let uname = document.createElement('label');
    uname.setAttribute('for', 'newUsername');
    let uname_label = document.createElement('b');
    let uname_text = document.createTextNode('Username');
    uname_label.appendChild(uname_text);
    uname.appendChild(uname_label);
    uname.style.color = '#1ec503';
    let unamePlaceHolderText = document.createElement('input');
    unamePlaceHolderText.setAttribute('class', 'registration-field');
    unamePlaceHolderText.setAttribute('id', 'newUsername');
    unamePlaceHolderText.setAttribute('type', 'text');
    unamePlaceHolderText.setAttribute('placeholder', 'Your username name');
    unamePlaceHolderText.setAttribute('name', 'newUname');
    unamePlaceHolderText.setAttribute('require', true);
    formDiv.appendChild(uname);
    formDiv.appendChild(unamePlaceHolderText);

    //email
    let email = document.createElement('label');
    email.setAttribute('for', 'userEmail');
    let email_label = document.createElement('b');
    let email_text = document.createTextNode('Email');
    email_label.appendChild(email_text);
    email.appendChild(email_label);
    email.style.color = '#1ec503';
    let emailPlaceHolderText = document.createElement('input');
    emailPlaceHolderText.setAttribute('class', 'registration-field');
    emailPlaceHolderText.setAttribute('id', 'userEmail');
    emailPlaceHolderText.setAttribute('type', 'email');
    emailPlaceHolderText.setAttribute('placeholder', 'Your email');
    emailPlaceHolderText.setAttribute('name', 'uEmailAddress');
    emailPlaceHolderText.setAttribute('require', true);
    formDiv.appendChild(email);
    formDiv.appendChild(emailPlaceHolderText);

    //New Password
    let pswd = document.createElement('label');
    pswd.setAttribute('for', 'newUserPassword');
    let pswd_label = document.createElement('b');
    let pswd_text = document.createTextNode('New Password');
    pswd_label.appendChild(pswd_text);
    pswd.appendChild(pswd_label);
    pswd.style.color = '#1ec503';
    let pswdPlaceHolderText = document.createElement('input');
    pswdPlaceHolderText.setAttribute('class', 'registration-field');
    pswdPlaceHolderText.setAttribute('id', 'newUserPassword');
    pswdPlaceHolderText.setAttribute('type', 'password');
    pswdPlaceHolderText.setAttribute('placeholder', 'Your password');
    pswdPlaceHolderText.setAttribute('name', 'newPassword');
    pswdPlaceHolderText.setAttribute('require', true);
    formDiv.appendChild(pswd);
    formDiv.appendChild(pswdPlaceHolderText);

    //Confirm New Password
    let confirmPswd = document.createElement('label');
    confirmPswd.setAttribute('for', 'confirmNewUserPassword');
    let confirmPswd_label = document.createElement('b');
    let confirmPswd_text = document.createTextNode('Confirm New Password');
    confirmPswd_label.appendChild(confirmPswd_text);
    confirmPswd.appendChild(confirmPswd_label);
    confirmPswd.style.color = '#1ec503';
    let confirmPswdPlaceHolderText = document.createElement('input');
    confirmPswdPlaceHolderText.setAttribute('class', 'registration-field');
    confirmPswdPlaceHolderText.setAttribute('id', 'confirmNewUserPassword');
    confirmPswdPlaceHolderText.setAttribute('type', 'password');
    confirmPswdPlaceHolderText.setAttribute('placeholder', 'Confirm your password');
    confirmPswdPlaceHolderText.setAttribute('name', 'confirmNewPassword');
    confirmPswdPlaceHolderText.setAttribute('require', true);
    formDiv.appendChild(confirmPswd);
    formDiv.appendChild(confirmPswdPlaceHolderText);

    // XXX implement realtime username check
    let submitRegBtn = document.createElement('button');
    submitRegBtn.setAttribute('id', 'submitRegBtn');
    submitRegBtn.setAttribute('type', 'submit');
    submitRegBtn.textContent = 'Submit';
    formDiv.appendChild(submitRegBtn);
}

// Navigation

// Takes apiObject and main Div as arguments
// creates the navigation bar and starts events listeners on each options
function navigation(api, parentElement) {
    let div = document.createElement('div');
    div.setAttribute('class', 'navigation-bar');
    let myFeedEle = document.createElement('a');
    myFeedEle.textContent = '->My Feed<-';
    myFeedEle.setAttribute('id', 'myFeedNav');
    myFeedEle.setAttribute('class', 'navigation-elements');
    div.appendChild(myFeedEle);
    let newPostEle = document.createElement('a');
    newPostEle.textContent = 'New Post';
    newPostEle.setAttribute('id', 'newPostNav');
    newPostEle.setAttribute('class', 'navigation-elements');
    div.appendChild(newPostEle);
    let myProfileEle = document.createElement('a');
    myProfileEle.textContent = 'My Profile';
    myProfileEle.setAttribute('id', 'myProfileNav');
    myProfileEle.setAttribute('class', 'navigation-elements');
    div.appendChild(myProfileEle);
    let followEle = document.createElement('a');
    followEle.textContent = 'Follow';
    followEle.setAttribute('id', 'followNav');
    followEle.setAttribute('class', 'navigation-elements');
    div.appendChild(followEle);
    parentElement.appendChild(div);
    let main = document.querySelector('main');
    myFeedEle.addEventListener('click', function (event) {
        updateNavigationBar(1);
        feed(api, main);
    });
    newPostEle.addEventListener('click', function (event) {
        updateNavigationBar(2);
        newPost(api, main);
    });
    myProfileEle.addEventListener('click', async function (event) {
        updateNavigationBar(3);
        await showProfile(api, main);
        editDelete(api, main);
        await following(api);
    });
    followEle.addEventListener('click', function (event) {
        updateNavigationBar(4);
        follow(api, main);
    });
}

//	Takes a newElement number(1,2,3,4) and updates the corresponding nav element as active and deactivates the others
function updateNavigationBar(navElement) {
    let myFeed = 'My Feed';
    let newPost = 'New Post';
    let myProfile = 'My Profile';
    let follow = 'Follow';
    let myFeedNav = document.getElementById('myFeedNav');
    let newPostNav = document.getElementById('newPostNav');
    let myProfileNav = document.getElementById('myProfileNav');
    let followNav = document.getElementById('followNav');
    document.getElementById('userDisplay').remove();
    if (navElement === 1) {
        myFeedNav.textContent = '->' + myFeed + '<-';
    } else {
        myFeedNav.textContent = myFeed;
    }
    if (navElement === 2) {
        newPostNav.textContent = '->' + newPost + '<-';
    } else {
        newPostNav.textContent = newPost;
    }
    if (navElement === 3) {
        myProfileNav.textContent = '->' + myProfile + '<-';
    } else {
        myProfileNav.textContent = myProfile;
    }
    if (navElement === 4) {
        followNav.textContent = '->' + follow + '<-';
    } else {
        followNav.textContent = follow;
    }
}


// Feed Interface
async function feed(api, main) {
    let response = await api.getUserData();
    USER_DATA = await response.json();
    let userDisplay = document.createElement('div');
    userDisplay.setAttribute('id', 'userDisplay');
    main.appendChild(userDisplay);
    // implement pagination, infinite scroll
    let p = 0;
    let n = 100;
    let userData = await api.getFeed(p, n);
    renderUserFeed(userData.posts, userDisplay);
    iteractive(api);
    // other users profiles
    let userNames = document.getElementsByClassName('post-title');

    function getUserProfile(event) {
        let username = event.target.innerHTML;
        let myProfileNav = document.getElementById('myProfileNav');
        myProfileNav.textContent = '->' + 'Profile' + '<-';
        document.getElementById('userDisplay').remove();
        showProfile(api, main, null, username);
    }

    for (let i = 0; i < userNames.length; i++) {
        userNames[i].addEventListener('click', getUserProfile, false);
    }

}

//populates mainDiv with the post objects from userData Array
function renderUserFeed(userPosts, mainDiv) {
    userPosts.sort(function (a, b) {
        return b.meta.published - a.meta.published;
    });
    for (let i = 0; i < userPosts.length; i++) {
        let section = document.createElement('section');
        section.setAttribute('id', userPosts[i].id + '-post');
        section.setAttribute('class', 'post');
        let h2 = document.createElement('h2');
        h2.textContent = userPosts[i].meta.author;
        h2.setAttribute('id', userPosts[i].id + '-post-title');
        h2.setAttribute('class', 'post-title');
        section.appendChild(h2);
        let date = new Date(userPosts[i].meta.published * 1000);
        let dateStr = date.toString();
        let datestr = document.createElement('p');
        datestr.textContent = dateStr.substring(0, 24);
        datestr.setAttribute('id', userPosts[i].id + '-post-published');
        datestr.setAttribute('class', 'post-published');
        section.appendChild(datestr);
        let img = document.createElement('img');
        img.setAttribute('id', userPosts[i].id + '-post-image');
        img.setAttribute('src', 'data:image/png;base64,' + userPosts[i].src);
        img.setAttribute('alt', userPosts[i].meta.description_text);
        img.setAttribute('class', 'post-image');
        section.appendChild(img);
        let post_description = document.createElement('p');
        post_description.textContent = userPosts[i].meta.description_text;
        post_description.setAttribute('id', userPosts[i].id + '-post-description_text');
        post_description.setAttribute('class', 'post-description_text');
        section.appendChild(post_description)
        let like = document.createElement('span');
        like.textContent = '❤ ' + userPosts[i].meta.likes.length;
        like.setAttribute('id', userPosts[i].id + '-post-like');
        like.setAttribute('class', 'post-likes');
        section.appendChild(like)
        let comment = document.createElement('span');
        comment.textContent = '💬 ' + userPosts[i].comments.length;
        comment.setAttribute('id', userPosts[i].id + '-post-comment-count');
        comment.setAttribute('class', 'post-comments-count');
        section.appendChild(comment)
        if (userPosts[i].comments.length > 0) {
            let show_comment = document.createElement('span');
            show_comment.textContent = '+';
            show_comment.setAttribute('id', userPosts[i].id + '-post-show-comment');
            show_comment.setAttribute('class', 'post-show-comments');
            section.appendChild(show_comment)
        } else {
            let show_comments = document.createElement('span');
            show_comments.textContent = '+';
            show_comments.setAttribute('id', userPosts[i].id + '-post-show-comment');
            show_comments.setAttribute('class', 'post-show-comments');
            show_comments.style.display = 'none';
            section.appendChild(show_comments);
        }
        let hide = document.createElement('span');
        hide.textContent = '-';
        hide.setAttribute('id', userPosts[i].id + '-post-hide-comment');
        hide.setAttribute('class', 'post-hide-comments');
        hide.style.display = 'none';
        section.appendChild(hide);
        mainDiv.appendChild(section);
    }
}

function iteractive(api) {
    // like posts
    let postLikes = document.getElementsByClassName('post-likes');
    let likeClick = async function () {
        let likeId = this.getAttribute('id');
        let postId = likeId.match(/^(\d+).+/)[1];
        let postData = await api.getPost(postId);
        let promiseResponse = 0;
        if (postData.meta.likes.includes(USER_DATA.id) === true) {
            promiseResponse = api.putUnLike(postId);
        } else {
            promiseResponse = api.putLike(postId);
        }
        let statusNb = await promiseResponse;
        if (statusNb === 200) {
            let newPostData = await api.getPost(postId);
            let likeElement = document.getElementById(likeId);
            likeElement.textContent = '❤' + newPostData.meta.likes.length;
        }
    };
    for (let i = 0; i < postLikes.length; i++) {
        postLikes[i].addEventListener('click', likeClick, false);
    }
    commentPost(api);
    // show comments
    let showComments = document.getElementsByClassName('post-show-comments');
    for (let i = 0; i < showComments.length; i++) {
        showComments[i].addEventListener('click', function (event) {
            event.preventDefault();
            updateComments(api, event.target.id, 3);
        });
    }
}

function commentPost(api) {
    let showComments = document.getElementsByClassName('post-show-comments');
    for (let i = 0; i < showComments.length; i++) {
        let eleId = showComments[i].getAttribute('id');
        let postId = eleId.match(/^(\d+).+/)[1];
        let commentInput = document.createElement('label');
        commentInput.setAttribute('for', postId + '-comment-box');
        let slaveNamePlaceHolderText = document.createElement('input');
        slaveNamePlaceHolderText.setAttribute('id', postId + '-comment-box');
        slaveNamePlaceHolderText.setAttribute('class', 'comment-box');
        slaveNamePlaceHolderText.setAttribute('type', 'text');
        slaveNamePlaceHolderText.setAttribute('placeholder', 'comments here');
        slaveNamePlaceHolderText.setAttribute('name', postId + '-commentBox');
        commentInput.appendChild(slaveNamePlaceHolderText);
        showComments[i].after(commentInput)
    }
    let postNewComment = async function (attribute) {
        let postId = attribute.match(/^(\d+).+/)[1];
        let input = document.getElementsByName(postId + '-commentBox')[0].value;
        // If comment box is empty, returns/
        if (isAnyStringEmpty([input]) !== false) {
            return;
        }
        let commentObject = {
            'author': USER_DATA.username,
            'published': Math.round((new Date()).getTime() / 1000),
            'comment': input
        }
        let promiseResponse = api.putComment(postId, commentObject);
        let statusNb = await promiseResponse;
        if (statusNb === 200) {
            document.getElementById(attribute).value = '';
            updateComments(api, attribute, 0);
        }
    };
    let postComments = document.getElementsByClassName('comment-box');
    for (let i = 0; i < postComments.length; i++) {
        postComments[i].addEventListener('keyup', function (event) {
            event.preventDefault();
            if (event.keyCode === 13) {
                postNewComment(event.target.id);
            }
        })
    }
}

async function updateComments(api, showCommentId, diff) {
    let postId = showCommentId.match(/^(\d+).+/)[1];
    let postData = await api.getPost(postId);
    let postCommentCount = document.getElementById(postId + '-post-comment-count');
    let postshowComment = document.getElementById(postId + '-post-show-comment');
    postshowComment.style.display = 'inline';
    postCommentCount.textContent = '💬 ' + postData.comments.length;
    let section = document.getElementById(postId + '-post');
    postData.comments.sort(function (a, b) {
        return b.published - a.published;
    });
    let postComment = section.getElementsByClassName('post-comment');
    let removeId = Array();
    let showNbComments = Math.min(postData.comments.length, Math.max(postComment.length + diff, 1));
    for (let i = 0; i < postComment.length; i++) {
        removeId.push(postComment[i].getAttribute('id'));
    }
    for (let j = 0; j < removeId.length; j++) {
        document.getElementById(removeId[j]).remove();
    }
    let showCommentBtn = document.getElementById(postId + '-post-show-comment')
    for (let k = 0; k < showNbComments; k++) {
        let post_comment = document.createElement('p');
        post_comment.textContent = postData.comments[k].author + ': ' + postData.comments[k].comment;
        post_comment.setAttribute('id', postId + '-post-comment-' + k);
        post_comment.setAttribute('class', 'post-comment');
        showCommentBtn.after(post_comment);
    }
}

//follow

function follow(api, mainRole) {
    let followDiv = document.createElement('div');
    followDiv.setAttribute('id', 'userDisplay');
    let centerDiv = document.createElement('div');
    centerDiv.setAttribute('id', 'centerDisplayFollowDiv');
    centerDiv.setAttribute('class', 'center-div');
    //Search username
    let followUser = document.createElement('label');
    followUser.setAttribute('for', 'followUsername');
    let followUser_label = document.createElement('b');
    let followUser_text = document.createTextNode('Follow User');
    followUser_label.appendChild(followUser_text);
    followUser.appendChild(followUser_label);
    followUser.style.color = '#1ec503';
    let placeHolderText = document.createElement('input');
    placeHolderText.setAttribute('class', 'followUserInput');
    placeHolderText.setAttribute('id', 'followUsername');
    placeHolderText.setAttribute('type', 'text');
    placeHolderText.setAttribute('placeholder', 'Username');
    placeHolderText.setAttribute('name', 'followName');
    placeHolderText.setAttribute('require', true);
    centerDiv.appendChild(followUser);
    centerDiv.appendChild(placeHolderText)

    let searchBtn = document.createElement('p');
    searchBtn.textContent = 'Search';
    searchBtn.setAttribute('id', 'searchUsernameBtn');
    searchBtn.setAttribute('class', 'search-Username-Btn');
    centerDiv.appendChild(searchBtn);
    followDiv.appendChild(centerDiv);
    mainRole.appendChild(followDiv);

    searchBtn.addEventListener('click', async function (event) {
        if (document.getElementById('followError') != null) {
            document.getElementById('followError').remove();
        }
        let followConfirmationBtn = document.getElementsByClassName('followConfirmation-Btn');
        for (let i = 0; i < followConfirmationBtn.length; i++) {
            document.getElementById(followConfirmationBtn[i].getAttribute('id')).remove();
        }
        let userName = document.getElementsByName('followName')[0].value;
        if (isAnyStringEmpty([userName]) !== false) {
            if (document.getElementById('followError') != null) {
                document.getElementById('followError').remove();
            }
            let error = document.createElement('p');
            error.setAttribute('id', 'followError');
            error.style.color = 'red';
            error.textContent = 'Please enter a username.';
            placeHolderText.after(error);
        } else if (userName !== USER_DATA.username) {
            let srchResponse = await api.getUserData(null, userName);
            if (srchResponse.status === 200) {
                let response = await api.getUserData();
                USER_DATA = await response.json();
                let srchData = await srchResponse.json();
                //IF user is already following the username give an option to Unfollow, else give an option to follow
                if (USER_DATA.following.includes(srchData.id) === true) {
                    let confirmUnfollow = document.createElement('p');
                    confirmUnfollow.textContent = 'Unfollow ' + userName;
                    confirmUnfollow.setAttribute('id', 'unfollowConfirmation');
                    confirmUnfollow.setAttribute('class', 'followConfirmation-Btn');
                    centerDiv.appendChild(confirmUnfollow);
                    confirmUnfollow.addEventListener('click', async function (event) {
                        let response = await api.putUnfollowUser(userName);
                        if (response === 200) {
                            document.getElementById('unfollowConfirmation').innerHTML = 'Unfollowed ' + userName;
                        }
                    });
                } else {
                    let confirmfollow = document.createElement('p');
                    confirmfollow.textContent = 'Follow ' + userName;
                    confirmfollow.setAttribute('id', 'followConfirmation');
                    confirmfollow.setAttribute('class', 'followConfirmation-Btn');
                    centerDiv.appendChild(confirmfollow);
                    confirmfollow.addEventListener('click', async function (event) {
                        let response = await api.putFollowUser(userName);
                        if (response === 200) {
                            document.getElementById('followConfirmation').innerHTML = 'Following ' + userName;
                        }
                    });
                }
            } else {
                if (document.getElementById('followError') != null) {
                    document.getElementById('followError').remove();
                }
                let error = document.createElement('p');
                error.setAttribute('id', 'followError');
                error.style.color = 'red';
                error.textContent = 'User Doesn\'t Exist';
                placeHolderText.after(error);
            }
        } else {
            if (document.getElementById('followError') != null) {
                document.getElementById('followError').remove();
            }
            let error = document.createElement('p');
            error.setAttribute('id', 'followError');
            error.style.color = 'red';
            error.textContent = 'Cannot Follow Yourself.';
            placeHolderText.after(error);
        }
    });
}

function newPost(api, mainRole) {
    let newPostDiv = document.createElement('div');
    newPostDiv.setAttribute('id', 'userDisplay');
    newPostDiv.setAttribute('class', 'uploadNewPost');
    let centerDiv = document.createElement('div');
    centerDiv.setAttribute('id', 'centerDivNewPost');
    centerDiv.setAttribute('class', 'center-div');
    let postDesc = document.createElement('label');
    postDesc.textContent = 'Description';
    postDesc.setAttribute('for', 'postDescription');
    postDesc.style.fontWeight = 'bold';
    let descriptionElement = document.createElement('input');
    descriptionElement.setAttribute('class', 'description-field');
    descriptionElement.setAttribute('id', 'postDescription');
    descriptionElement.setAttribute('type', 'text');
    descriptionElement.setAttribute('placeholder', 'Add your description here');
    descriptionElement.setAttribute('name', 'description');
    descriptionElement.setAttribute('require', true);
    centerDiv.appendChild(postDesc);
    centerDiv.appendChild(descriptionElement);

    let upImage = document.createElement('input');
    upImage.setAttribute('class', 'upload-file');
    upImage.setAttribute('id', 'uploadPost');
    upImage.setAttribute('type', 'file');
    upImage.setAttribute('name', 'uploadImageFile');
    upImage.setAttribute('require', true);

    let submitBtn = document.createElement('p');
    submitBtn.textContent = 'submit';
    submitBtn.setAttribute('id', 'submitNewPostBtn');
    submitBtn.setAttribute('class', 'submit-Btn');
    centerDiv.appendChild(upImage);
    centerDiv.appendChild(submitBtn);
    newPostDiv.appendChild(centerDiv);
    mainRole.appendChild(newPostDiv);

    let img = document.createElement('img');
    img.setAttribute('id', 'post-image');
    img.setAttribute('src', '#');
    img.setAttribute('class', 'post-image');
    img.style.display = 'none';
    centerDiv.appendChild(img);

    let post_description = document.createElement('p');
    post_description.setAttribute('id', 'post-description');
    post_description.setAttribute('class', 'post-text-box');
    post_description.style.display = 'none';
    centerDiv.appendChild(post_description);

    let confirm_post = document.createElement('p');
    confirm_post.textContent = 'POST';
    confirm_post.setAttribute('id', 'confirm-post-submission');
    confirm_post.setAttribute('class', 'confirm-post');
    confirm_post.style.display = 'none';
    centerDiv.appendChild(confirm_post);

    submitBtn.addEventListener('click', function () {

        let imgElement = document.getElementById('post-image');
        let descElement = document.getElementById('post-description');
        let postBtn = document.getElementById('confirm-post-submission');

        let post_desc = document.getElementsByName('description')[0].value;
        let imageRaw = document.getElementsByName('uploadImageFile')[0].files;

        postBtn.style.display = 'none';
        descElement.style.display = 'none';
        imgElement.style.display = 'none';

        if (postBtn.removeEventListener) {
            postBtn.removeEventListener('click', newPostUploadBtnClicked);
        }

        if (imageRaw && imageRaw[0] && isAnyStringEmpty([post_desc]) === false) {
            let errorNewPost = document.getElementById('errorNewPost');

            if (errorNewPost) {
                document.getElementById('errorNewPost').remove();
            }

            const reader = new FileReader();

            reader.addEventListener('load', function () {
                let base64Img = reader.result;
                let pngRE = /data:image\/png;base64,(.+)/;
                let base64Encoding = pngRE.exec(base64Img);
                if (base64Encoding === null) {
                    if (document.getElementById('errorNewPost') != null) {
                        document.getElementById('errorNewPost').remove();
                    }
                    let error = document.createElement('p');
                    error.setAttribute('id', 'errorNewPost');
                    error.style.color = 'red';
                    error.textContent = 'Incorrect Image format.';
                    upImage.after(error);
                } else {
                    descElement.style.display = 'block';
                    descElement.textContent = post_desc;
                    let img = document.querySelector('img');  // $('img')[0]
                    img.style.display = 'block';
                    img.src = URL.createObjectURL(imageRaw[0]);
                    let displayPostBtn = document.getElementById('confirm-post-submission');
                    displayPostBtn.style.display = 'block';
                    let object = {
                        'api': api,
                        'postObject': {
                            'description_text': post_desc,
                            'src': base64Encoding[1]
                        }
                    };
                    displayPostBtn.addEventListener('click', newPostUploadBtnClicked.bind(null, object));
                }

            }, false);

            reader.readAsDataURL(imageRaw[0]);
        } else {
            if (document.getElementById('errorNewPost') != null) {
                document.getElementById('errorNewPost').remove();
            }
            let error = document.createElement('p');
            error.setAttribute('id', 'errorNewPost');
            error.style.color = 'red';
            error.textContent = 'Please add Description and Image.';
            upImage.after(error);
        }
    });
}

async function newPostUploadBtnClicked(object) {
    let displayPostBtn = document.getElementById('confirm-post-submission');
    let errorNewPost = document.getElementById('errorNewPost');
    if (errorNewPost) {
        document.getElementById('errorNewPost').remove();
    }
    let resp = await object.api.postPost(object.postObject);
    if (resp.status === 200) {
        alert('Post Uploaded');
        document.getElementById('userDisplay').remove();
        newPost(object.api, document.querySelector('main'));
    } else {
        if (document.getElementById('errorNewPost') != null) {
            document.getElementById('errorNewPost').remove();
        }
        let error = document.createElement('p');
        error.setAttribute('id', 'errorNewPost');
        error.style.color = 'red';
        error.textContent = 'Image Could Not Be processed. Try Again.';
        displayPostBtn.after(error);
    }
}

// Show Profile

function showProfile(api, mainRole, id = null, username = null) {
    return new Promise(async (resolve) => {
        let newPostDiv = document.createElement('div');
        newPostDiv.setAttribute('id', 'userDisplay');
        newPostDiv.setAttribute('class', 'showProfile');
        let userProfile = document.createElement('div');
        userProfile.setAttribute('id', 'userProfileDisplay');
        userProfile.setAttribute('class', 'user-Profile-Display');
        let userPostFeed = document.createElement('div');
        userPostFeed.setAttribute('id', 'userPostFeedDisplay');
        userPostFeed.setAttribute('class', 'user-Post-Feed-Display');

        newPostDiv.appendChild(userProfile);
        newPostDiv.appendChild(userPostFeed);
        mainRole.appendChild(newPostDiv);

        let response = await api.getUserData(id, username);
        let userData = await response.json();
        //Show user's own posts
        let likeCommentsCount = {
            'likes': 0,
            'comments': 0
        };
        let promiseArray = [];
        for (let i = 0; i < userData.posts.length; i++) {
            promiseArray.push(api.getPost(userData.posts[i]));
        }
        Promise.all(promiseArray).then(function (values) {
            renderUserFeed(values, userPostFeed);
            iteractive(api);

            likeCommentsCount.likes = 0;
            likeCommentsCount.comments = 0;
            for (let i = 0; i < values.length; i++) {
                likeCommentsCount.likes += values[i].meta.likes.length;
                likeCommentsCount.comments += values[i].comments.length;
            }

            //Show user profile Information
            let followName = '';
            if (id == null && username == null) {
                followName = 'u';
            } else {
                followName = userData.username.substring(0, 1);
            }
            let infoBar = document.createElement('div');
            infoBar.textContent = `${userData.username}\t\t|\t\t Post ${userData.posts.length}\t\t|\t\t❤ ${likeCommentsCount.likes}\t\t|\t\t 💬 ${likeCommentsCount.comments}\t\t|\t\t follower ${followName} ${userData.followed_num}\t\t|\t\t ${followName} follow ${userData.following.length}`
            infoBar.setAttribute('id', 'userProfileInformation');
            infoBar.setAttribute('class', 'user-Profile-Information');
            //Add infoBar to userProfile
            userProfile.appendChild(infoBar);
            resolve(true);
        });
    });
}

//Ability to Edit or Delete Profile elements

// calls editProfile and editPost functions
function editDelete(api, main) {
    editProfile(api, main);
    editPost(api, main);
}

//Edit profile

// Adds edit profile button to top of my profile and listens for a click event
function editProfile(api, main) {
    let userProfileDisplay = document.getElementById('userProfileDisplay');
    let editProfileBtn = document.createElement('p');
    editProfileBtn.textContent = 'Edit Profile';
    editProfileBtn.setAttribute('id', 'editProfile');
    editProfileBtn.setAttribute('class', 'edit-profile-btn');
    editProfileBtn.style.fontWeight = 'bold';
    userProfileDisplay.appendChild(editProfileBtn);

    async function editProfileDetails(event) {
        let newPostNav = document.getElementById('myProfileNav');
        newPostNav.textContent = '->' + 'Edit Profile' + '<-';
        document.getElementById('userDisplay').remove();
        let updateProfileDiv = document.createElement('div');
        updateProfileDiv.setAttribute('id', 'userDisplay');
        updateProfileDiv.setAttribute('class', 'updateProfile');
        let submitBtn = document.createElement('p');
        submitBtn.textContent = 'submit';
        submitBtn.setAttribute('id', 'submitchangeOrderBtn');
        submitBtn.setAttribute('class', 'submit-Btn');
        let response = await api.getUserData();
        USER_DATA = await response.json();
        populateChangeFields(updateProfileDiv);
        updateProfileDiv.appendChild(submitBtn);
        main.appendChild(updateProfileDiv);
        submitBtn.addEventListener('click', async function () {
            let inputValues = {
                'officialName': document.getElementById('changeName').value,
                'email': document.getElementById('changeEmail').value,
                'newPassword': document.getElementById('changePassword').value,
                'confirmPassword': document.getElementById('confirmChangePassword').value
            }
            // Takes an array of values from input fiels and populates object for api post
            let changeFlag = 0;
            let holdFlag = 0;
            let changeObject = {};
            if (inputValues.email != '' && inputValues.email != null) {
                changeFlag = 1;
                let re = /^(([^<>()\[\]\\.,;:\s@']+(\.[^<>()\[\]\\.,;:\s@']+)*)|('.+'))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                if (re.test(String(inputValues.email).toLowerCase())) {
                    changeObject['email'] = inputValues.email;
                } else {
                    holdFlag = 1;
                    if (document.getElementById('updateProfile') != null) {
                        document.getElementById('updateProfile').remove();
                    }
                    let error = document.createElement('p');
                    error.setAttribute('id', 'updateProfile');
                    error.style.color = 'red';
                    error.textContent = 'Incorrect Email Format.';
                    document.getElementById('confirmChangePassword').after(error);
                }

            }
            //Update password
            if (inputValues.newPassword == '' || inputValues.newPassword == null, inputValues.confirmPassword == '' || inputValues.confirmPassword == null) {
                //Do Nothing
            } else {
                if (holdFlag === 0) {
                    if (inputValues.newPassword === inputValues.confirmPassword) {
                        changeFlag = 1;
                        changeObject['password'] = inputValues.confirmPassword;
                    } else {
                        holdFlag = 1;
                        if (document.getElementById('updateProfile') != null) {
                            document.getElementById('updateProfile').remove();
                        }
                        let error = document.createElement('p');
                        error.setAttribute('id', 'updateProfile');
                        error.style.color = 'red';
                        error.textContent = 'Passwords Do Not Match';
                        document.getElementById('confirmChangePassword').after(error);
                    }
                }
            }
            //Update name
            if (inputValues.officialName != '' && inputValues.officialName != null && holdFlag === 0) {
                changeFlag = 1;
                changeObject['name'] = inputValues.officialName;
            }
            if (holdFlag === 1) {
                changeFlag = 2;
            }
            changeObject = [changeObject, changeFlag];
            if (changeObject[1] === 1) {
                api.putProfileUpdate(changeObject[0]);
                alert('Profile Updated');
                updateNavigationBar(3);
                await showProfile(api, document.querySelector('main'));
                editDelete(api, document.querySelector('main'));
            } else if (changeObject[1] === 2) {
                // Do nothing
            } else {
                if (document.getElementById('updateProfile') != null) {
                    document.getElementById('updateProfile').remove();
                }
                let error = document.createElement('p');
                error.setAttribute('id', 'updateProfile');
                error.style.color = 'red';
                error.textContent = 'Provide Input for the field of your choice.';
                document.getElementById('confirmChangePassword').after(error);
            }
        });
    }

    editProfileBtn.addEventListener('click', editProfileDetails, false);
}

//Create form for profile update
function populateChangeFields(updateProfileDiv) {
    let changeName = document.createElement('label');
    changeName.textContent = 'New Name';
    changeName.setAttribute('for', 'changeName');
    changeName.style.fontWeight = 'bold';
    let inputName = document.createElement('input');
    inputName.setAttribute('class', 'change-field');
    inputName.setAttribute('id', 'changeName');
    inputName.setAttribute('type', 'text');
    inputName.setAttribute('placeholder', USER_DATA.name);

    updateProfileDiv.appendChild(changeName);
    updateProfileDiv.appendChild(inputName);

    let changeEmail = document.createElement('label');
    changeEmail.textContent = 'New Email Address';
    changeEmail.setAttribute('for', 'changeEmail');
    changeEmail.style.fontWeight = 'bold';
    let inputEmail = document.createElement('input');
    inputEmail.setAttribute('class', 'change-field');
    inputEmail.setAttribute('id', 'changeEmail');
    inputEmail.setAttribute('type', 'email');
    inputEmail.setAttribute('placeholder', USER_DATA.email);
    updateProfileDiv.appendChild(changeEmail);
    updateProfileDiv.appendChild(inputEmail);

    let changePassword = document.createElement('label');
    changePassword.textContent = 'Enter New Password';
    changePassword.setAttribute('for', 'changePassword');
    changePassword.style.fontWeight = 'bold';
    let inputPassword = document.createElement('input');
    inputPassword.setAttribute('class', 'change-field');
    inputPassword.setAttribute('id', 'changePassword');
    inputPassword.setAttribute('type', 'password');
    inputPassword.setAttribute('placeholder', 'Enter New Passowrd');
    updateProfileDiv.appendChild(changePassword);
    updateProfileDiv.appendChild(inputPassword);

    let confirmPasswordChange = document.createElement('label');
    confirmPasswordChange.textContent = 'Confirm New Password';
    confirmPasswordChange.setAttribute('for', 'confirmPasswordChange');
    confirmPasswordChange.style.fontWeight = 'bold';
    let inputPasswordConfirmation = document.createElement('input');
    inputPasswordConfirmation.setAttribute('class', 'change-field');
    inputPasswordConfirmation.setAttribute('id', 'confirmChangePassword');
    inputPasswordConfirmation.setAttribute('type', 'password');
    inputPasswordConfirmation.setAttribute('placeholder', 'Confirm Password');
    updateProfileDiv.appendChild(confirmPasswordChange);
    updateProfileDiv.appendChild(inputPasswordConfirmation);
}


//Edit Posts
function editPost(api, main) {
    let postPublished = document.getElementsByClassName('post-published');
    for (let i = 0; i < postPublished.length; i++) {
        let publishId = postPublished[i].getAttribute('id');
        let postId = publishId.match(/^(\d+).+/)[1];
        let editPostEle = document.createElement('p');
        editPostEle.textContent = 'Edit Post';
        editPostEle.setAttribute('id', postId + 'editPost');
        editPostEle.setAttribute('class', 'edit-post');
        postPublished[i].after(editPostEle);

    }

    let editPostsElement = document.getElementsByClassName('edit-post');

    function editPostEvent(event) {
        let editPostId = event.target.id;
        let postId = editPostId.match(/^(\d+).+/)[1];
        let myProfileNav = document.getElementById('myProfileNav');
        myProfileNav.textContent = 'My Profile';
        let newPostNav = document.getElementById('newPostNav');
        newPostNav.textContent = '->' + 'Edit Post' + '<-';
        document.getElementById('userDisplay').remove();
        let newPostDiv = document.createElement('div');
        newPostDiv.setAttribute('id', 'userDisplay');
        newPostDiv.setAttribute('class', 'editPost');
        main.appendChild(newPostDiv);
        updatePost(api, newPostDiv, postId);
    }

    for (let i = 0; i < editPostsElement.length; i++) {
        editPostsElement[i].addEventListener('click', editPostEvent, false);
    }
}

// Creates form elements for update post and delete post
// listens for click event on those elements
function updatePost(api, mainRole, postId) {
    let centerDiv = document.createElement('div');
    centerDiv.setAttribute('id', 'centerDivNewPost');
    centerDiv.setAttribute('class', 'center-div');

    let postDesc = document.createElement('label');
    postDesc.textContent = 'Description';
    postDesc.setAttribute('for', 'postDescription');
    postDesc.style.fontWeight = 'bold';
    let descriptionElement = document.createElement('input');
    descriptionElement.setAttribute('class', 'description-field');
    descriptionElement.setAttribute('id', 'updatePostDescription');
    descriptionElement.setAttribute('type', 'text');
    descriptionElement.setAttribute('placeholder', 'Add your new description here');
    descriptionElement.setAttribute('name', 'description');
    descriptionElement.setAttribute('require', true);

    centerDiv.appendChild(postDesc);
    centerDiv.appendChild(descriptionElement);

    let upImage = document.createElement('input');
    upImage.setAttribute('class', 'upload-file');
    upImage.setAttribute('id', 'updateImage');
    upImage.setAttribute('type', 'file');
    upImage.setAttribute('name', 'uploadImageFile');
    upImage.setAttribute('require', true);

    let submitBtn = document.createElement('p');
    submitBtn.textContent = 'submit';
    submitBtn.setAttribute('id', 'submitUpdatePostBtn');
    submitBtn.setAttribute('class', 'submit-Btn');

    let deleteBtn = document.createElement('p');
    deleteBtn.textContent = 'DELETE POST';
    deleteBtn.setAttribute('id', 'confirmPostDelete');
    deleteBtn.setAttribute('class', 'confirm-delete-post');

    centerDiv.appendChild(upImage);
    centerDiv.appendChild(submitBtn);
    centerDiv.appendChild(deleteBtn);
    mainRole.appendChild(centerDiv);

    let img = document.createElement('img');
    img.setAttribute('id', 'displayUpdatedImage');
    img.setAttribute('src', '#');
    img.setAttribute('class', 'post-image');
    img.style.display = 'none';
    centerDiv.appendChild(img);

    let post_description = document.createElement('p');
    post_description.setAttribute('id', 'displayUpdatedDescription');
    post_description.setAttribute('class', 'post-text-box');
    post_description.style.display = 'none';
    centerDiv.appendChild(post_description);

    let confirm_post = document.createElement('p');
    confirm_post.textContent = 'UPDATE POST';
    confirm_post.setAttribute('id', 'confirmPostUpdate');
    confirm_post.setAttribute('class', 'confirm-post');
    confirm_post.style.display = 'none';
    centerDiv.appendChild(confirm_post);

    submitBtn.addEventListener('click', function () {
        let imgElement = document.getElementById('displayUpdatedImage');
        let descElement = document.getElementById('displayUpdatedDescription');
        let postBtn = document.getElementById('confirmPostUpdate');

        let post_desc = document.getElementById('updatePostDescription').value;
        let imageRaw = document.getElementById('updateImage').files;

        //Ensure description is hidden at the beginning
        imgElement.style.display = 'none';
        descElement.style.display = 'none';
        postBtn.style.display = 'none';
        if (postBtn.removeEventListener) {
            postBtn.removeEventListener('click', postUpdateClicked);
        }
        let errorUpdatePost = document.getElementById('errorUpdatePost');
        if (errorUpdatePost) {
            document.getElementById('errorUpdatePost').remove();
        }
        if (imageRaw && imageRaw[0] && isAnyStringEmpty([post_desc]) === false) {
            const reader = new FileReader();
            reader.addEventListener('load', function () {
                let base64Img = reader.result;
                let pngRE = /data:image\/png;base64,(.+)/;
                let base64Encoding = pngRE.exec(base64Img);
                if (base64Encoding === null) {
                    if (document.getElementById('errorUpdatePost') != null) {
                        document.getElementById('errorUpdatePost').remove();
                    }
                    let error = document.createElement('p');
                    error.setAttribute('id', 'errorUpdatePost');
                    error.style.color = 'red';
                    error.textContent = 'Incorrect Image format.';
                    upImage.after(error);
                } else {
                    descElement.style.display = 'block';
                    descElement.textContent = post_desc;
                    let img = document.querySelector('img');
                    img.style.display = 'block';
                    img.src = URL.createObjectURL(imageRaw[0]);
                    confirmNupdate(api, {
                        'description_text': post_desc,
                        'src': base64Encoding[1]
                    }, postId);
                }
            }, false);
            reader.readAsDataURL(imageRaw[0]);
        } else if (imageRaw && imageRaw[0]) {
            const reader = new FileReader();
            reader.addEventListener('load', function () {
                let base64Img = reader.result;
                let pngRE = /data:image\/png;base64,(.+)/;
                let base64Encoding = pngRE.exec(base64Img);
                if (base64Encoding === null) {
                    if (document.getElementById('errorUpdatePost') != null) {
                        document.getElementById('errorUpdatePost').remove();
                    }
                    let error = document.createElement('p');
                    error.setAttribute('id', 'errorUpdatePost');
                    error.style.color = 'red';
                    error.textContent = 'Incorrect Image format.';
                    upImage.after(error);
                } else {
                    let img = document.querySelector('img');  // $('img')[0]
                    img.style.display = 'block';
                    img.src = URL.createObjectURL(imageRaw[0]);
                    confirmNupdate(api, { 'src': base64Encoding[1] }, postId);
                }
            }, false);
            reader.readAsDataURL(imageRaw[0]);
        } else if (isAnyStringEmpty([post_desc]) === false) {
            descElement.style.display = 'block';
            descElement.textContent = post_desc;
            confirmNupdate(api, { 'description_text': post_desc }, postId);
        } else {
            if (document.getElementById('errorUpdatePost') != null) {
                document.getElementById('errorUpdatePost').remove();
            }
            let error = document.createElement('p');
            error.setAttribute('id', 'errorUpdatePost');
            error.style.color = 'red';
            error.textContent = 'Please add Description or Image.';
            upImage.after(error);
        }
    });

    deleteBtn.addEventListener('click', async function () {
        let resp = await api.deleteUpdatePost(postId);

        if (resp.status === 200) {
            alert('Post Deleted');
            //document.getElementById('userDisplay').remove();
            updateNavigationBar(3);
            await showProfile(api, document.querySelector('main'));
            editDelete(api, document.querySelector('main'));
        } else {
            let displayPostBtn = document.getElementById('confirmPostUpdate');
            if (document.getElementById('errorUpdatePost') != null) {
                document.getElementById('errorUpdatePost').remove();
            }
            let error = document.createElement('p');
            error.setAttribute('id', 'errorUpdatePost');
            error.style.color = 'red';
            error.textContent = 'Post Not Found. Try Again.';
            displayPostBtn.after(error);
        }
    });

}

// When post update event is triggered contacts api to make changes
async function postUpdateClicked(object) {
    let displayPostBtn = document.getElementById('confirmPostUpdate');

    let errorUpdatePost = document.getElementById('errorUpdatePost');
    if (errorUpdatePost) {
        document.getElementById('errorUpdatePost').remove();
    }

    let resp = await object.api.putUpdatePost(object.postId, object.postObject);

    if (resp.status === 200) {
        alert('Post Updated');
        updateNavigationBar(3);
        await showProfile(object.api, document.querySelector('main'));
        editDelete(object.api, document.querySelector('main'));
    } else {
        if (document.getElementById('errorUpdatePost') != null) {
            document.getElementById('errorUpdatePost').remove();
        }
        let error = document.createElement('p');
        error.setAttribute('id', 'errorUpdatePost');
        error.style.color = 'red';
        error.textContent = 'Image Could Not Be processed. Try Again.';
        displayPostBtn.after(error);
    }
}

// Confirms if the user wants to continue with update
function confirmNupdate(api, postObject, postId) {
    let displayPostBtn = document.getElementById('confirmPostUpdate');
    displayPostBtn.style.display = 'block';
    let object = {
        'api': api,
        'postObject': postObject,
        'postId': postId
    }
    displayPostBtn.addEventListener('click', postUpdateClicked.bind(null, object));
}

// Following
function following(api) {
    return new Promise(async (resolve) => {
        let response = await api.getUserData();
        USER_DATA = await response.json();

        let scrollBoxContainer = document.createElement('div');
        scrollBoxContainer.setAttribute('id', 'scrollBoxContainerID');
        scrollBoxContainer.setAttribute('class', 'scrollBoxContainer');
        let scrollBox = document.createElement('div');
        scrollBox.setAttribute('id', 'scrollBoxFollowing');
        scrollBox.setAttribute('class', 'scrollBox');

        let userProfileDisplay = document.getElementById('userProfileDisplay');

        for (let i = 0; i < USER_DATA.following.length; i++) {
            let response = await api.getUserData(USER_DATA.following[i], null);
            let following_user_data = await response.json();
            let following_user_element = document.createElement('li');
            following_user_element.textContent = following_user_data.username;
            following_user_element.setAttribute('id', 'following-' + USER_DATA.following[i])
            following_user_element.setAttribute('class', 'following-user');
            scrollBox.appendChild(following_user_element);
        }
        scrollBoxContainer.appendChild(scrollBox);
        userProfileDisplay.after(scrollBoxContainer);
    });
}
