import React from "react";
import LabelledInput from '../components/LabelledInput';

const Increase = () => {

  const increaseCount = async () => {
  	const response = await fetch('http://localhost:6080/count/increment', {
      method: 'POST',
      body: JSON.stringify({
      	increase: 50,
      }),
      headers: {
      	'Content-type': 'application/json',
      },
    });
    alert('Count increased!');
  }

  return (
    <>
      <LabelledInput label={'Enter increase number'} />
      <div>
      	<button onClick={increaseCount}>Increase number</button>
      </div>
    </>
  );
}

export default Increase;
