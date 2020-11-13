import * as React from "react";


export const ProductCard = ({ item, onAddToCart, discount = 0 }) => {
  // TODO - add your component here
  const id = item.id
  const image = item.image
  const title = item.title
  const price = item.price.toFixed(2)
  const currency = item.currency
  const description = item.descriptions
  const recommendationRatio = item.recommendationRatio
  const cardstyle = {
    boxShadow: '0 8px 16px 0 rgba(0,0,0,0.2)',
    transaction: '0.3s',
    width: '1000px',
    height: '600px',
  }
  const imgstyle = {
    float: 'left',
    width: '500px',
    height: '600px',
  }
  const titlestyle = {
    fontSize: '40px',
    fontWeight: 'bold',
    marginBottom: '10px',
    marginTop: '30px',
  }
  const textstyle = {
    fontSize: '20px',
    textAlign: 'center'
  }
  const pricestyle = {
    color: '#6f696d',
    marginBottom: '50px',
  }
  const boardstyle = {
    width: '400px',
    margin: 'auto'
  }
  const recommandstyle = {
    fontSize: '20px',
    marginTop: '50px',
  }
  let descriptions = []
  for (let i = 0; i < description.length; i++) {
    descriptions.push(<div>{description[i]}</div>);
  }
  const [value, setValue] = React.useState(0);
  const buttonstyle = {
    marginLeft: '20px',
    width: '100px',
    height: '90px',
    backgroundColor: '#efefef',
    fontSize: '20px',
    padding: '8px'
  }
  const circle = []
  let filled = Math.ceil(recommendationRatio * 5)
  for (let j = 0; j < filled; j++) {
    circle.push(<circle cx={50 + j * 50} cy={50} r={20} fill="yellow" stroke={'black'} />)
  }
  for (let n = 0; n < 5 - filled; n++) {
    circle.push(<circle cx={50 * filled + (n + 1) * 50} cy={50} r={20} fill="none" stroke={'black'} />)
  }


  return (
    <>
      <div style={cardstyle}>
        <title>{title}</title>
        <img src={image} alt={'bike'} style={imgstyle} />
        <div style={titlestyle}>{title}</div>
        <div style={pricestyle}>$ {price * (1 - discount)} {currency}</div>
        <div style={{ display: 'flex' }}>
          <div style={boardstyle}>
            <div style={textstyle}>{descriptions}</div>
          </div>
        </div>
        <div style={recommandstyle}>Highly recommended by {recommendationRatio * 100}% users</div>
        <svg style={{ height: '100px' }}>
          {circle}
        </svg>

        <div style={{ fontSize: '30px' }}>
          <span onClick={() => setValue(value - 1)}>- </span>
          <span>{value}</span>
          <span onClick={() => setValue(value + 1)}> +</span>
          <span onClick={() => onAddToCart(id, value)} style={buttonstyle}>Add to cart</span>
        </div>
      </div>
    </>
  )
    ;
};
