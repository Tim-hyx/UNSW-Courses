import data from "./config.json";

const API_URL = `http://localhost:${data.BACKEND_PORT}`;

// the answerId is required in custom.js
export const newAnswer = (answerId,answerBody, isRightOne) => ({
    answerId,
    answerBody,
    isRightOne,
});

// the definition of how to create a question
// answers is a list of object created by newAnswer method
export const newQuestion = (
    questionId,
    questionBody,
    answers,
    type,
    timeLimit,
    worthOfPoints,
    image
) => ({
    questionId,
    questionBody,
    answers,
    type,
    timeLimit,
    worthOfPoints,
    image,
});

export const playerData = (playerName, playerScore)=>({
    playerName,
    playerScore
});


// get the base url of app is running on include the port number
const urlFull = window.location.href;
const urlSplit = urlFull.split("/");
export const urlBase = `${urlSplit[0]  }//${  urlSplit[2]}`

export default API_URL;
