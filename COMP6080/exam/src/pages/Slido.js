import React from "react";

const Slido = () => {
    let grid = []
    const [img, setImg] = React.useState('');
    for (let i = 0; i < 9; i++) {
        grid.push(<div style={{
            width: '150px',
            height: '150px',
            border: '1px solid #333',
            textAlign: 'center',
            lineHeight: '150px',
            fontSize: '40px',
        }}>{img}</div>)
    }

    return (
        <div>
            <div style={{
                width: '500px',
                height: '300px',
                display: 'flex',
                flexWrap: "wrap",
                margin: 'auto',
                paddingTop: '5%'
            }}>{grid}</div>
            <div>
                <button style={{position: 'absolute', top: '90%', left: '10%', width: '50px', height: '50px'}}>Solve
                </button>
                <button style={{position: 'absolute', top: '90%', left: '80%', width: '50px', height: '50px'}}>Reset
                </button>
            </div>
        </div>

    )
}
export default Slido;