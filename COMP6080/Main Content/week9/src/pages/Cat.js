import React from 'react';

const Cat = () => {
	const login = () => {
		localStorage.setItem('auth_token', 'LOGGEDIN');
	}
	const logout = () => {
		localStorage.removeItem('auth_token');
	}
	return (
		<div>
			Cat
			<button onClick={login}>Login</button>
			<button onClick={logout}>Logout</button>
		</div>
	);
};

export default Cat;