import React from 'react';
import { StoreContext } from '../utils/store';

const All = () => {
  const context = React.useContext(StoreContext);
  const [movies] = context.movies;
  const [tvShows] = context.tvShows;
  return (
    <div>
      <h2>Movies</h2>
      <ul>
        {movies.map((movie, idx) => (
          <li>{movie}</li>
        ))}
      </ul>
      <h2>TV Shows</h2>
      <ul>
        {tvShows.map((tvShow, idx) => (
          <li>{tvShow}</li>
        ))}
      </ul>
    </div>
  );
}

export default All;
