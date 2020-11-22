import logo from './logo.svg';
import './App.css';
import Cat from './pages/Cat';
import Dog from './pages/Dog';
import Mink from './pages/Mink';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";

function App() {
  return (
    <Router>
      <Link to="/cat">Cat</Link>&nbsp;
      <Link to="/dog">Dog</Link>&nbsp;
      <Link to="/mink">Mink</Link>
      <Switch>
        <Route path="/cat">
          <Cat />
        </Route>
        <Route path="/dog/:quizid">
          <Dog name="spot" />
        </Route>
        <Route path="/dog">
          <Dog name="spot" />
        </Route>
        <Route path="/mink">
          <Mink />
        </Route>
      </Switch>
    </Router>
  );
}

export default App;
