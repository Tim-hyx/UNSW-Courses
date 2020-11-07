import React from 'react';
import './App.css';
import Button from '@material-ui/core/Button';
import Input from "@material-ui/core/Input";


function App() {

    const [name, setName] = React.useState([]);
    const [allNames, setAllNames] = React.useState([]);

    const submitInfo = () => {
        setAllNames([...allNames, name]);
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            submitInfo();
        }
    }

    return (
        <div>
            <div className="header">
                <div id="nav-bar">
                    <h3 className="nav-item">Home</h3>
                    <h3 className="nav-item">About</h3>
                    <h3 className="nav-item">Pricing</h3>
                    <h3 className="nav-item">Partners</h3>
                    <h3 className="nav-item">Contact</h3>
                </div>
            </div>
            <div className="main">
                <div style={{fontSize: '20px', fontWeight: 'bold'}}>First name: <Input
                    placeholder={'Enter your first name'} inputProps={{'aria-label': 'description'}} type="text"
                    name="first-name"
                    value={name}
                    onChange={e => setName(e.target.value)}
                    tabIndex={0}
                    onKeyDown={handleKeyDown}/></div>
                <br/>
                {allNames.map((n, idx) => (
                    <div style={{width: '50px', height: '50px', display: 'inline-block'}}>{n}</div>
                ))}
                <Button variant="contained" color="primary" style={{marginTop: '20px', width: '70px', height: '30px'}}
                        id="form-submit"
                        onClick={submitInfo}>Submit
                </Button>
            </div>
            <div className="footer">
                &copy; Giant Apple 2020
            </div>
        </div>
    );
}

export default App;
