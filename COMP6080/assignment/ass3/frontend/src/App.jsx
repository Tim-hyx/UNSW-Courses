import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { useSelector } from "react-redux";
import Login from "./pages/login/Login";
import Signup from "./pages/signup/Signup";
import NavigationBar from "./components/navbar/NavigationBar";
import CustomizedSnackbars from "./components/utilities/Alert";
import Dashboard from "./pages/home/Dashboard";
import EditGame from "./pages/edit/EditGame";
import EditGameQuestion from "./pages/edit/EditGameQuestion";
import GameProgression from './pages/game-progression/GameProgression';
import GameJoin from './pages/game-user/GameJoin';
import GamePlay from './pages/game-user/GamePlay';
import GameResult from './pages/game-user/GameResult';

const App = () => {
    const alert = useSelector((state) => state.alert);

    return (
        <div>
            {alert.message && (
                <CustomizedSnackbars type={alert.type} message={alert.message} />
            )}
            <Router>
                <NavigationBar />
                <Switch>
                    <Route exact path="/login">
                        <Login />
                    </Route>
                    <Route exact path="/signup">
                        <Signup />
                    </Route>
                    <Route exact path="/dashboard/:quizId">
                        <EditGame />
                    </Route>
                    <Route exact path="/dashboard/:quizId/:questionId">
                        <EditGameQuestion />
                    </Route>
                    <Route exact path="/game/join/:sessionId"> 
                        <GameJoin/>
                    </Route>
                    <Route exact path="/game/play/:playerId"> 
                        <GamePlay/>
                    </Route>
                    <Route exact path="/game/progression/:quizId/:sessionId"> 
                        <GameProgression/>
                    </Route>
                    <Route exact path="/game/play/results/:playerId/:right/:wrong"> 
                        <GameResult/>
                    </Route>
                    <Route path="/">
                        <Dashboard />
                    </Route>
                </Switch>
            </Router>
        </div>
    );
};

export default App;
