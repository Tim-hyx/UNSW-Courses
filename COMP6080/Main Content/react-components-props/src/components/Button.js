import React from 'react';

const Button = ({ background, click, title }) => {
  return (
  	<button
  	  style={{
  	    width: '100px',
  	    background: background
  	  }}
  	  onClick={click}
  	>
      {title ? title : 'Submit'}
    </button>
  );
}

export default Button; 