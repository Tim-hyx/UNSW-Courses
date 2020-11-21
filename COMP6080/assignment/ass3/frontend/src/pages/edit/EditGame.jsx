import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Grid from "@material-ui/core/Grid";
import { makeStyles } from "@material-ui/core/styles";
import Button from "@material-ui/core/Button";
import uuid from "react-uuid";
import API_URL from "../../constants";
import FormDialogAddQuestion from "../../components/dialog/FormDialogAddQuestion";
import QuestionEditCard from "../../components/utilities/QuestionEditCard";

const useStyles = makeStyles(() => ({
    root: {
        flexGrow: 1,
    },
    girdContainer: {
        width: "100%",
        display: "flex",
        justifyContent: "center",
        margin: "80px 0px 0px",
        padding: "0px 150px",
    },
}));
const EditGame = () => {
    const classes = useStyles();
    // extract the quizId from url path
    const { quizId } = useParams();

    const [quizze, setQuizze] = useState({ questions: [] });
    const [open, setOpen] = useState(false);
    const [toogle, setToogle] = useState(false);

    const handleClickOpen = () => {
        setOpen(true);
    };
    const handleClose = () => {
        setOpen(false);
    };

    useEffect(() => {
        // TODO handle 403 error case
        fetch(`${API_URL}/admin/quiz/${quizId}`, {
            method: "GET",
            headers: {
                Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
            },
        })
            .then((res) => res.json())
            .then((data) => {
                setQuizze(data);
            });
    }, [quizId, open, toogle]);


    return (
        <div className={classes.root}>
            <Grid container spacing={4} className={classes.girdContainer}>
                <Grid container item xs={12} spacing={5}>
                    <Grid item container xs={12} alignItems="center" justify="flex-end">
                        <Button
                            variant="contained"
                            color="primary"
                            onClick={handleClickOpen}
                        >
                            Add A NEW QUESTION
                        </Button>
                    </Grid>
                </Grid>
                <Grid container item xs={12} spacing={2}>
                    {quizze.questions.map((question) => {
                        return (
                            <Grid item xs={12} key={uuid()}>
                                <QuestionEditCard
                                    question={question}
                                    quizId={quizId}
                                    setToogle={setToogle}
                                />
                            </Grid>
                        );
                    })}
                </Grid>
            </Grid>
            <FormDialogAddQuestion
                open={open}
                handleClose={handleClose}
                id={quizId}
            />
        </div>
    );
};

export default EditGame;
