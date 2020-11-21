import React, { useState, useEffect } from "react";
import { useParams, useHistory } from "react-router-dom";
import Button from "@material-ui/core/Button";
import PanoramaOutlinedIcon from "@material-ui/icons/PanoramaOutlined";
import Typography from "@material-ui/core/Typography";
import Grid from "@material-ui/core/Grid";
import TextField from "@material-ui/core/TextField";
import MenuItem from "@material-ui/core/MenuItem";
import Select from "@material-ui/core/Select";
import FormControl from "@material-ui/core/FormControl";
import Slider from "@material-ui/core/Slider";
import Checkbox from "@material-ui/core/Checkbox";
import FormLabel from "@material-ui/core/FormLabel";
import { makeStyles } from "@material-ui/core/styles";
import { useDispatch } from "react-redux";
import { alertError, alertSuccess } from "../../redux/actions";



import API_URL from "../../constants";

/* eslint-disable no-eval */

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
    imageIcon: {
        width: 100,
        height: 100,
        color: "rgb(101, 105, 105)",
    },
    choice: {
        width: "100%",
        margin: 8,
        display: "flex",
        justifyContent: "space-around",
        alignItems: "center",
    },
    choice1: {
        backgroundColor: (props) => (props.answer1 ? "#e21b3c" : "#ffffff"),
    },
    choice2: {
        backgroundColor: (props) => (props.answer2 ? "#1368ce" : "#ffffff"),
    },
    choice3: {
        backgroundColor: (props) => (props.answer3 ? "#d89e00" : "#ffffff"),
    },
    choice4: {
        backgroundColor: (props) => (props.answer4 ? "#26890c" : "#ffffff"),
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
    butSet: {
        display: "flex",
        justifyContent: "flex-end",
        alignItems: "center"
    },
}));

