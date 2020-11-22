import logo from './logo.svg';
import './App.css';

import Boring from './example1/Boring';
import { Title, RedTitle, BigLink } from './example2/Fun';
import ReallyFun from './example3/ReallyFun';

function App() {

  return (
    <div>
      {/*<Boring href={"https://google.com"} />*/}
      <Title>Hello there</Title>
      <RedTitle>Hello there</RedTitle>
      <BigLink
        target="_blank"
        href="https://google.com"
      >
        Google
      </BigLink>
      <BigLink
        target="_blank"
        href="https://bing.com"
        primary
        fontSize={3.2}
      >
        Bing
      </BigLink>
      <ReallyFun />
    </div>
  );
}

export default App;
