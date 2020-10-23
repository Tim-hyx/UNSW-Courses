// /**
//  * Make a request to `path` with `options` and parse the response as JSON.
//  * @param {*} path The url to make the reques to.
//  * @param {*} options Additiona options to pass to fetch.
//  */
// const getJSON = (path, options) =>
//     fetch(path, options)
//         .then(res => res.json())
//         .catch(err => console.warn(`API_ERROR: ${err.message}`));

let TOKEN;
/**
 * This is a sample class API which you may base your code on.
 * You don't have to do this as a class.
 */
export default class API {

    // /**
    //  * Defaults to the API URL
    //  * @param {string} url
    //  */
    // constructor(url = API_URL) {
    //     this.url = url;
    // }
    //
    // makeAPIRequest(path) {
    //     return getJSON(`${this.url}/${path}`);
    // }

    postRegistration(registrationObject) {
        return fetch('http://127.0.0.1:5000/auth/signup', {
            method: 'POST',
            body: JSON.stringify(registrationObject),
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(async function (resp) {
                if (resp.status === 200 || resp.status === 409) {
                    let tokenObject = await resp.json();
                    TOKEN = tokenObject.token;
                    return resp;
                } else if (resp.status === 400) {
                    throw resp.status;
                }
            });
    }

    postLogin(authObject) {
        return fetch('http://127.0.0.1:5000/auth/login', {
            method: 'POST',
            body: JSON.stringify(authObject),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        })
            .then(async function (resp) {
                let tokenObject = await resp.json();
                if (resp.status === 200) {
                    TOKEN = tokenObject.token;
                }
                return resp.status;
            });
    }

    getFeed(p, n) {
        return fetch(`http://127.0.0.1:5000/user/feed?p=${p}&n=${n}`, {
            method: 'GET',
            headers: {
                'accept': 'application/json',
                'Authorization': 'Token ' + TOKEN
            }
        })
            .then(response => {
                return response.json();
            });
    }

    getPost(id) {
        return fetch(`http://127.0.0.1:5000/post/?id=${id}`, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Authorization': 'Token ' + TOKEN
            }
        })
            .then(function (resp) {
                if (resp.status === 200) {
                    return resp.json();
                } else {
                    throw resp.status;
                }
            });
    }

    putLike(id) {
        return fetch(`http://127.0.0.1:5000/post/like?id=${id}`, {
            method: 'PUT',
            headers: {
                'accept': 'application/json',
                'Authorization': 'Token ' + TOKEN
            }
        })
            .then(function (resp) {
                if (resp.status === 200) {
                    return resp.status;
                } else {
                    throw resp.status;
                }
            });
    }

    putUnLike(id) {
        return fetch(`http://127.0.0.1:5000/post/unlike?id=${id}`, {
            method: 'PUT',
            headers: {
                'accept': 'application/json',
                'Authorization': 'Token ' + TOKEN
            }
        })
            .then(function (resp) {
                if (resp.status === 200) {
                    return resp.status;
                } else {
                    throw resp.status;
                }
            });
    }

    putComment(id, commentObject) {
        return fetch(`http://127.0.0.1:5000/post/comment?id=${id}`, {
            method: 'PUT',
            body: JSON.stringify(commentObject),
            headers: {
                'Accept': 'application/json',
                'Authorization': 'Token ' + TOKEN,
                'Content-Type': 'application/json'
            }
        })
            .then(function (resp) {
                if (resp.status === 200) {
                    return resp.status;
                } else {
                    throw resp.status;
                }
            });
    }

    getUserData(id = null, username = null) {
        let payload;
        if (id !== null) {
            payload = '?id=' + id;
        } else if (username !== null) {
            payload = '?username=' + username;
        } else {
            payload = '';
        }
        return fetch(`http://127.0.0.1:5000/user/${payload}`, {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Authorization': 'Token ' + TOKEN
            }
        })
            .then(function (resp) {
                if (resp.status === 200 || resp.status === 404) {
                    return resp;
                } else {
                    throw resp.status;
                }
            });
    }

    putFollowUser(username) {
        return fetch(`http://127.0.0.1:5000/user/follow?username=${username}`, {
            method: 'PUT',
            headers: {
                'Accept': 'application/json',
                'Authorization': 'Token ' + TOKEN,
            }
        })
            .then(function (resp) {
                if (resp.status === 200 || resp.status === 404) {
                    return resp.status;
                } else {
                    throw resp.status;
                }
            });
    }

    putUnfollowUser(username) {
        return fetch(`http://127.0.0.1:5000/user/unfollow?username=${username}`, {
            method: 'PUT',
            headers: {
                'Accept': 'application/json',
                'Authorization': 'Token ' + TOKEN,
            }
        })
            .then(function (resp) {
                if (resp.status === 200) {
                    return resp.status;
                } else {
                    throw resp.status;
                }
            });
    }

    postPost(postObject) {
        let fetchObject = {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Authorization': 'Token ' + TOKEN,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(postObject)
        };
        return fetch('http://127.0.0.1:5000/post/', fetchObject)
            .then(function (resp) {
                if (resp.status === 200 || resp.status === 400) {
                    return resp;
                } else {
                    throw resp.status + ' 400: Malformed Request / Image could not be processed | 403: Invalid Auth Token';
                }

            });
    }

    putUpdatePost(id, postObject) {
        return fetch(`http://127.0.0.1:5000/post/?id=${id}`, {
            method: 'PUT',
            body: JSON.stringify(postObject),
            headers: {
                'Accept': 'application/json',
                'Authorization': 'Token ' + TOKEN,
                'Content-Type': 'application/json'
            }
        })
            .then(function (resp) {
                if (resp.status === 200) {
                    return resp;
                } else {
                    throw resp.status;
                }
            });
    }

    deleteUpdatePost(id) {
        return fetch(`http://127.0.0.1:5000/post/?id=${id}`, {
            method: 'delete',
            headers: {
                'Accept': 'application/json',
                'Authorization': 'Token ' + TOKEN
            }
        })
            .then(function (resp) {
                if (resp.status === 200) {
                    return resp;
                } else {
                    throw resp.status;
                }
            });
    }

    putProfileUpdate(updateObject) {
        return fetch('http://127.0.0.1:5000/user/', {
            method: 'PUT',
            body: JSON.stringify(updateObject),
            headers: {
                'Accept': 'application/json',
                'Authorization': 'Token ' + TOKEN,
                'Content-Type': 'application/json'
            }
        })
            .then(function (resp) {
                if (resp.status === 200) {
                    return resp;
                } else {
                    throw resp.status;
                }
            });
    }

}
