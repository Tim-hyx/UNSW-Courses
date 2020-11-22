import React from 'react';
import {
  Link,
  Redirect
} from "react-router-dom";
import { withRouter } from "react-router";
import { loginCheck } from './loginCheck';

const Dog = (props) => {
	const quizid = props.match.params.quizid;
	
	if (quizid) {
		return <div>Welcome to {quizid}</div>
	} else {
		return <div><Link to="/dog/123"><button>Go to quiz 123</button></Link></div>;
	}
};

export default loginCheck(withRouter(Dog));