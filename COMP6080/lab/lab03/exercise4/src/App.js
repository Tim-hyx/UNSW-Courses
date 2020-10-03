import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p className="title">Your are safe now</p>
        <div className="human">human</div>
        <img src="https://i.ytimg.com/vi/wWqdhBdeMSg/hqdefault.jpg" className="App-logo" alt="logo" />
        <p className="text">
          You either die a hero, or live long<br/>enough too see yourself come the villian:
        </p>
        <a
          className="App-link"
          href="https://www.youtube.com/watch?v=ByH9LuSILxU"
          target="_blank"
          rel="noopener noreferrer"
        >
          <li className="video"><span>Cat Video1</span></li>
        </a>
        <a
            className="App-link"
            href="https://www.youtube.com/watch?v=SB-qEYVdvXA"
            target="_blank"
            rel="noopener noreferrer"
        >
          <li className="video"><span>Cat Video2</span></li>
        </a>
      </header>
    </div>
  );
}

export default App;
