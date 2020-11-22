import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {

  const [emailList, setEmailList] = React.useState(['','']);

  const updateInput = (event, index) => {
    const newEmailList = [...emailList];
    newEmailList[index] = event.target.value;
    setEmailList(newEmailList);
  };

  const addTwoEmails = () => {
    if (emailList.length <= 9) {
      const newEmailList = [...emailList];
      newEmailList.push('');
      newEmailList.push('');
      setEmailList(newEmailList);
    }
  };

  const name = 'Hayden';

  return (
    <div className="App">
      <h1>Please invite your friends to join CSE</h1>
        {/*<form action="" method="get">*/}
          <div>
            <h3>Welcome message</h3>
            <textarea name="welcomeMessage" id="welcomeMessage"></textarea>
          </div>
          <div id="emailList">
            {emailList.map((email, idx) => (
              <div key={idx}><span>Email Address: </span><input type="text" onChange={event => updateInput(event, idx)} value={emailList[idx]} /></div>
            ))}
          </div>

          {emailList.length <= 9 ? <button onClick={addTwoEmails} id="addMoreEmail">Add More</button> : ''}

          <hr />
          Current Emails:<br />
          {emailList.map((email, idx) => (
            <span key={idx}>{emailList[idx]}, </span>
          ))}
          <input type="submit" value="Invite" />
        {/*</form>*/}
    </div>
  );
}

export default App;
