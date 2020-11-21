import React, { useEffect, useState } from "react";
import { useParams, useHistory } from "react-router-dom";
import Grid from "@material-ui/core/Grid";
import { makeStyles } from "@material-ui/core/styles";
import Chip from "@material-ui/core/Chip";
import Checkbox from "@material-ui/core/Checkbox";
import Typography from "@material-ui/core/Typography";
import { CountdownCircleTimer } from "react-countdown-circle-timer";
import moment from "moment";
import { useDispatch } from "react-redux";
import API_URL from "../../constants";
import { alertError, alertSuccess } from "../../redux/actions";


/* eslint-disable no-eval */
let gamePollingInterval = null;
let questionPollingInterval = null;
let answerTimeOut = null;
let questionEndTimeOut = null;

const useStyles = makeStyles((theme) => ({
    appBar: {
        position: "relative",
    },
    title: {
        marginLeft: theme.spacing(2),
        flex: 1,
    },
    girdContainer: {
        width: "100%",
        minHeight: "calc(100vh - 64px)",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        backgroundColor: "#f2f2f2",
        [theme.breakpoints.down("sm")]: {
            padding: "70px 20px 0px",
            flexWrap: "nowrap",
        },
        [theme.breakpoints.up("md")]: {
            padding: "20px 40px 0px",
        },
        [theme.breakpoints.up("lg")]: {
            padding: "80px 150px 0px",
        },
    },
    formControl: {
        margin: theme.spacing(1),
        minWidth: 120,
    },
    head: {
        flex: 1,
    },
    headWrapper: {
        display: "flex",
        justifyContent: "center",
    },
    body: {
        flex: 4,
    },
    foot: {
        flex: 2,
    },

    left: {
        padding: "40px 40px",
        alignItems: "center",
    },
    right: {
        margin: "0px 0px 40px",
        border: "2px dashed rgb(204, 204, 204)",
    },
    imageContainer: {
        height: "85%",
    },
    imageFrame: {
        display: "inline-flex",
        borderRadius: 2,
        border: "1px solid #eaeaea",
        margin: 10,
        padding: 4,
        boxSizing: "border-box",

        [theme.breakpoints.down("sm")]: {
            maxWidth: 220,
            maxHeight: 370,
        },
        [theme.breakpoints.up("md")]: {
            maxWidth: 240,
            maxHeight: 370,
        },
        [theme.breakpoints.up("lg")]: {
            maxWidth: 300,
            maxHeight: 370,
        },
    },
    imageFrameInner: {
        display: "flex",
        minWidth: 0,
        overflow: "hidden",
    },
    image: {
        width: "100%",
        height: "100%",
    },
    choice: {
        width: "100%",
        margin: 8,
        display: "flex",
        justifyContent: "space-around",
        alignItems: "center",
    },
    choice1: {
        backgroundColor: "#e21b3c",
    },
    choice2: {
        backgroundColor: "#1368ce",
    },
    choice3: {
        backgroundColor: "#d89e00",
    },
    choice4: {
        backgroundColor: "#26890c",
    },
    inputText: {
        color: "white",
    },
    upload: {
        margin: 12,
    },
    placeHolder: {
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        fontSize: "1.5em",
    },
    backdrop: {
        zIndex: theme.zIndex.drawer + 1,
        color: "#fff",
    },

    timer: {
        fontFamily: "Montserrat",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
    },
    text: {
        color: "#aaa",
    },
    value: {
        fontSize: "40px",
    },
    showAnswer: {
        justifyContent: "center",
        alignItems: "flex-start",
    },
    textstyle: {
        fontSize: '50px',
        textAlign: 'center',
        marginTop: '20%'
    }
}));

