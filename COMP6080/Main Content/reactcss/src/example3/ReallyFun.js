import React from 'react';
import { Box, Button } from '@material-ui/core';
import Checkbox from '@material-ui/core/Checkbox';

import { styled } from '@material-ui/core/styles';
import Button2 from '@material-ui/core/Button';

const MyButton = styled(Button2)({
  background: 'linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%)',
  border: 0,
  borderRadius: 3,
  boxShadow: '0 3px 5px 2px rgba(255, 105, 135, .3)',
  color: 'white',
  height: 48,
  padding: '0 30px',
});

const ReallyFun = (props) => {
  const [checked, setChecked] = React.useState(true);
  return (
    <>
      <Box m={4}>
        <Button color="primary">Hello World</Button>
        <MyButton color="primary">Hello World</MyButton>
      </Box>
      <Checkbox
        checked={checked}
        onChange={() => setChecked(!checked)}
        color="primary"
        inputProps={{ 'aria-label': 'secondary checkbox' }}
      />
      <Checkbox
        defaultChecked
        indeterminate
        inputProps={{ 'aria-label': 'indeterminate checkbox' }}
      />
    </>
  );
};

export default ReallyFun;