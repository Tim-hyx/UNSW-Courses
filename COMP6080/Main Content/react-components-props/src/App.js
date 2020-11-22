import React from 'react';

import logo from './logo.svg';
import './App.css';
import Button from './components/Button';
import Paragraph from './components/Paragraph';

function App() {
  const [welcome, setWelcome] = React.useState('Hello');
  return (
    <div className="App">
      {welcome}
      <Button title="Cat" background="red" click={() => setWelcome(welcome + '!!')} />
      <Button title="Dog" background="blue" click={() => alert('hey super friend')} />
      <Button background="orange" click={() => console.log('Goodbye')}  />
      {/*<Paragraph text="I am a duck" />*/}
      <Paragraph>
        I am a duck
        <Button background="orange" click={() => console.log('Goodbye')}  />
      </Paragraph>
    </div>
  );
}

export default App;
