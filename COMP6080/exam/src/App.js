import './App.css';
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import Naviation from "./pages/naviationbar";
import Dashboard from "./pages/dashboard";
import Blanko from "./pages/Blanko";
import Slido from "./pages/Slido";
import Tetro from "./pages/Tetro";

const App = () => {
    const footerstyle = {
        height: '50px',
        width: '100%',
        backgroundColor: '#999999',
        marginTop: '20%'
    }

    return (
        <div>
            <Router>
                <Naviation/>
                <Switch>
                    <Route exact path='/'>
                        <Dashboard/>
                    </Route>
                    <Route exact path='/Blanko'>
                        <Blanko/>
                    </Route>
                    <Route exact path='/Slido'>
                        <Slido/>
                    </Route>
                    <Route exact path='/Tetro'>
                        <Tetro/>
                    </Route>
                </Switch>
                <footer style={footerstyle}></footer>
            </Router>
        </div>
    )
}


export default App;
