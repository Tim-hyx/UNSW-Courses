// https://reactjs.org/docs/react-component.html

import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const [name, setName] = React.useState('');
  const [age, setAge] = React.useState(0);

  React.useEffect(() => {
    console.log('Only run once');
  }, [name]);

  return (
    <div className="App">
      <p>
        <input type="text" value={name} onChange={e => setName(e.target.value)} />
        <input type="text" value={age} onChange={e => setAge(e.target.value)} />
      </p>
      <p>
        My name is {name} and my age is {age}.
      </p>
    </div>
  );
}

/*class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
      age: '0',
    };
  }

  componentDidUpdate(prevProps, prevState) {
    if (this.state !=)
  }

  render() {
    return (
      <div className="App">
        <p>
          <input type="text" value={this.state.name} onChange={e => this.setState({ ...this.state, name: e.target.value })} />
          <input type="text" value={this.state.age} onChange={e => this.setState({ ...this.state, age: e.target.value })} />
        </p>
        <p>
          My name is {this.state.name} and my age is {this.state.age}.
        </p>
      </div>
    );
  }
}*/

export default App;
