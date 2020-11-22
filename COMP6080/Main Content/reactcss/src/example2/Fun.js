import React from 'react';
import styled, { css } from 'styled-components';

export const Title = styled.h1`
  font-size: 2em;
  text-align: center;
`;

export const RedTitle = styled(Title)`
  color: red;
`

export const BigLink = styled.a`
  display: block;
  text-decoration: underline;
  font-weight: bold;
  ${props => props.primary
  	? css`color: black;`
  	: css`color: purple;`
  }
  ${props => props.fontSize
  	? css`font-size: ${props.fontSize}em`
  	: css`font-size: 2em`
  }
`;