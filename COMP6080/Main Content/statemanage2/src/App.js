import React from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from 'react-router-dom';

import StoreProvider  from './utils/store';
import All from './pages/All';
import TvShows from './pages/TvShows';
import Movies from './pages/Movies';

const App = () => {
  return (
    <StoreProvider>	
      <Router>
        <div>
          <nav>
            <ul>
              <li>
                <Link to="/">All</Link>
              </li>
              <li>
                <Link to="/movies">Movies</Link>
              </li>
              <li>
                <Link to="/tv">TV Shows</Link>
              </li>
            </ul>
          </nav>
          <hr />
          <Switch>
            <Route path="/tv">
              <TvShows />
            </Route>
            <Route path="/movies">
              <Movies />
            </Route>
            <Route path="/">
              <All />
            </Route>
          </Switch>
        </div>
      </Router>
    </StoreProvider>
  );
}

export default App;
