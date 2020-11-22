import React from 'react';
import './App.css';

const CAT_FACT_URL = 'https://cat-fact.herokuapp.com/facts';

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function App() {
  const [loadingState, setLoadingState] = React.useState('idle');
  const [catFact, setCatFact] = React.useState(undefined);

  React.useEffect(() => {
    async function fetchCatFacts() {
      setLoadingState('loading');
      const response = await fetch(CAT_FACT_URL);
      const json = await response.json();
      const length = json['all'].length;
      const catFactIndex = getRandomInt(length);
      setCatFact(json['all'][catFactIndex]['text'])
      setLoadingState('success');
    }

    fetchCatFacts();
  }, []);

  return (
    <section className="App">
      { loadingState !== 'success' && <p>Loading...</p> }
      { loadingState === 'success' && <p>{catFact}</p> }
    </section>
  );
}

export default App;
