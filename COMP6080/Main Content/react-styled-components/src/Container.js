import styled from 'styled-components';

const Container = styled.section`
  display: flex;
  flex-direction: column;
  max-width: 400px;
  padding: 16px;

  & > button {
    margin-bottom: 8px;
  }
`

export default Container;

