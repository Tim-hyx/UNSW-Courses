import React from 'react';
import styled from 'styled-components';

const InputContainer = styled.div`
    display: flex;
    height: 40px;
`;

const InputLabel = styled.label`
    color: white;
    font-weight: bold;
    margin-right: 24px;
    min-width: 72px;
    height: 100%;
    display: flex;
    align-items: center;
`;

const TextInputWrapper = styled.input`
    width: 100%;
    color: white;
    font-weight: bold;
    background: 0;
    outline: 0;
    border: ${props => props.valid ? '2px solid white' : '2px solid red'};
    border-radius: 8px;
    padding: 16px;

    &::placeholder {
      color: #a6a5a6;
      font-weight: normal;
    }
`;

const TextInput = React.memo(({ 
  type = 'text',
  name,
  valid = true,
  label,
  placeholder,
  value,
  onChange,
}) => {
  return (
    <InputContainer>
      <InputLabel htmlFor={name}>{label}</InputLabel>
      <TextInputWrapper autoComplete="off" type={type} valid={valid} name={name} placeholder={placeholder} value={value} onChange={onChange}/>
    </InputContainer>
  )
});

export default TextInput;
