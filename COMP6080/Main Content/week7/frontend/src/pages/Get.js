import React from "react";
import Countdown from 'react-countdown';

const Get = () => {
  const [count, setCount] = React.useState(0);

  React.useEffect(async () => {
    const response = await fetch('http://localhost:6080/count', {
      method: 'GET',
    });
    const payload = await response.json();
    setCount(payload.count);
  }, []);
  return (
    <>
      {count !== 0 && <Countdown
        date={Date.now() + count * 1000}
        onComplete={() => console.log('Done!1')}
        onPause={() => console.log('Done!2')}
        onStop={() => console.log('Done!3')}
      />}      
    </>
  );
}

export default Get;
