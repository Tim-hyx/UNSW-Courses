import React, { useState } from "react";
import MuiAlert from "@material-ui/lab/Alert";
import Snackbar from "@material-ui/core/Snackbar";
import PropTypes from "prop-types";
import { useDispatch } from "react-redux";
import useIsMounted from 'ismounted';
import { alertClear } from "../../redux/actions";

const CustomizedSnackbars = ({ type, message }) => {
    const dispatch = useDispatch();
    const [open, setOpen] = useState(true);
    const isMounted = useIsMounted();

    const handleClose = (_event, reason) => {
        if (reason === "clickaway") {
            return;
        }
        dispatch(alertClear());
        if(isMounted.current){
            // if component hasn't yet mount, call setState will cause error
            setOpen(false);
        }
    };

    return (
        <Snackbar
            open={open}
            autoHideDuration={6000}
            onClose={handleClose}
            anchorOrigin={{
                vertical: "top",
                horizontal: "center",
            }}
        >
            <MuiAlert
                elevation={6}
                variant="filled"
                onClose={handleClose}
                severity={type}
            >
                {message}
            </MuiAlert>
        </Snackbar>
    );
};

CustomizedSnackbars.propTypes = {
    type: PropTypes.string.isRequired,
    message: PropTypes.string.isRequired,
};

export default CustomizedSnackbars;
