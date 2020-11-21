import React, { useState, useEffect } from "react";
import Button from "@material-ui/core/Button";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogTitle from "@material-ui/core/DialogTitle";
import PropTypes from "prop-types";
import { CopyToClipboard } from "react-copy-to-clipboard";
import { makeStyles } from "@material-ui/core/styles";
import { useDispatch } from "react-redux";
import API_URL, {urlBase} from "../../constants";
import { alertError, alertSuccess } from "../../redux/actions";

const useStyles = makeStyles(() => ({
    link: {
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
    },
}));
const DialogStartGame = ({ open, handleClose, quizid, quizStatus }) => {
    const dispatch = useDispatch();
    const classes = useStyles();
    const [sessionId, setSessionId] = useState("");

    const handleOnCopy = () => {
        dispatch(alertSuccess("Copy Success"));
    };

    useEffect(() => {
    // only run fetch when open is set from false to true and quiz is not
    // currently active
        if (open === true) {
            if (quizStatus === null) {
                fetch(`${API_URL}/admin/quiz/${quizid}/start`, {
                    method: "POST",
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
                    },
                })
                    .then((res) => {
                        if (res.ok) {
                            return Promise.resolve(res.json());
                        }
                        return Promise.resolve(res.json()).then((data) => {
                            return Promise.reject(data.error);
                        });
                    })

                    .then(
                        () => {
                            dispatch(alertSuccess("Start Game Success"));
                            // if start game successful should get the session id

                            fetch(`${API_URL}/admin/quiz/${quizid}`, {
                                method: "GET",
                                headers: {
                                    Authorization: `Bearer ${localStorage.getItem(
                                        "accessToken"
                                    )}`,
                                },
                            })
                                .then((res) => res.json())
                                .then((data) => {
                                    setSessionId(data.active);
                                });
                        },
                        (error) => {
                            dispatch(alertError(error));
                        }
                    )
                    .catch((error) => {
                        dispatch(alertError(error.message));
                    });
            } else {
                // quiz is already active
                fetch(`${API_URL}/admin/quiz/${quizid}`, {
                    method: "GET",
                    headers: {
                        Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
                    },
                })
                    .then((res) => res.json())
                    .then((data) => {
                        setSessionId(data.active);
                    });
            }
        }
    }, [quizid, dispatch, quizStatus, open]);

    return (
        <Dialog
            open={open}
            onClose={handleClose}
            aria-labelledby="form-dialog-title"
            fullWidth
            maxWidth="sm"
        >
            <DialogTitle id="form-dialog-title">Join Game</DialogTitle>
            <DialogContent>
                <DialogContentText>Copy the link to join the game</DialogContentText>
                <div className={classes.link}>
                    <div>{sessionId}</div>
                    <CopyToClipboard text={`${urlBase}/game/join/${sessionId}`} onCopy={handleOnCopy}>
                        <button type="button" style={{ height: "30px" }}>
              Copy to Clipboard
                        </button>
                    </CopyToClipboard>
                </div>
            </DialogContent>
            <DialogActions>
                <Button onClick={handleClose} color="primary">
          Cancel
                </Button>
            </DialogActions>
        </Dialog>
    );
};
DialogStartGame.propTypes = {
    open: PropTypes.bool.isRequired,
    handleClose: PropTypes.func.isRequired,
    quizid: PropTypes.number.isRequired,
    quizStatus: PropTypes.oneOfType([PropTypes.number, PropTypes.bool]),
};

DialogStartGame.defaultProps = {
    quizStatus: null,
};

export default DialogStartGame;
