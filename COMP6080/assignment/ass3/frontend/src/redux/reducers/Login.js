import { userConstants } from "../actionTypes";

// check the localStorage see if user already logged in
const accessToken = localStorage.getItem("accessToken");

// Shorthand property names stynex
const initialState = accessToken
    ? { loggedIn: true, accessToken }
    : { loggedIn: false };

// given the current state and action return the next state
export default (state = initialState, action) => {
    switch (action.type) {
    case userConstants.LOGIN_REQUEST:
        return {
            loggingIn: true,
        };
    case userConstants.LOGIN_SUCCESS:
        return {
            loggedIn: true,
            accessToken: action.accessToken,
        };
    case userConstants.LOGIN_FAILURE:
        return {};
    case userConstants.LOGOUT_REQUEST:
        return { ...state, loggingOut: true };
    case userConstants.LOGOUT_SUCCESS:
        return { loggedIn: false };
    case userConstants.LOGOUT_FAILURE:
        return state;
    default:
        return state;
    }
};
