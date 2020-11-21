import { combineReducers } from "redux";
import authentication from "./Login";
import alert from "./Alert";
import register from './Signin';
// will add more reducer here
export default combineReducers({ authentication, alert ,register});
