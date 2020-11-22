import React from 'react';
import { withRouter } from "react-router";

export const loginCheck = (BigBrainComponent) => withRouter((props) => {
	const [loggedIn, setLoggedIn] = React.useState(false);

	React.useEffect(() => {
		if (localStorage.getItem('auth_token') !== null) {
			setLoggedIn(true);	
		} else {
			setTimeout(() => {
				props.history.push('/cat');
			}, 2000);
		}
	}, []);

	if (!loggedIn) {
		return <div>Not logged in. Redirecting you now!</div>;
	}

	return <BigBrainComponent />;
});