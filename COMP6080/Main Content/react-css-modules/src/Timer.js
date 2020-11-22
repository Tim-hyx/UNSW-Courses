import * as React from 'react';
import styles from './Timer.module.css';

const format = (num) => {
  return num < 10 ? `0${num}` : `${num}`
}

function Timer() {
  const [seconds, setSeconds] = React.useState(0);
  const [minutes, setMinutes] = React.useState(0);

  React.useEffect(() => {
    const interval = window.setInterval(() => {
      setSeconds(s => s + 1);
    }, 1000);

    return () => clearInterval(interval)
  }, []);

  React.useEffect(() => {
    if (seconds >= 60) {
      setSeconds(0);
      setMinutes(m => m + 1);
    } 
  }, [seconds])

  return (
    <section className={styles.container}>
      <p className={styles.timer}>{format(minutes)}:{format(seconds)}</p>
    </section>
  )
}

export default Timer;
