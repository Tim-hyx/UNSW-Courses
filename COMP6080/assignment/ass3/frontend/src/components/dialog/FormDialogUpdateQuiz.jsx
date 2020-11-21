import React, { useState, useEffect } from "react";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogTitle from "@material-ui/core/DialogTitle";
import PropTypes from "prop-types";
import { useDropzone } from "react-dropzone";
import Typography from '@material-ui/core/Typography';
import styled from 'styled-components';
import API_URL from "../../constants";

const Container = styled.div`
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  border-width: 2px;
  border-radius: 2px;
  border-color: #eeeeee;
  border-style: dashed;
  background-color: #fafafa;
  color: #bdbdbd;
  outline: none;
  transition: border .24s ease-in-out;
`;


const FormDialogUpdateQuiz = ({ open, handleClose, id }) => {
    // add button should call backend api, stub for now

    const [name, setName] = useState("");
    const [image, setImage] = useState(null);
    const [imageData, setImageData] = useState();

    const handleEdit = () => {

        fetch(`${API_URL}/admin/quiz/${id}`, {
            method: "GET",
            headers: {
                Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
            },
        })
            .then((res) => res.json())
            .then((data) => {

                fetch(`${API_URL}/admin/quiz/${id}`, {
                    method: "PUT",
                    headers: {
                        Accept: "application/json",
                        "Content-Type": "application/json",
                        Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
                    },
                    body: JSON.stringify({
                        ...data,
                        name,
                        thumbnail: imageData
                    })
                })
                    .then((res) => console.log(res.status))
                    .then(() => {
                        handleClose();
                    });
            });

    };

    const {
        acceptedFiles,
        getRootProps,
        getInputProps,
    } = useDropzone({
        accept: "image/jpeg, image/png",
        noDrag: true,
    });

    useEffect(() => {
        if (acceptedFiles[0]) {
            const imageLocal = acceptedFiles[0];
            setImage(imageLocal);
            const reader = new FileReader();
            reader.onloadend = () => {
                setImageData(reader.result);
            };

            reader.readAsDataURL(imageLocal);
        }

    }, [acceptedFiles]);

    const handleKeyDown = (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            handleEdit();
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
            <DialogTitle id="form-dialog-title">Edit Quizze</DialogTitle>
            <DialogContent>
                <DialogContentText>
                    Change the title of the created quizze
                </DialogContentText>
                <TextField
                    onKeyDown={handleKeyDown}
                    autoFocus
                    margin="dense"
                    label="Quizze Name"
                    type="text"
                    fullWidth
                    value={name}
                    onChange={(e) => {
                        setName(e.target.value);
                    }}
                />
                <div style={{ height: "30px" }} />
                <DialogContentText>
                    Change the thumbnail of created quizze
                </DialogContentText>
                <div style={{ height: "20px" }} />
                <section className="container">
                    <Container {...getRootProps({ className: 'dropzone' })}>
                        <input {...getInputProps()} />
                        <Typography variant="body2" gutterBottom>
                            Click to select an image
                        </Typography>
                        <Typography variant="body2" gutterBottom>
                            <em>(Only *.jpeg and *.png images will be accepted)</em>
                        </Typography>
                    </Container>
                    <aside>
                        <h4>Accepted files</h4>
                        <ul>{
                            image === null ?
                                "No image has been uploaded yet" :
                                <li key={image.path}>
                                    {image.path} - {image.size} bytes
							  </li>
                        }</ul>

                    </aside>
                </section>
            </DialogContent>
            <DialogActions>
                <Button onClick={handleClose} color="primary">
                    Cancel
                </Button>
                <Button onClick={handleEdit} color="primary">
                    Add
                </Button>
            </DialogActions>
        </Dialog>
    );
};

FormDialogUpdateQuiz.propTypes = {
    open: PropTypes.bool.isRequired,
    handleClose: PropTypes.func.isRequired,
    id: PropTypes.number.isRequired
};

export default FormDialogUpdateQuiz;
