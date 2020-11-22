import styled, { css, keyframes } from 'styled-components';

const removeDefaultButtonStyles = css`
  border: 0;
  padding: 0;
  font-family: inherit;
  font-weight: normal;
  background-color: unset;
  outline: none;
`;

export const BaseButton = styled.button`
  ${removeDefaultButtonStyles};
  cursor: pointer;
  padding: 12px;
  box-sizing: border-box;
  border-radius: 4px;
  font-weight: bold;
`;

const clickAnimation = keyframes`
  0% {
    transform: scale(1);
    border-radius: 4px;
    
  }

  50% {
    transform: scale(1.01);
  }

  75% {
    transform: scale(0.99);
  }

  100% {
    transform: scale(1);
  }
`;

function createHoverableButton(backgroundColor, hoverColor, inverted) {
  return styled(BaseButton)`
    color: ${inverted ? 'white' : 'black'};
    background-color: ${backgroundColor};

    &:hover {
      background-color: ${hoverColor};
      animation: ${props => props.animated ? css`${clickAnimation} 0.15s ease-in-out` : undefined};
    }
  `;
}

export const PrimaryButton = createHoverableButton(
  "#19aaee",
  "#33bbff",
  true,
);

export const SecondaryButton = createHoverableButton(
  "#d5d7d7",
  "#edf0f2",
  false,
);

export const ContrastButton = createHoverableButton(
  "#7d2ae8",
  "#8d39fa",
  true,
);