const EditGameQuestion = () => {
    const { quizId, questionId } = useParams();
    const history = useHistory();
    const dispatch = useDispatch();
    const [title, setTitle] = useState("");
    const [answer1, setAnswer1] = useState("");
    const [answer2, setAnswer2] = useState("");
    const [answer3, setAnswer3] = useState("");
    const [answer4, setAnswer4] = useState("");
    const [points, setPoints] = useState(1000);
    const [timeLimit, setTimeLimit] = useState("");
    const [checked1, setChecked1] = useState(false);
    const [checked2, setChecked2] = useState(false);
    const [checked3, setChecked3] = useState(false);
    const [checked4, setChecked4] = useState(false);

    const [upload, setUpload] = useState({ imagePreviewUrl: "" });

    const classes = useStyles({ answer1, answer2, answer3, answer4 });

    const handleChangeCheckBox1 = (event) => {
        setChecked1(event.target.checked);
    };
    const handleChangeCheckBox2 = (event) => {
        setChecked2(event.target.checked);

    };
    const handleChangeCheckBox3 = (event) => {
        setChecked3(event.target.checked);

    };
    const handleChangeCheckBox4 = (event) => {
        setChecked4(event.target.checked);

    };

    const handleChange = (event) => {
        setTimeLimit(event.target.value);
    };
    const valuetext = (value) => {
        return value;
    };


    let imagePlaceHolder;

    if (upload.imagePreviewUrl) {
        imagePlaceHolder = (
            <div className={classes.imageFrameInner}>
                <div className={classes.imageFrame}>
                    <img
                        src={upload.imagePreviewUrl}
                        alt="upload"
                        className={classes.image}
                    />
                </div>
            </div>
        );
    } else {
        imagePlaceHolder = (
            <div className={classes.placeHolder}>
                <PanoramaOutlinedIcon className={classes.imageIcon} />
                <div style={{ height: "20px" }} />
                <Typography variant="body1" gutterBottom>
                    <span>Preview Uploaded Image Here</span>
                </Typography>
            </div>
        );
    }

    const handleImageChange = (e) => {
        e.preventDefault();

        const reader = new FileReader();
        const file = e.target.files[0];

        reader.onloadend = () => {
            setUpload({
                imagePreviewUrl: reader.result,
            });
        };

        reader.readAsDataURL(file);
    };

    const handleCancel = () => {
        history.push(`/dashboard/${quizId}`);
    };

    const handleSubmit = () => {
        if (!(answer1 && answer2 && answer3 && answer4)) {
            dispatch(alertError("Please Fill In All Answers"));
            return;
        }
        if (!title) {
            dispatch(alertError("Please Fill in Title"));
            return;
        }
        if (!timeLimit) {
            dispatch(alertError("Please Set Time Limit"));
            return;
        }
        if (!upload.imagePreviewUrl) {
            dispatch(alertError("Please Upload An Image"));
            return;
        }

        let atLeastOneAnswer = false;
        for (let i = 1; i <= 4; i += 1) {

            if (eval(`checked${i}`) === true) {
                atLeastOneAnswer = true;
                break;
            }
        }
        if (!atLeastOneAnswer) {
            dispatch(alertError("Please Checked Atleast One Correct Answer"));
            return;
        }

        let cnt = 0;
        let type;
        for (let i = 1; i <= 4; i += 1) {
            if (eval(`checked${i}`) === true) {
                cnt += 1;
            }
        }
        if (cnt > 1) {
            type = "Mutiple Choice";
        } else {
            type = "Single Choice";
        }

        console.log(type);

        // do a fetch call to update the question

        fetch(`${API_URL}/admin/quiz/${quizId}`, {
            method: "GET",
            headers: {
                Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
            },
        })
            .then((res) => res.json())
            .then((data) => {


                console.log(data);
                // const
                const q = data.questions.find(qes => qes.questionId === questionId);
                console.log(q);
                q.answers[0].answerBody = answer1;
                q.answers[1].answerBody = answer2;
                q.answers[2].answerBody = answer3;
                q.answers[3].answerBody = answer4;

                q.answers[0].isRightOne = checked1;
                q.answers[1].isRightOne = checked2;
                q.answers[2].isRightOne = checked3;
                q.answers[3].isRightOne = checked4;
                q.timeLimit = timeLimit;
                q.worthOfPoints = points;
                q.image = upload.imagePreviewUrl;
                q.questionBody = title;


                const { questions } = data;
                const newQuestions = []
                console.log("apple", questions);
                for (let i = 0; i < questions.length; i += 1) {
                    if (questions[i].questionId !== questionId) {
                        newQuestions.push(questions[i]);
                    }
                    else {
                        newQuestions.push(q);
                    }
                }
                console.log("new", newQuestions);

                fetch(`${API_URL}/admin/quiz/${quizId}`, {
                    method: "PUT",
                    headers: {
                        Accept: "application/json",
                        "Content-Type": "application/json",
                        Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
                    },
                    body: JSON.stringify({
                        ...data,
                        questions: newQuestions,
                    }),
                })
                    .then((res) => console.log(res.status))
                    .then(() => {
                        dispatch(alertSuccess("Update Questions Success"));
                        history.push(`/dashboard/${quizId}`);
                    });

            });




    };



    useEffect(() => {


        fetch(`${API_URL}/admin/quiz/${quizId}`, {
            method: "GET",
            headers: {
                Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
            },
        })
            .then((res) => res.json())
            .then((data) => {

                const quesitonData = data.questions.filter((q) => q.questionId === questionId)[0];
                setTitle(quesitonData.questionBody);
                setTimeLimit(quesitonData.timeLimit);
                setUpload({
                    imagePreviewUrl: quesitonData.image
                });

                setAnswer1(quesitonData.answers[0].answerBody);
                setAnswer2(quesitonData.answers[1].answerBody);
                setAnswer3(quesitonData.answers[2].answerBody);
                setAnswer4(quesitonData.answers[3].answerBody);
                setChecked1(quesitonData.answers[0].isRightOne);
                setChecked2(quesitonData.answers[1].isRightOne);
                setChecked3(quesitonData.answers[2].isRightOne);
                setChecked4(quesitonData.answers[3].isRightOne);
                setPoints(quesitonData.worthOfPoints);
                // console.log(quesitonData);
                console.log(data);
            });


    }, [questionId, quizId]);




    return (
        <Grid container className={classes.girdContainer} spacing={2}>
            <Grid container item xs={12} className={classes.head}>
                <Grid item container xs={12} className={classes.butSet}>
                    <Button size="medium" variant="contained" color="secondary" onClick={handleCancel} >
                        Cancel
                    </Button>
                    <div style={{ width: "20px" }} />
                    <Button size="medium" variant="contained" color="primary" onClick={handleSubmit}>
                        Submit
                    </Button>
                </Grid>

                <Grid item container xs={12}>
                    <TextField
                        id="outlined-full-width"
                        label="Start typing your question"
                        style={{ margin: 8 }}
                        placeholder="How many hours did you spend on this assignment?"
                        fullWidth
                        margin="normal"
                        InputLabelProps={{
                            shrink: true,
                        }}
                        variant="outlined"
                        value={title}
                        onChange={(event) => setTitle(event.target.value)}
                        inputProps={{ style: { textAlign: "center" } }}
                    />
                </Grid>
            </Grid>
            <Grid container item xs={12} className={classes.body}>
                <Grid item container xs={12} sm={4} md={4} className={classes.left}>
                    <Grid item xs={12} container justify="center" alignContent="center">
                        <FormControl className={classes.formControl}>
                            <FormLabel>Time Limit</FormLabel>

                            <Select
                                labelId="demo-simple-select-label"
                                id="demo-simple-select"
                                value={timeLimit}
                                onChange={handleChange}
                            >
                                <MenuItem value={10}>10 sec</MenuItem>
                                <MenuItem value={20}>20 sec</MenuItem>
                                <MenuItem value={30}>30 sec</MenuItem>
                            </Select>
                        </FormControl>
                    </Grid>
                    <Grid item xs={12} container justify="center" alignContent="center">
                        <FormControl className={classes.formControl}>
                            <FormLabel>Points</FormLabel>
                            <div style={{ height: 15 }} />
                            <Slider
                                getAriaValueText={valuetext}
                                aria-labelledby="discrete-slider"
                                valueLabelDisplay="auto"
                                step={200}
                                marks
                                min={500}
                                max={2000}
                                onChange={(event, newValue) => {
                                    setPoints(newValue);
                                }}
                                value={points}
                            />
                        </FormControl>
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
                        {imagePlaceHolder}
                    </Grid>
                    <Grid item xs={12} container justify="center" alignItems="center">
                        <label htmlFor="raised-button-file">
                            <input
                                accept="image/*"
                                className={classes.input}
                                style={{ display: "none" }}
                                id="raised-button-file"
                                multiple
                                type="file"
                                onChange={handleImageChange}
                            />

                            <Button
                                variant="contained"
                                component="span"
                                className={classes.button}
                                size="small"
                            >
                                Upload
                            </Button>
                        </label>
                    </Grid>
                </Grid>
                <Grid item md={2} />
            </Grid>
            <Grid container item xs={12} className={classes.foot}>
                <Grid container item xs={12} spacing={1}>
                    <Grid container item xs={12} sm={12} md={12} lg={6}>
                        <div className={`${classes.choice} ${classes.choice1}`}>
                            <TextField
                                className="text"
                                label="Answer1"
                                onChange={(event) => setAnswer1(event.target.value)}
                                InputProps={{
                                    className: classes.inputText,
                                }}
                                value={answer1}
                            />
                            <Checkbox
                                checked={checked1}
                                onChange={handleChangeCheckBox1}
                                inputProps={{ "aria-label": "primary checkbox" }}
                                inputstyle={{ color: "white" }}
                                style={{ color: "white" }}
                            />
                        </div>
                    </Grid>
                    <Grid container item xs={12} sm={12} md={12} lg={6}>
                        <div className={`${classes.choice} ${classes.choice2}`}>
                            <TextField
                                className="text"
                                label="Answer2"
                                onChange={(event) => setAnswer2(event.target.value)}
                                InputProps={{
                                    className: classes.inputText,
                                }}
                                value={answer2}
                            />
                            <Checkbox
                                checked={checked2}
                                onChange={handleChangeCheckBox2}
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
                            <TextField
                                className="text"
                                label="Answer3"
                                onChange={(event) => setAnswer3(event.target.value)}
                                InputProps={{
                                    className: classes.inputText,
                                }}
                                value={answer3}
                            />
                            <Checkbox
                                checked={checked3}
                                onChange={handleChangeCheckBox3}
                                inputProps={{ "aria-label": "primary checkbox" }}
                                inputstyle={{ color: "white" }}
                                style={{ color: "white" }}
                            />
                        </div>
                    </Grid>
                    <Grid container item xs={12} sm={12} md={12} lg={6}>
                        <div className={`${classes.choice} ${classes.choice4}`}>
                            <TextField
                                className="text"
                                label="Answer4"
                                onChange={(event) => setAnswer4(event.target.value)}
                                InputProps={{
                                    className: classes.inputText,
                                }}
                                value={answer4}
                            />
                            <Checkbox
                                checked={checked4}
                                onChange={handleChangeCheckBox4}
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
};

export default EditGameQuestion;
