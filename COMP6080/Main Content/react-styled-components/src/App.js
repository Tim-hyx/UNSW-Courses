import React from 'react';
import Container from './Container'
import { BaseButton, PrimaryButton, SecondaryButton, ContrastButton } from './Button';

const onClick = () => console.log("onClick has been called");

function App() {
  return (
    <Container>
      <h1>Buttons</h1>
      <BaseButton>Base Button</BaseButton>
      <PrimaryButton animated={true} onClick={onClick}>Primary Button</PrimaryButton>
      <SecondaryButton onClick={onClick}>Secondary Button</SecondaryButton>
      <ContrastButton onClick={onClick}>Contrast Button</ContrastButton>
    </Container>
  )

}

export default App;
