import React from 'react';
import { StoreContext } from '../utils/store';

const Movies = () => {
  const [newItem, setNewItem] = React.useState('');
  const context = React.useContext(StoreContext);
  const [movies, setMovies] = context.movies;
  return (
    <div>
      <ul>
        {movies.map((movie, idx) => (
          <li>{movie}</li>
        ))}
      </ul>
      <input type="text" value={newItem} onChange={e => setNewItem(e.target.value)} />
      <button onClick={() => setMovies([...movies, newItem])}>Add</button>
    </div>
  );
}

export default Movies;
