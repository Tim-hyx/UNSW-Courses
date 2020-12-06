import React from "react";
import {strs} from "../data/blanko";

const Blanko = () => {
    const containerlist = [];
    const [value,setValue]=React.useState('');

    for (let i = 0; i < 12; i++) {
        containerlist.push(<div
            style={{
                width: '50px',
                height: '50px',
                border: 'solid',
                textAlign: 'center',
                lineHeight: '50px',
                fontSize: '40px',
            }}>{value}</div>)
    }

    return (
        <div style={{
            width: '1000px',
            height: '100px',
            float: 'left',
            display: 'flex',
            marginTop: '10%',
            marginLeft: '30%'
        }}>
            {containerlist}
        </div>
    )
}
export default Blanko;