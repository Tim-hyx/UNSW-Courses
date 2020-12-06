import React, {useEffect} from 'react';
import {makeStyles} from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import IconButton from '@material-ui/core/IconButton';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import FormDialogAddQuiz from "./FormEditQuiz";
import MediaCard from "./quizcard";


class Clock extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            date: new Date()
        };
    }

    componentDidMount() {
        this.timerID = setInterval(
            () => this.setState({
                date: new Date()
            }),
            1000
        );
    }

    componentWillUnmount() {
        clearInterval(this.timerID);
    }

    render() {
        return (
            <span>{this.state.date.toLocaleString()} </span>
        );
    }
}

function App() {
    const useStyles = makeStyles((theme) => ({
        root: {
            flexGrow: 1,
        },
        menuButton: {
            marginRight: theme.spacing(2),
        },
        title: {
            flexGrow: 1,
        },
        footer: {
            marginTop: '10%',
            marginRight: '5%',
            textAlign: 'right'
        },
    }));
    const classes = useStyles();
    const [open, setOpen] = React.useState(false);
    const handleClickOpen = () => {
        setOpen(true);
    };
    const handleClose = () => {
        setOpen(false);
    };
    const cardlist = [];

    cardlist.push(<MediaCard name={localStorage.getItem('name')} img={localStorage.getItem('thumbnail')}/>);

    console.log(cardlist)

    return (
        <div className={classes.root}>
            <AppBar position="static">
                <Toolbar>
                    <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
                    </IconButton>
                    <Typography variant="h6" className={classes.title}>
                        BigBrain
                    </Typography>
                    <Button color="inherit" onClick={handleClickOpen} style={{width: '100px', height: '50px'}}>Create
                        Quiz</Button>
                    <Button color="inherit" onClick={handleClickOpen}>Logout</Button>
                </Toolbar>
            </AppBar>
            <footer>
                <div className={classes.footer}><Clock/> &copy; BigBrain</div>
            </footer>
            <Dialog
                open={open}
                onClose={handleClose}
                aria-labelledby="alert-dialog-title"
                aria-describedby="alert-dialog-description"
            >
                <DialogContent>
                    <DialogContentText id="alert-dialog-description">
                        Do you want to log out from BigBrain?
                    </DialogContentText>
                </DialogContent>
                <DialogActions>
                    <Button color="primary">
                        Continue
                    </Button>
                    <Button onClick={handleClose} color="primary" autoFocus>
                        Cancel
                    </Button>
                </DialogActions>
            </Dialog>
            <FormDialogAddQuiz open={open} handleClose={handleClose}/>
            {cardlist}
        </div>
    );
}

export default App;
