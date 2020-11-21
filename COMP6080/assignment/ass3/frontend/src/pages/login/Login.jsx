import React, {useState} from "react";
import {makeStyles} from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";
import Button from "@material-ui/core/Button";
import InputAdornment from "@material-ui/core/InputAdornment";
import EmailIcon from "@material-ui/icons/Email";
import LockIcon from "@material-ui/icons/Lock";
import {useDispatch} from "react-redux";
import {useHistory} from "react-router-dom";
import {login} from "../../redux/actions";

const useStyles = makeStyles(() => ({
    root: {
        // 64px is the height of navbar
        height: "calc(100vh - 64px)",
        justifyContent: "center",
        alignItems: "center",
    },
    form: {
        display: "flex",
        flexDirection: "column",
        maxWidth: 400,
        minWidth: 300,
    },
}));
const Login = () => {
    const [email, setEmail] = useState();
    const [password, setPassword] = useState();
    const classes = useStyles();
    const dispatch = useDispatch();
    const history = useHistory();
    return (
        <Grid container className={classes.root}>
            <form
                className={classes.form}
                onSubmit={(e) => {
                    e.preventDefault();
                    dispatch(login(email, password));
                    history.push("/dashboard");
                }}
            >
                <TextField
                    label="Email"
                    type="email"
                    margin="normal"
                    required
                    InputProps={{
                        startAdornment: (
                            <InputAdornment position="start">
                                <EmailIcon/>
                            </InputAdornment>
                        ),
                    }}
                    onChange={(event) => setEmail(event.target.value)}
                />
                <TextField
                    label="Password"
                    margin="normal"
                    type="password"
                    required
                    InputProps={{
                        startAdornment: (
                            <InputAdornment position="start">
                                <LockIcon/>
                            </InputAdornment>
                        ),
                    }}
                    onChange={(event) => setPassword(event.target.value)}
                />
                <div style={{height: 20}}/>
                <Button color="primary" variant="contained" type="submit">
                    Log in
                </Button>
            </form>
        </Grid>
    );
};

export default Login;
