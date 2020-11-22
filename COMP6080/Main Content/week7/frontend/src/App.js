import React from "react";
import logo from './logo.svg';
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import Get from './pages/Get';
import Increase from './pages/Increase';

function App() {
  return (
    <>
      <Router>
        <div>
          <nav>
            <ul>
              <li>
                <Link to="/get">Get</Link>
              </li>
              <li>
                <Link to="/increase">Increase</Link>
              </li>
            </ul>
          </nav>

          {/* A <Switch> looks through its children <Route>s and
              renders the first one that matches the current URL. */}
          <Switch>
            <Route path="/get">
              <Get />
            </Route>
            <Route path="/increase">
              <Increase />
            </Route>
          </Switch>
        </div>
      </Router>
    </>
  );
}

export default App;
