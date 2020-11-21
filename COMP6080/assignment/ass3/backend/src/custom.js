/*
 For a given data structure of a question, produce another
 object that doesn't contain any important meta data (e.g. the answer)
 to return to a "player"
*/
export const quizQuestionPublicReturn = question => {
  const { answers, } = question;
  const answesrPublic = answers.map(({ isRightOne, ...keepAttrs }) => keepAttrs);
  return { ...question, answers: answesrPublic, };
};

/*
 For a given data structure of a question, get the IDs of
 the correct answers (minimum 1).
*/
export const quizQuestionGetCorrectAnswers = question => {
  const { answers, } = question;
  const answersRight = answers.filter(answer => answer.isRightOne === true);
  //   console.log('anwer corrent id ', answersRight.map(answer => answer.answerId));
  return answersRight.map(answer => answer.answerId);
};

/*
 For a given data structure of a question, get the IDs of
 all of the answers, correct or incorrect.
*/
export const quizQuestionGetAnswers = question => {
  const { answers, } = question;
  return answers.map(answer => answer.answerId);
};

/*
 For a given data structure of a question, get the duration
 of the question once it starts. (Seconds)
*/
export const quizQuestionGetDuration = question => {
  return question.timeLimit;
};
