import { userConstants, alertConstants } from "./actionTypes";
import API_URL from "../constants";

// this file constains all the action creators used in this project

// action creator for user status management
export const loginRequest = () => ({
    type: userConstants.LOGIN_REQUEST,
});

export const loginSuccess = (accessToken) => ({
    type: userConstants.LOGIN_SUCCESS,
    accessToken,
});

export const loginFailure = () => ({
    type: userConstants.LOGIN_FAILURE,
});
export const logoutRequest = () => ({
    type: userConstants.LOGOUT_REQUEST,
});

export const logoutSuccess = () => ({
    type: userConstants.LOGOUT_SUCCESS,
});

export const logoutFailure = () => ({
    type: userConstants.LOGOUT_FAILURE,
});

export const registryRequest = () => ({
    type: userConstants.REGISTER_REQUEST,
});

export const registrySuccess = () => ({
    type: userConstants.REGISTER_SUCCESS,
});

export const registryFailure = () => ({
    type: userConstants.REGISTER_FAILURE,
});

// action creator for alert
export const alertSuccess = (message) => ({
    type: alertConstants.SUCCESS,
    message,
});

export const alertError = (message) => ({
    type: alertConstants.ERROR,
    message,
});

export const alertClear = () => ({
    type: alertConstants.CLEAR,
});

// async action creator
export const login = (email, password) => {
    return (dispatch) => {
        dispatch(loginRequest());
        fetch(`${API_URL}/admin/auth/login`, {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ email, password }),
        })
            .then((res) => {
                if (res.ok) {
                    return Promise.resolve(res.json());
                }
                return Promise.resolve(res.json()).then(data => {
                    return Promise.reject(data.error);
                });
            })
            .then((data) => {
                // pretent api give us an accessToken
                localStorage.setItem("accessToken", data.token);
                dispatch(loginSuccess(data.token));
                dispatch(alertSuccess("Login Successfully"));
            },
            (error) => {
                dispatch(loginFailure());
                dispatch(alertError(error));
            }
            )
            .catch((error) => {
                dispatch(loginFailure());
                dispatch(alertError(error.message));
            });
    };
};



export const signin = (email, password, name) => {
    return (dispatch) => {
        dispatch(registryRequest());
        fetch(`${API_URL}/admin/auth/register`, {
            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ email, password, name }),
        })
            .then((res) => {
                if (res.ok) {
                    return Promise.resolve(res.json());
                }
                return Promise.resolve(res.json()).then(data => {
                    return Promise.reject(data.error);
                });
            })
            .then((data) => {

                dispatch(registrySuccess());
                localStorage.setItem("accessToken", data.token);
                dispatch(loginSuccess(data.token));
                dispatch(alertSuccess("Signin Successfully"));


            }, (error) => {
                dispatch(registryFailure());
                dispatch(alertError(error));
            })
            .catch((error) => {
                dispatch(registryFailure());
                dispatch(alertError(error.message));
            });
    };
};

export const logout = () => {
    return (dispatch) => {
        dispatch(logoutRequest());
        fetch(`${API_URL}/admin/auth/logout`, {
            method: "POST",
            headers: {
                Accept: "application/json",
                Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
            },
        })
            .then((res) => {
                if (res.ok) {
                    return Promise.resolve(res.json());
                }
                return Promise.resolve(res.json()).then(data => {
                    return Promise.reject(data.error);
                });

            })
            .then(() => {
                localStorage.removeItem("accessToken");
                dispatch(logoutSuccess());
            }, (error) => {
                alertError(error);
                dispatch(logoutFailure());
            })
            .catch((error) => {
                alertError(error.message);
                dispatch(logoutFailure());
            });
    };
};