const GamePlay = () => {
    const { playerId } = useParams();
    const classes = useStyles();
    const history = useHistory();
    const dispatch = useDispatch();

    // gameStatus is one of { game not started, question started, question end, game end }
    const [gameStatus, setGameStatus] = useState({
        current: "game not started",
        prev: "",
    });

    const [key, setKey] = useState(0);
    const [checked0, setChecked0] = useState(false);
    const [checked1, setChecked1] = useState(false);
    const [checked2, setChecked2] = useState(false);
    const [checked3, setChecked3] = useState(false);
    // this is used as a toogle to trigger rerender in useEffect
    const [checkBoxClicked, setCheckBoxClicked] = useState(false);

    const [disabled0, setDisabled0] = useState(false);
    const [disabled1, setDisabled1] = useState(false);

    const [disabled2, setDisabled2] = useState(false);
    const [disabled3, setDisabled3] = useState(false);

    const [remainTime, setRemainTime] = useState(0);


    const [questionCurrent, setQuestionCurrent] = useState({
        questionBody: "",
        answers: [
            { answerBody: "" },
            { answerBody: "" },
            { answerBody: "" },
            { answerBody: "" },
        ],
        timeLimit: 0,
    });
    const handleChangeCheckBox0 = (event) => {
        setChecked0(event.target.checked);
        setCheckBoxClicked((prevValue) => !prevValue);
    };
    const handleChangeCheckBox1 = (event) => {
        setChecked1(event.target.checked);
        setCheckBoxClicked((prevValue) => !prevValue);
    };
    const handleChangeCheckBox2 = (event) => {
        setChecked2(event.target.checked);
        setCheckBoxClicked((prevValue) => !prevValue);
    };
    const handleChangeCheckBox3 = (event) => {
        setChecked3(event.target.checked);
        setCheckBoxClicked((prevValue) => !prevValue);
    };

    const renderTime = ({ remainingTime }) => {
        if (remainingTime === 0) {
            return <div className={classes.timer}>Too lale...</div>;
        }

        return (
            <div className={classes.timer}>
                <div className={classes.text}>Remaining</div>
                <div className={classes.value}>{remainingTime}</div>
                <div className={classes.text}>seconds</div>
            </div>
        );
    };

    useEffect(() => {
        // using polling to get the ongoing game status
        const getGameStutus = () => {
            console.log("game not started, pooling");
            fetch(`${API_URL}/play/${playerId}/status`, {
                method: "GET",
            })
                .then((res) => res.json())
                .then((data) => {
                    if (data.started === true) {
                        // check if the qestion is active
                        setGameStatus((prevState) => ({
                            current: "question started",
                            prev: prevState.current,
                        }));
                    } else {
                        setGameStatus((prevState) => ({
                            current: "game not started",
                            prev: prevState.current,
                        }));

                    }
                });
        };
        const getQuestion = () => {
            fetch(`${API_URL}/play/${playerId}/question`, {
                method: "GET",
            })
                .then((res) => {
                    if (res.ok) {
                        return Promise.resolve(res.json());
                    }
                    return Promise.resolve(res.json()).then(data => {
                        return Promise.reject(data.error);
                    });
                })

                .then((data) => {
                    const { question } = data;
                    console.log("quesaiotyn", question);
                    const previousQestionId = localStorage.getItem(playerId);

                    // no question is current active, fetch one from api
                    if (
                        previousQestionId === null ||
                        previousQestionId !== question.questionId
                    ) {

                        const { isoTimeLastQuestionStarted, ...rest } = question;

                        setQuestionCurrent(rest);

                        // need a way to perserve the time remaining value between user refresh page
                        // i used real time calculation, so no matter how you refrest the page
                        // the time remain is presist
                        const now = moment(new Date());
                        const questionStart = moment(isoTimeLastQuestionStarted);
                        const questionEnd = questionStart.add(rest.timeLimit, "seconds");

                        const diffInSeconds = moment
                            .duration(questionEnd.diff(now))
                            .asSeconds();
                        if (diffInSeconds > 0) {
                            setRemainTime(diffInSeconds);
                            // reset the coutdown based on real time value
                            setKey((prevKey) => prevKey + 1);
                            // should set a setTimeout api call when the countdown reach 0
                            console.log("remain", diffInSeconds);

                            // note the (diffInSeconds - 1) * 1000
                            // there is a small delay due to code need time to excute
                            // i am asuming that in my machine its less than 1 sec
                            // so submit the answer 1 sec early

                            answerTimeOut = setTimeout(() => {
                                // get the id of user selected choice

                                const answerIds = [];

                                for (let i = 0; i < 4; i += 1) {
                                    if (eval(`checked${i}`) === true) {
                                        answerIds.push(rest.answers[i].answerId);
                                    }
                                }
                                console.log("answerIds", answerIds);
                                fetch(`${API_URL}/play/${playerId}/answer`, {
                                    method: "PUT",
                                    headers: {
                                        "Content-Type": "application/json",
                                    },
                                    body: JSON.stringify({ answerIds }),
                                })
                                    .then((res) => {
                                        if (res.ok) {
                                            return Promise.resolve(res.json());
                                        }
                                        return Promise.resolve(res.json()).then((data2) => {
                                            return Promise.reject(data2.error);
                                        });
                                    })
                                    .then(
                                        () => {
                                            dispatch(alertSuccess("Answer Submit Success"));
                                        },
                                        (error) => {
                                            dispatch(alertError(error));
                                        }
                                    );
                            }, (diffInSeconds - 1) * 1000);

                            // use a timeout to end the question
                            questionEndTimeOut = setTimeout(() => {
                                // preserve the questionId in localStorage
                                // it is just indicate current quesion is active
                                localStorage.setItem(playerId, question.questionId);
                                setChecked0(false);
                                setChecked1(false);
                                setChecked2(false);
                                setChecked3(false);
                                setGameStatus((prevState) => ({
                                    current: "question end",
                                    prev: prevState.current,
                                }));
                            }, (diffInSeconds + 1) * 1000);
                        }
                    }
                    if (
                        previousQestionId !== null &&
                        previousQestionId !== question.questionId
                    ) {
                        // case where a new question is fetched from api
                        // stop pulling question from server
                        clearInterval(questionPollingInterval);
                        questionPollingInterval = null;

                        // invalid the item in localstorage
                        if (localStorage.getItem(playerId) !== null) {
                            localStorage.removeItem(playerId);
                        }
                        setGameStatus((prevState) => ({
                            current: "question started",
                            prev: prevState.current,
                        }));
                    }

                    // case where user wait admin to advance to next question
                    if (
                        previousQestionId !== null &&
                        previousQestionId === question.questionId
                    ) {
                        // keep pooling

                        if (gameStatus.current !== "question end") {
                            setGameStatus((prevState) => ({
                                current: "question end",
                                prev: prevState.current,
                            }));
                        }
                    }
                }, (error) => {
                    console.log(error, "game should end");
                    setGameStatus((prevState) => ({
                        current: "game end",
                        prev: prevState.current,
                    }));

                    // fetch the game result
                    fetch(`${API_URL}/play/${playerId}/results`, {
                        method: "GET",
                    })
                        .then((res) => res.json())
                        .then((data) => {
                            console.log(data)

                            let right = 0;

                            for (let i = 0; i < data.length; i += 1) {
                                if (data[i].correct === true) {
                                    right += 1;
                                }
                            }
                            const wrong = data.length - right;
                            history.push(`/game/play/results/${playerId}/${right}/${wrong}`);
                        })
                });
        };

        const getAnswers = () => {
            // question already end
            // but react setState don't presisit between refresh
            // need to do a fetch call here to get the data from
            // the question just ended
            fetch(`${API_URL}/play/${playerId}/question`, {
                method: "GET",
            })
                .then((res) => res.json())

                .then((data) => {
                    const { question } = data;
                    setQuestionCurrent(question);
                    fetch(`${API_URL}/play/${playerId}/answer`, {
                        method: "GET",
                    })
                        .then((res) => res.json())
                        .then((data2) => {
                            // console.log(data2.answerIds);
                            // diable all checkboxs
                            setDisabled0(true);
                            setDisabled1(true);
                            setDisabled2(true);
                            setDisabled3(true);

                            console.log("all the answr id", question.answers);
                            console.log("correct answerid", data2.answerIds);
                            question.answers.forEach((answer, index) => {

                                if (data2.answerIds.includes(answer.answerId)) {
                                    eval(`setChecked${index}(true)`);
                                }
                            });
                        });
                });
        };

        // if game is not start, keep pooling
        // if game start, stop pooling and get question, page should work correctly
        // even if user refresh the page
        // if counterdown end, should wait admin to advance to next question

        if (gameStatus.current === "game not started") {
            getGameStutus();
            // point of declare pollingTimeout as a global object is
            // making sure there are only one pooling function get runned
            // avoid multiple copy of pooling give server too much preasure
            if (!gamePollingInterval) {
                gamePollingInterval = setInterval(() => getGameStutus(), 1000);
            }
        } else if (gameStatus.current === "question started") {
            getQuestion();

            if (gameStatus.prev === "question end") {
                // reset all the checkbox
                setChecked0(false);
                setChecked1(false);
                setChecked2(false);
                setChecked3(false);

                // make sure this only get runned once
                setGameStatus((prevState) => ({
                    current: "question started",
                    prev: prevState.current,
                }));

            }
        } else if (gameStatus.current === "question end") {
            // do a pooling to get next question
            if (!questionPollingInterval) {
                questionPollingInterval = setInterval(() => {
                    getQuestion();
                }, 1000);
            }

            // show current question answers
            console.log("fukc", gameStatus);
            getAnswers();
        } else {
            // game end
            console.log("should be game end");
        }
        return () => {
            // when component unmounted, stop pooling
            clearInterval(gamePollingInterval);
            clearTimeout(answerTimeOut);
            clearTimeout(questionEndTimeOut);
            clearInterval(questionPollingInterval);
            // do below when quiz end
            // localStorage.removeItem(`${playerId}${questionCurrent.questionId}`);
            gamePollingInterval = null;
            answerTimeOut = null;
            questionEndTimeOut = null;
            questionPollingInterval = null;
        };
    }, [playerId, gameStatus, checkBoxClicked, dispatch, history]);


    // condition render base on gameStatus
    let pageContent = null;

    if (gameStatus.current === "game not started") {
        pageContent = <div className={classes.textstyle}>Game not started yet</div>;
    } else if (gameStatus.current === "question end") {
        pageContent = (

            <Grid container className={classes.girdContainer} spacing={2}>
                <Grid container item xs={12} className={classes.head}>
                    <Grid item container xs={12} className={classes.headWrapper}>
                        <Typography variant="h3" gutterBottom>
                            Wait admin to advance to next question
                        </Typography>
                    </Grid>
                </Grid>
                <Grid container item xs={12} className={classes.body}>
                    <Grid
                        item
                        container
                        xs={12}
                        sm={12}
                        md={12}
                        className={classes.right}
                    >
                        <Grid
                            container
                            item
                            xs={12}
                            className={classes.imageContainer}
                            justify="center"
                            alignItems="center"
                        >
                            <div className={classes.imageFrameInner}>
                                <div className={classes.imageFrame}>
                                    <img
                                        src={questionCurrent.image}
                                        alt="question"
                                        className={classes.image}
                                    />
                                </div>
                            </div>
                        </Grid>
                    </Grid>
                    <Grid item md={2} />
                </Grid>
                <Grid container item xs={12} className={classes.foot}>
                    <Grid
                        container
                        item
                        xs={12}
                        spacing={1}
                        className={classes.showAnswer}
                    >
                        <Typography variant="h5" gutterBottom>
                            Correct Answers Shown Bellow
                        </Typography>
                    </Grid>
                    <Grid container item xs={12} spacing={1}>
                        <Grid container item xs={12} sm={12} md={12} lg={6}>
                            <div className={`${classes.choice} ${classes.choice1}`}>
                                <Typography variant="button" display="block" gutterBottom>
                                    {questionCurrent.answers[0].answerBody}
                                </Typography>
                                <Checkbox
                                    checked={checked0}
                                    onChange={handleChangeCheckBox0}
                                    inputProps={{ "aria-label": "primary checkbox" }}
                                    inputstyle={{ color: "white" }}
                                    style={{ color: "white" }}
                                    disabled={disabled0}
                                />
                            </div>
                        </Grid>
                        <Grid container item xs={12} sm={12} md={12} lg={6}>
                            <div className={`${classes.choice} ${classes.choice2}`}>
                                <Typography variant="button" display="block" gutterBottom>
                                    {questionCurrent.answers[1].answerBody}
                                </Typography>
                                <Checkbox
                                    checked={checked1}
                                    onChange={handleChangeCheckBox1}
                                    inputProps={{ "aria-label": "primary checkbox" }}
                                    inputstyle={{ color: "white" }}
                                    style={{ color: "white" }}
                                    disabled={disabled1}
                                />
                            </div>
                        </Grid>
                    </Grid>
                    <Grid container item xs={12} spacing={1}>
                        <Grid container item xs={12} sm={12} md={12} lg={6}>
                            <div className={`${classes.choice} ${classes.choice3}`}>
                                <Typography variant="button" display="block" gutterBottom>
                                    {questionCurrent.answers[2].answerBody}
                                </Typography>
                                <Checkbox
                                    checked={checked2}
                                    onChange={handleChangeCheckBox2}
                                    inputProps={{ "aria-label": "primary checkbox" }}
                                    inputstyle={{ color: "white" }}
                                    style={{ color: "white" }}
                                    disabled={disabled2}
                                />
                            </div>
                        </Grid>
                        <Grid container item xs={12} sm={12} md={12} lg={6}>
                            <div className={`${classes.choice} ${classes.choice4}`}>
                                <Typography variant="button" display="block" gutterBottom>
                                    {questionCurrent.answers[3].answerBody}
                                </Typography>
                                <Checkbox
                                    checked={checked3}
                                    onChange={handleChangeCheckBox3}
                                    inputProps={{ "aria-label": "primary checkbox" }}
                                    inputstyle={{ color: "white" }}
                                    style={{ color: "white" }}
                                    disabled={disabled3}
                                />
                            </div>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>
        );
    } else if (gameStatus.current === "question started") {
        pageContent = (
            <Grid container className={classes.girdContainer} spacing={2}>
                <Grid container item xs={12} className={classes.head}>
                    <Grid item container xs={12} className={classes.headWrapper}>
                        <Typography variant="h3" gutterBottom>
                            {questionCurrent.questionBody}
                        </Typography>
                    </Grid>
                </Grid>
                <Grid container item xs={12} className={classes.body}>
                    <Grid item container xs={12} sm={4} md={4} className={classes.left}>
                        <Grid item xs={12} container justify="center" alignContent="center">
                            <CountdownCircleTimer
                                onComplete={() => {
                                    // should to some api call
                                    console.log("end");
                                }}
                                isPlaying
                                key={key}
                                duration={questionCurrent.timeLimit}
                                initialRemainingTime={remainTime}
                                colors={[
                                    ["#004777", 0.33],
                                    ["#F7B801", 0.33],
                                    ["#A30000", 0.33],
                                ]}
                            >
                                {renderTime}
                            </CountdownCircleTimer>
                        </Grid>
                        <Grid item xs={12} container justify="center" alignContent="center">
                            <Typography variant="body1" gutterBottom>
                                {questionCurrent.worthOfPoints} points
                            </Typography>
                        </Grid>
                        <Grid item xs={12} container justify="center" alignContent="center">
                            <Chip label={questionCurrent.type} />
                        </Grid>
                    </Grid>

                    <Grid item container xs={12} sm={8} md={6} className={classes.right}>
                        <Grid
                            container
                            item
                            xs={12}
                            className={classes.imageContainer}
                            justify="center"
                            alignItems="center"
                        >
                            <div className={classes.imageFrameInner}>
                                <div className={classes.imageFrame}>
                                    <img
                                        src={questionCurrent.image}
                                        alt="question"
                                        className={classes.image}
                                    />
                                </div>
                            </div>
                        </Grid>
                    </Grid>
                    <Grid item md={2} />
                </Grid>
                <Grid container item xs={12} className={classes.foot}>
                    <Grid container item xs={12} spacing={1}>
                        <Grid container item xs={12} sm={12} md={12} lg={6}>
                            <div className={`${classes.choice} ${classes.choice1}`}>
                                <Typography variant="button" display="block" gutterBottom>
                                    {questionCurrent.answers[0].answerBody}
                                </Typography>
                                <Checkbox
                                    checked={checked0}
                                    onChange={handleChangeCheckBox0}
                                    inputProps={{ "aria-label": "primary checkbox" }}
                                    inputstyle={{ color: "white" }}
                                    style={{ color: "white" }}
                                />
                            </div>
                        </Grid>
                        <Grid container item xs={12} sm={12} md={12} lg={6}>
                            <div className={`${classes.choice} ${classes.choice2}`}>
                                <Typography variant="button" display="block" gutterBottom>
                                    {questionCurrent.answers[1].answerBody}
                                </Typography>
                                <Checkbox
                                    checked={checked1}
                                    onChange={handleChangeCheckBox1}
                                    inputProps={{ "aria-label": "primary checkbox" }}
                                    inputstyle={{ color: "white" }}
                                    style={{ color: "white" }}
                                />
                            </div>
                        </Grid>
                    </Grid>
                    <Grid container item xs={12} spacing={1}>
                        <Grid container item xs={12} sm={12} md={12} lg={6}>
                            <div className={`${classes.choice} ${classes.choice3}`}>
                                <Typography variant="button" display="block" gutterBottom>
                                    {questionCurrent.answers[2].answerBody}
                                </Typography>
                                <Checkbox
                                    checked={checked2}
                                    onChange={handleChangeCheckBox2}
                                    inputProps={{ "aria-label": "primary checkbox" }}
                                    inputstyle={{ color: "white" }}
                                    style={{ color: "white" }}
                                />
                            </div>
                        </Grid>
                        <Grid container item xs={12} sm={12} md={12} lg={6}>
                            <div className={`${classes.choice} ${classes.choice4}`}>
                                <Typography variant="button" display="block" gutterBottom>
                                    {questionCurrent.answers[3].answerBody}
                                </Typography>
                                <Checkbox
                                    checked={checked3}
                                    onChange={handleChangeCheckBox3}
                                    inputProps={{ "aria-label": "primary checkbox" }}
                                    inputstyle={{ color: "white" }}
                                    style={{ color: "white" }}
                                />
                            </div>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>
        );
    } else {
        console.log("really shoukd not get here");
    }
    return pageContent;
};

export default GamePlay;
