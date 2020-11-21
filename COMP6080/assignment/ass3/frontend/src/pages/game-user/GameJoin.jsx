import React, { useState } from "react";
import { useParams, useHistory } from "react-router-dom";
import { makeStyles } from "@material-ui/core/styles";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import { useDispatch } from "react-redux";
import API_URL from "../../constants";
import { alertError, alertSuccess } from "../../redux/actions";

const useStyles = makeStyles(() => ({
    root: {
        flexGrow: 1,
        height: "calc(100vh - 64px)",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
    },

    form: {
        display: "flex",
        flexDirection: "column",
        width: 250,
    },
}));

// this page should allow the user to enter their name and redirect them to play page
const GameJoin = () => {
    const { sessionId } = useParams();
    const classes = useStyles();
    const history = useHistory();
    const dispatch = useDispatch();

    const [name, setName] = useState('');
    const handleSubmit = (e) => {
        e.preventDefault();
        // api call to join the game
        fetch(`${API_URL}/play/join/${sessionId}`, {

            method: "POST",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ name })
        }).then((res) => {
            if (res.ok) {
                return Promise.resolve(res.json());
            }
            return Promise.resolve(res.json()).then(data => {
                return Promise.reject(data.error);
            });
        })
            .then(data => {
                dispatch(alertSuccess("Join Game Success"));
                history.push(`/game/play/${data.playerId}`);
            }, (error) => {
                dispatch(alertError(error));
            });

    };

    return (
        <div className={classes.root}>
            <form className={classes.form} onSubmit={handleSubmit}>
                <TextField label="Enter your player name"
                    required
                    onChange={(event) => setName(event.target.value)}
                />
                <div style={{ height: 20 }} />
                <Button color="primary" variant="contained" type="submit">
                    Submit
                </Button>
            </form>
        </div>
    );
};

export default GameJoin;
