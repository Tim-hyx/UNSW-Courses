import React from "react";

const LabelledInput = (props) => {
  return (
    <>
      <div style={{ padding: '10px', background: '#eee', display: 'inline-block' }}>
      	{props.label}: {' '}
        <input type="text" />
      </div>
    </>
  );
}

export default LabelledInput;
