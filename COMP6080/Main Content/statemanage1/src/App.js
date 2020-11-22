import React from 'react';
import logo from './logo.svg';
import './App.css';

import Plus from './Plus';
import Minus from './Minus';

function App() {

  const [value, setValue] = React.useState(0);

  return (
    <div>
      <input type="text" disabled value={value} />
      <Plus onClick={() => setValue(value + 1)} />
      <Minus onClick={() => setValue(value - 1)} />
    </div>
  );
}

export default App;
