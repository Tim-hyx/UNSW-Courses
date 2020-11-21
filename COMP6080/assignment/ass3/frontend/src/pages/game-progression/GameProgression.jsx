import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Button from "@material-ui/core/Button";
import { useDispatch } from "react-redux";
import { CountdownCircleTimer } from "react-countdown-circle-timer";
import { makeStyles } from "@material-ui/core/styles";
import moment from "moment";
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import uuid from 'react-uuid'
import { LineChart, CartesianGrid, XAxis, YAxis, Tooltip, Legend, Line } from "recharts";
import { alertError, alertSuccess } from "../../redux/actions";
import API_URL, { playerData } from "../../constants";


const useStyles = makeStyles(() => ({
    timer: {
        fontFamily: "Montserrat",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        fontSize: "30px",
    },
    text: {
        color: "#aaa",
        fontSize: "25px",
    },
    value: {
        fontSize: "40px",
    },
    id: {
        fontSize: "30px",
        textAlign: "center",
        marginTop: "5%",
        marginBottom: "2%",
    },
    end: {
        fontSize: "50px",
        textAlign: "center",
        marginTop: "10%",
    },
    page: {
        display: "flex",
        flexDirection: "column"
    },
    chart: {
        width: "100%",
        minHeight: 300,
        display: "flex",
        alignItems: "center",
        justifyContent: "center"
    },
    tb: {

        maxWidth: 500
    }
}));

