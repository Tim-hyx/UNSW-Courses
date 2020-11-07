import React from 'react';

import { Header } from './Header';

export default {
  title: 'Example/Header',
  component: Header,
};

const Template = (args) => <Header {...args} />;
const username='Tim Huang'

export const Signedup = Template.bind({});
Signedup.args = {
  user: {username},
};

export const LoggedOut = Template.bind({});
LoggedOut.args = {username};
