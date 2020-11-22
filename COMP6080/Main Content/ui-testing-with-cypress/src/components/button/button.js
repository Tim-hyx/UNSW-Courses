import styled from 'styled-components';
import React from 'react';

const ButtonWrapper = styled.button`
    background-color: #785ef0;
    padding: 8px;
    height: 40px;
    color: white;
    font-weight: bold;
    cursor: pointer;
    border-radius: 8px;
    width: 100%;
    box-shadow: none;
    border: 0;
    outline: none;
    transition: background-color 0.15s ease-in-out;

    &:hover {
      background-color: #9b82f3;
    }

    &:disabled {
      cursor: default;
      background-color: #343334;
      color: #eaeaea;
    }
`

const Button = React.memo(({
  children,
  onClick,
  disabled,
}) => (
  <ButtonWrapper type="submit" disabled={disabled} onClick={onClick}>
    {children}
  </ButtonWrapper>
))

export default Button;
