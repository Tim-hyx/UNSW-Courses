import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  const [org, setOrg] = React.useState(0);

  React.useEffect(() => {
    async function fetchdata() {
      try {
        const res = await fetch(`https://api.github.com/orgs/microsoft`);
        const d = await res.json();
        setOrg(d.public_repos);
      } catch (err) {
        console.log(err);
      }
    }

    fetchdata();
  }, []);

  return (
    <div style={{ margin: '50px' }}>
      <input disabled="true" type="text" value={org} />
    </div>
  );
}

export default App;
