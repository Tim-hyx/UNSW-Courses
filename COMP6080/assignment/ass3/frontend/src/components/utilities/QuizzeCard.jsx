import React, { useState, useEffect, useCallback } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardMedia from "@material-ui/core/CardMedia";
import CardContent from "@material-ui/core/CardContent";
import Avatar from "@material-ui/core/Avatar";
import IconButton from "@material-ui/core/IconButton";
import Typography from "@material-ui/core/Typography";
import { red } from "@material-ui/core/colors";
import MoreVertIcon from "@material-ui/icons/MoreVert";
import PropTypes from "prop-types";
import Menu from "@material-ui/core/Menu";
import MenuItem from "@material-ui/core/MenuItem";
import { useHistory } from "react-router-dom";
import Button from "@material-ui/core/Button";
import { useDispatch } from "react-redux";
import API_URL from "../../constants";
import FormDialogUpdateQuiz from "../dialog/FormDialogUpdateQuiz";
import DialogStartGame from "../dialog/DialogStartGame";
import { alertError, alertSuccess } from "../../redux/actions";
import FormDialogJsonTemplate from "../dialog/FormDialogJsonTemplate";

const useStyles = makeStyles((theme) => ({
    root: {
        flexGrow: 1,
    },
    media: {
        height: 0,
        paddingTop: "56.25%", // 16:9
    },
    expand: {
        transform: "rotate(0deg)",
        marginLeft: "auto",
        transition: theme.transitions.create("transform", {
            duration: theme.transitions.duration.shortest,
        }),
    },
    expandOpen: {
        transform: "rotate(180deg)",
    },
    avatar: {
        backgroundColor: red[500],
    },
    butContainer: {
        display: "flex",
        justifyContent: "flex-end",
    },
    but: {
        margin: "10px 5px 0px",
    },
}));

