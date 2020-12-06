import React from "react";

const Tetro = () => {

    let grid = []
    const [img, setImg] = React.useState('');
    for (let i = 0; i < 120; i++) {
        grid.push(<div style={{
            width: '50px',
            height: '50px',
            border: '1px solid #333333 ',
            textAlign: 'center',
            lineHeight: '150px',
            fontSize: '40px',
        }}>{img}</div>)
    }
    return (
        <div>
            <div style={{
                width: '550px',
                height: '300px',
                display: 'flex',
                flexWrap: "wrap",
                margin: '20px 20px 100px 20px'
            }}>{grid}</div>
            <button style={{marginTop: '20%', marginLeft: '10%'}}>reset</button>
        </div>
    )
}
export default Tetro;