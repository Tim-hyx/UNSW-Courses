import React, {useState} from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogTitle from "@material-ui/core/DialogTitle";
import PropTypes from "prop-types";
import {useDispatch} from "react-redux";
import API_URL from "../../constants";
import {alertError, alertSuccess} from "../../redux/actions";

const FormDialogAddQuiz = ({open, handleClose}) => {
    // add button should call backend api, stub for now

    const [name, setName] = useState("");
    const dispatch = useDispatch();


    const handleAdd = () => {
        fetch(`${API_URL}/admin/quiz/new`, {
            method: "POST",
            body: JSON.stringify({name}),
            headers: {
                Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
                Accept: "application/json",
                "Content-Type": "application/json",
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
                    dispatch(alertSuccess("Create Quizz Success"));
                    handleClose();
                },
                (error) => {
                    dispatch(alertError(error));
                }
            ).catch((error) => {
                dispatch(alertError(error.message));
            });

    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            handleAdd();
        }
    }

    return (
        <Dialog
            open={open}
            onClose={handleClose}
            aria-labelledby="form-dialog-title"
            fullWidth
            maxWidth="sm"
        >
            <DialogTitle id="form-dialog-title">Add a new quizze</DialogTitle>
            <DialogContent>
                <DialogContentText>
                    To add to this new quizze, please enter the name
                </DialogContentText>
                <TextField
                    onKeyDown={handleKeyDown}
                    autoFocus
                    margin="dense"
                    id="name"
                    label="Quizze Name"
                    type="text"
                    fullWidth
                    value={name}
                    onChange={(e) => {
                        setName(e.target.value);
                    }}
                />
            </DialogContent>
            <DialogActions>
                <Button onClick={handleClose} color="primary">
                    Cancel
                </Button>
                <Button onClick={handleAdd} color="primary">
                    Add
                </Button>
            </DialogActions>
        </Dialog>
    );
};

FormDialogAddQuiz.propTypes = {
    open: PropTypes.bool.isRequired,
    handleClose: PropTypes.func.isRequired,
};

export default FormDialogAddQuiz;
