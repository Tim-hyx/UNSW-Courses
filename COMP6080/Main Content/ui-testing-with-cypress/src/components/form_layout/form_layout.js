import styled from 'styled-components';

const FormLayout = styled.div`
    display: grid;
    row-gap: 32px;
    padding: 16px;
    box-sizing: border-box;
    width: clamp(240px, 400px, 400px);
`;

export default FormLayout;
