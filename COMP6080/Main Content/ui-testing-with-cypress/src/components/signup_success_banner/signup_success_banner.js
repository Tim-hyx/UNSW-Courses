import tick from './check.svg';
import { motion } from 'framer-motion';
import styled from 'styled-components';
import React from 'react';

const Wrapper = styled.div`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
`

const Image = styled(motion.img)`
  max-width: 240px;
  margin-bottom: 32px;
`

const CaptionHeading = styled.h2`
    font-weight: bold;
    font-size: 48px;
    color: white;
    text-align: center;
    margin: 0;
`

const CaptionText = styled.p`
    font-size: 18px;
    color: white;
    text-align: center;
    margin-top: 16px;
`;

const CaptionLink = styled.a`
    font-size: 16px;
    color: white;
    text-align: center;
    margin-top: 8px;
`;

export const Tick = React.memo(({
  email,
  onReset,
}) => (
  <Wrapper>
    <Image
      src={tick}
      animate={{
        scale: [1.1, 1],
      }}
      transition={{ duration: 0.25, easing: 'easeInOut' }}
    />
    <div/>
      <CaptionHeading>Form Submitted!</CaptionHeading>
      <CaptionText data-test-target="CaptionText">Check your email: {email}</CaptionText> 
      <CaptionLink href="#" onClick={onReset} >‹ Back</CaptionLink>
    <div/>
  </Wrapper>
));

export default Tick;
