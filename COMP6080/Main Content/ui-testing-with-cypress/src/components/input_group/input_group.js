import styled from 'styled-components';
import React from 'react';

const InputGroupWrapper = styled.div`
    display: flex;
    flex-direction: column;
`

const InputGroupItem = styled.div`
    margin-top: 16px;
`;

const InputGroup = React.memo(({ children }) => (
  <InputGroupWrapper>
    {React.Children.toArray(children).map((child, i) => (
      <InputGroupItem key={i}>
        {child}
      </InputGroupItem>
    ))}
  </InputGroupWrapper>
));

export default InputGroup;
