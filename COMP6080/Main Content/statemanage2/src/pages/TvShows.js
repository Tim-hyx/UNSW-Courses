import React from 'react';
import { StoreContext } from '../utils/store';

const TvShows = () => {
  const [newItem, setNewItem] = React.useState('');
  const context = React.useContext(StoreContext);
  const [tvShows, setTvShows] = context.tvShows;
  return (
    <div>
      <ul>
        {tvShows.map((tvshow, idx) => (
          <li>{tvshow}</li>
        ))}
      </ul>
      <input type="text" value={newItem} onChange={e => setNewItem(e.target.value)} />
      <button onClick={() => setTvShows([...tvShows, newItem])}>Add</button>
    </div>
  );
}

export default TvShows;
