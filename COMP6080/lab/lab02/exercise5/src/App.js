import React from 'react';
import './App.css';
import shrek from './shrek.jpg';

function App() {
    return (
        <div className="App">
            <header className="App-header">
                <img src={shrek} className="App-logo" alt="shrek"/>
                <p>
                    Pa-ran-nah!
                </p>
                <a
                    className="App-link"
                    href="https://reactjs.org"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Learn React
                </a>
            </header>
        </div>
    );
}

export default App;