const QuizzeCard = ({ id, name, createdAt, thumbnail, setEdit }) => {
    const classes = useStyles();
    const dispatch = useDispatch();
    const history = useHistory();
    const [quiz, setQuiz] = useState({ questions: [], active: false });
    // the original data formal is not standard format ususlly seen convert it to standard
    const dataFormated = new Date(createdAt);
    const [anchorEl, setAnchorEl] = useState(null);
    const [gameDialog, setGameDialog] = useState(false);
    const [editLocal, setEditLocal] = useState(false);
    const [editQ,setEditQ] = useState(false);
    const [templateDialog, setTemplateDialog] = useState(false);
    const [endGame, setEndGame] = useState(false);
    useEffect(() => {
        fetch(`${API_URL}/admin/quiz/${id}`, {
            method: "GET",
            headers: {
                Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
            },
        })
            .then(res=>res.json())
            .then(data=>setQuiz(data));
    }, [id, gameDialog, endGame,editQ]);

    const handleClick = (event) => {
        setAnchorEl(event.currentTarget);
    };
    const handleClose = () => {
        setAnchorEl(null);
    };
    const handleEditClose = () => {
        // toogle the edit global state vairlbe because the user may edit multiple times
        setEdit((prevState) => !prevState);
        setEditLocal(false);
    };
    const handleEditOpen = () => {
        setEditLocal(true);
    };

    const handleTemplateDialogClose = () => {
        setEditQ((prevState) => !prevState);
        setTemplateDialog(false);
      
    };

    const handleTemplateDialogOpen = () => {
        setTemplateDialog(true);
    };

    const handeEditQuizze = () => {
        handleClose();
        handleEditOpen();
    };

    const handleEditQuestion = () => {
        handleClose();
        history.push(`/dashboard/${id}`);
    };

    const handleDelete = () => {
        fetch(`${API_URL}/admin/quiz/${id}`, {
            method: "DELETE",
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
                    dispatch(alertSuccess("Delete Success"));
                    handleClose();
                    setEdit((prevState) => !prevState);
                },

                (error) => {
                    dispatch(alertError(error));
                }
            );
    };

    const handleShowClipBoard = () => {
        setGameDialog(true);
        handleClose();
    };

    const handleShowGameProgression = () => {
        handleClose();
        history.push(`/game/progression/${id}/${quiz.active}`);
    };

    const handeJsonTemplate = () => {
        handleClose();
        handleTemplateDialogOpen();
    };
    const renderMenu = (
        <Menu
            id="simple-menu"
            anchorEl={anchorEl}
            keepMounted
            open={Boolean(anchorEl)}
            onClose={handleClose}
        >
            {quiz.active && (
                <MenuItem onClick={handleShowClipBoard}>Show ClipBoard</MenuItem>
            )}
            {quiz.active && (
                <MenuItem onClick={handleShowGameProgression}>
          Show Game Progression
                </MenuItem>
            )}
            <MenuItem onClick={handeJsonTemplate}>Json Template</MenuItem>
            <MenuItem onClick={handeEditQuizze}>Edit Quizze</MenuItem>
            <MenuItem onClick={handleEditQuestion}>Edit Question</MenuItem>
            <MenuItem onClick={handleDelete}>Delete</MenuItem>
        </Menu>
    );

    // the content of this button depend on whether the quiz is active or not
    // if do a normal condition render here will have same problem
    // the button will apear after fetch in the rerender
    // there will be an annoying animation each time
    // useCallback help us memorize the value
    const changeQuizStatusButton = useCallback(() => {
        const handleStartGame = () => {
            // display the clipboard for user to copy the url used for joining the game
            setGameDialog(true);
        };
        const handleEndGame = () => {
            fetch(`${API_URL}/admin/quiz/${id}/end`, {
                method: "POST",
                headers: {
                    Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
                },
            }).then((res) => {
                console.log(res.status);
                setEndGame((prevState) => !prevState);
            });
        };
        if (quiz.active === false) {
            // component hasn't mount
            return null;
        }
        if (quiz.active === null) {
            // quiz is not active, we can start a game
            return (
                <Button
                    variant="contained"
                    color="primary"
                    onClick={handleStartGame}
                    className={classes.but}
                >
          Start Session
                </Button>
            );
        }

        return (
            <Button
                variant="contained"
                color="secondary"
                onClick={handleEndGame}
                className={classes.but}
            >
        Stop Session
            </Button>
        );
    }, [classes.but, id, quiz.active]);

    return (
        <div>
            <Card className={classes.root}>
                <CardHeader
                    avatar={
                        <Avatar aria-label="recipe" className={classes.avatar}>
              R
                        </Avatar>
                    }
                    action={
                        <IconButton aria-label="settings" onClick={handleClick}>
                            <MoreVertIcon />
                        </IconButton>
                    }
                    title={name}
                    subheader={dataFormated.toDateString()}
                />

                <CardMedia
                    className={classes.media}
                    image={thumbnail ?? `${process.env.PUBLIC_URL}/trump.jpg`}
                    title="Paella dish"
                />

                <CardContent>
                    <Typography variant="body2" color="textSecondary" component="p">
            This question&apos;s id is {id}, it has {quiz.questions.length}{" "}
            questions.
                    </Typography>
                    <div className={classes.butContainer}>{changeQuizStatusButton()}</div>
                </CardContent>
            </Card>
            {renderMenu}
            <FormDialogUpdateQuiz
                open={editLocal}
                handleClose={handleEditClose}
                id={id}
            />
            <DialogStartGame
                open={gameDialog}
                handleClose={() => {
                    setGameDialog(false);
                }}
                quizid={id}
                quizStatus={quiz.active}
            />
            <FormDialogJsonTemplate
                open={templateDialog}
                handleClose={handleTemplateDialogClose}
                id={id}
            />
        </div>
    );
};

QuizzeCard.propTypes = {
    id: PropTypes.number.isRequired,
    name: PropTypes.string.isRequired,
    createdAt: PropTypes.string.isRequired,
    thumbnail: PropTypes.string,
    setEdit: PropTypes.func.isRequired,
};

QuizzeCard.defaultProps = {
    thumbnail: null,
};
export default QuizzeCard;