const GameProgression = () => {
    const { quizId, sessionId } = useParams();
    const dispatch = useDispatch();
    const classes = useStyles();

    // -2 is an impossible value for fetch to return
    // this is set to default value
    const [timeLimitCurrent, setTimeLimitCurrent] = useState(1000);
    const [position, setPosition] = useState(-2);
    const [gameLength, setGameLength] = useState(-1);
    const [key, setKey] = useState(0);
    const [remainTime, setRemainTime] = useState(1000);
    const [advanceDisabled, setAdvanceDisabled] = useState(true);
    const [result, setResult] = useState([{ answers: [{correct:false}] }]);
    const [mark, setMark] = useState();

    useEffect(() => {
        fetch(`${API_URL}/admin/session/${sessionId}/status`, {
            method: "GET",
            headers: {
                Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
            },
        })
            .then((res) => res.json())
            .then((data) => {
                const { results } = data;
                console.log("in fetch", results);
                // could access gameStatus attribute to get posotion and length
                // create extra state varible just to make the code more
                // readable to myself

                setPosition(results.position);
                setGameLength(results.questions.length);
                if (
                    results.position !== -1 &&
                    results.position !== results.questions.length
                ) {
                    const now = moment(new Date());
                    const questionStart = moment(results.isoTimeLastQuestionStarted);
                    const questionEnd = questionStart.add(
                        results.questions[results.position].timeLimit,
                        "seconds"
                    );

                    const diffInSeconds = moment
                        .duration(questionEnd.diff(now))
                        .asSeconds();

                    if (diffInSeconds > 0) {
                        setRemainTime(diffInSeconds);
                        setTimeLimitCurrent(results.questions[results.position].timeLimit);
                        setKey((prevKey) => prevKey + 1);
                    } else {
                        // if already pass the time limit
                        // enable the advance button
                        // and set the countdown to the stop stage
                        setRemainTime(0);
                        setTimeLimitCurrent(0);
                        setAdvanceDisabled(false);
                        setKey((prevKey) => prevKey + 1);
                    }
                }

                if (results.position === results.questions.length) {
                    fetch(`${API_URL}/admin/session/${sessionId}/results`, {
                        method: "GET",
                        headers: {
                            Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
                        },
                    })
                        .then((res) => res.json())
                        .then((data2) => {
                            setMark(results);
                            setResult(data2.results);
                        });
                }
            });
    }, [sessionId, position]);

    const handleAdvanceGame = () => {
        // api with error handling
        fetch(`${API_URL}/admin/quiz/${quizId}/advance`, {
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
                    dispatch(alertSuccess("Advance Sucess"));
                    setAdvanceDisabled(true);
                    setPosition((prevPosition) => prevPosition + 1);
                },
                (error) => {
                    dispatch(alertError(error));
                }
            );
    };

    const renderTime = ({ remainingTime }) => {
        if (remainingTime === 0) {
            return <div className={classes.timer}>Too late...</div>;
        }

        return (
            <div className={classes.timer}>
                <div className={classes.text}>Remaining</div>
                <div className={classes.value}>{remainingTime}</div>
                <div className={classes.text}>seconds</div>
            </div>
        );
    };


    let pageContent;
    if (position === -2) {
        return null;
    }
    if (position === -1) {
        pageContent = (
            <Button color="primary" variant="contained" onClick={handleAdvanceGame}>
                Start The Game
            </Button>
        );
        // use setTimeout to get the answer then refresh the page by changing state varible
    } else if (position === gameLength) {
        // didn't end now, end with a timeout
        // when game end show final result

        const scoreList = [];
        for (let i = 0; i < result.length; i += 1) {
            let grade = 0;
            for (let j = 0; j < result[i].answers.length; j += 1) {
                if (result[i].answers[j].correct === true) {
                    grade += mark.questions[j].worthOfPoints;
                }
            }
            scoreList.push(grade);
        }

        const rightList = []
        const timeList = []
        for (let n = 0; n < result[0].answers.length; n += 1) {
            let right = 0;
            let quesitionTime = 0
            for (let j = 0; j < result.length; j += 1) {

                if (result[j].answers[n].correct === true) {
                    right += 1;
                }

                const answerAt = moment(result[j].answers[n].answeredAt);
                const questionStart = moment(result[j].answers[n].questionStartedAt);
                const diff = moment.duration(answerAt.diff(questionStart)).asSeconds();
                quesitionTime += diff;

            }
            const rigthRate = right / result[0].answers.length
            const average = quesitionTime / result[0].answers.length
            rightList.push(rigthRate);
            timeList.push(average);
        }
        const data = [];
        for (let i = 0; i < rightList.length; i += 1) {
            const fill = {
                'name': i + 1,
                'question number': rightList[i]
            }
            data.push(fill);
        }
        const data2 = [];
        for (let i = 0; i < timeList.length; i += 1) {
            const fill = {
                'name': i + 1,
                'question number': timeList[i]
            }
            data2.push(fill);
        }

        const playDataList = [];
        for (let n = 0; n < scoreList.length; n += 1) {
            playDataList.push(playerData(result[n].name, scoreList[n]));
        }
        playDataList.sort((a, b) => {
            return b.playerScore - a.playerScore;
        });

        const arr = [];
        for (let i = 0; i < playDataList.length; i += 1) {
            const body = (
                <TableRow key={uuid()}>
                    <TableCell>{playDataList[i].playerName}</TableCell>
                    <TableCell>{playDataList[i].playerScore}</TableCell>
                </TableRow>
            );

            arr.push(body);
        }

        pageContent = (

            <div className={classes.page}>
                <div>Top 5 Users and Scores </div>
                <div className={classes.chart}>
                    <TableContainer component={Paper} className={classes.tb}>
                        <Table aria-label="simple table">
                            <TableHead>
                                <TableRow>
                                    <TableCell>player name</TableCell>
                                    <TableCell>player score</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {arr}
                            </TableBody>
                        </Table>
                    </TableContainer>
                </div>
                <div>Percentages of each question </div>
                <div className={classes.chart}>
                    <LineChart width={600} height={250} data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="name" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Line type="monotone" dataKey="question number" stroke="#8884d8" />
                    </LineChart>
                </div>
                <div>Average time of each question </div>
                <div className={classes.chart}>
                    <LineChart width={600} height={250} data={data2} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="name" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Line type="monotone" dataKey="question number" stroke="#8884d8" />
                    </LineChart>
                </div>
            </div>
        );

    } else {
        // should be a countdown timer here
        pageContent = (
            <>
                <div style={{ display: "flex" }}>
                    <div style={{ margin: "auto" }}>
                        <CountdownCircleTimer
                            onComplete={() => {
                                // should to some api call
                                console.log("end");
                                setAdvanceDisabled(false);
                            }}
                            isPlaying
                            key={key}
                            duration={timeLimitCurrent}
                            initialRemainingTime={remainTime}
                            colors={[
                                ["#004777", 0.33],
                                ["#F7B801", 0.33],
                                ["#A30000", 0.33],
                            ]}
                        >
                            {renderTime}
                        </CountdownCircleTimer>
                    </div>
                </div>
                <Button
                    style={{ marginTop: "5%" }}
                    color="primary"
                    onClick={handleAdvanceGame}
                    variant="contained"
                    disabled={advanceDisabled}
                >
                    Advance
                </Button>
            </>
        );
    }

    return (
        <>
            <div className={classes.id}>sessionId:{sessionId}</div>
            <div style={{ fontSize: "20px", textAlign: "center" }}>{pageContent}</div>
        </>
    );
};

export default GameProgression;
