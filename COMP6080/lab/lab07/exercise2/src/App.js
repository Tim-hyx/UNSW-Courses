import React from "react";
import Card from "./Card";
import "./App.css";

let timeout = null;

function App() {
  const [value, setValue] = React.useState("");
  const [content, setContent] = React.useState();

  React.useEffect(() => {
    if (value === "") {
      return;
    }
    clearTimeout(timeout);
    timeout = setTimeout(() => {
      let nameList = value.split(",");
      Promise.all(
        nameList.map((name) =>
          fetch(`https://api.github.com/users/${name}`).then((res) =>
            res.json()
          )
        )
      ).then((data) => {
        let allCards = data.map((cardData, index) => Card(cardData, index));
        setContent(allCards);
      });
    }, 500);
  }, [value]);

  const onChangeHandler = (e) => {
    setValue(e.target.value);
  };

  return (
    <div>
      <input type="text" value={value} onChange={onChangeHandler} />
      <div>{content}</div>
    </div>
  );
}

export default App;
