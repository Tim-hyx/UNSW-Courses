import React,{useEffect, useMemo, useState} from 'react';
import PropTypes from "prop-types";
import Dialog from "@material-ui/core/Dialog";
import DialogContent from "@material-ui/core/DialogContent";
import DialogTitle from "@material-ui/core/DialogTitle";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogActions from "@material-ui/core/DialogActions";
import Button from "@material-ui/core/Button";
import {useDropzone} from 'react-dropzone';
import API_URL from '../../constants';

const baseStyle = {
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    padding: '20px',
    borderWidth: 2,
    borderRadius: 2,
    borderColor: '#eeeeee',
    borderStyle: 'dashed',
    backgroundColor: '#fafafa',
    color: '#bdbdbd',
    outline: 'none',
    transition: 'border .24s ease-in-out'
};
  
const activeStyle = {
    borderColor: '#2196f3'
};
  
const acceptStyle = {
    borderColor: '#00e676'
};
  
const rejectStyle = {
    borderColor: '#ff1744'
};
  
const FormDialogJsonTemplate = ({ open, handleClose, id }) => {

    const [jsonFile,setJsonFile] = useState(null);
    // accept only json file
    const {
        acceptedFiles,
        getRootProps,
        getInputProps,
        isDragActive,
        isDragAccept,
        isDragReject
	  } = useDropzone({
        accept: '.json'
	  });
	
	  const style = useMemo(() => ({
        ...baseStyle,
        ...(isDragActive ? activeStyle : {}),
        ...(isDragAccept ? acceptStyle : {}),
        ...(isDragReject ? rejectStyle : {})
	  }), [
        isDragActive,
        isDragReject,
        isDragAccept
	  ]);
	
	  const files = acceptedFiles.map(file => (
        <li key={file.path}>
		  {file.path} - {file.size} bytes
        </li>
	  ));
	  
	  
	  
    const handleEdit = ()=>{
        // contain array of question
        const {questions,thumbnail,createdAt} = jsonFile;

        const validQuestions = questions.map(question=>{
            // this is used as a validtor
            // if the field is not presert in the question
            // when destructe, it will have value null
            const { questionId,
                questionBody,
                answers,
                type,
                timeLimit,
                worthOfPoints,
                image} = question;

            return { questionId,
                questionBody,
                answers,
                type,
                timeLimit,
                worthOfPoints,
                image};
        });

        fetch(`${API_URL}/admin/quiz/${id}`,{
            method: "PUT",
            headers: {
                Accept: "application/json",
                "Content-Type": "application/json",
                Authorization: `Bearer ${localStorage.getItem("accessToken")}`,
            },
            body: JSON.stringify({
                questions: validQuestions,
                thumbnail,
                createdAt
            }),
        
        })  
            .then((res) => console.log(res.status))
            .then(() => {
                handleClose();
            });
    };

    useEffect(()=>{
        if(acceptedFiles[0]){
            const jsonFileLocal = acceptedFiles[0];
            const fileReader = new FileReader();
            fileReader.onload = (event)=>{
                setJsonFile(JSON.parse(event.target.result));
            }
            fileReader.readAsText(jsonFileLocal);
        }

       
    }, [acceptedFiles]);

    return (
        <Dialog
            open={open}
            onClose={handleClose}
            aria-labelledby="form-dialog-title"
            fullWidth
            maxWidth="sm"
        >
            <DialogTitle>Json Template</DialogTitle>
            <DialogContent>
                <DialogContentText>
				Fill the Quiz with Json Template
                </DialogContentText>
                <section className="container">
                    <div {...getRootProps({style})}>
                        <input {...getInputProps()} />
                        <p>Upload a json file</p>
                    </div>
                    <aside>
                        <h4>Files</h4>
                        <ul>{files}</ul>
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


FormDialogJsonTemplate.propTypes = {
    open: PropTypes.bool.isRequired,
    handleClose: PropTypes.func.isRequired,
    id: PropTypes.number.isRequired
};


export default FormDialogJsonTemplate;