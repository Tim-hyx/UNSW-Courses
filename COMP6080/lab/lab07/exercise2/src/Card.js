import React from "react";

const Card = (cardData, index) => {
    return (
        <div style={{ marginTop: '20px', border: 'solid', width: '10%' }} key={index}>
            <div style={{ display: 'flex' }}>
                <img style={{ width: '50px', height: '50px', margin: 'auto' }} src={cardData.avatar_url} alt="card" />
            </div>
            <div style={{ display: 'flex' }}>
                <a style={{ margin: 'auto' }} href={cardData.url} target="_blank" rel="noopener noreferrer">
                    {cardData.name}
                </a></div>
        </div>
    );
};

export default Card;
