import React from "react";

const Dashboard = () => {
    const [number, setNumber] = React.useState(3);
    const handleclick = () => {
        fetch('http://cgi.cse.unsw.edu.au/~cs6080/20T3/data/score.json')
            .then((res) => res.json())
            .then((data) => setNumber(data.score))
    }

    return (
        <div style={{textAlign: 'center', marginTop: '15%'}}>
            <div style={{color: 'red', fontSize: '2em'}}>Please choose an option from the navbar.</div>
            <div>Game won: {number} <span><button onClick={handleclick}>reset</button></span></div>
        </div>
    )
}
export default Dashboard;