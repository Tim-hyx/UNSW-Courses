import React from 'react';
import TextInput from '../text_input/text_input';
import Button from '../button/button';
import InputGroup from '../input_group/input_group';
import useEmailValidation from '../../hooks/use_email_validation';
import useEmptyValidation from '../../hooks/use_empty_validation';

const SignupForm = React.memo(({
  onSubmit,
}) => {
  const [name, setName] = React.useState('');
  const nameIsValid = useEmptyValidation(name);
  const [email, setEmail] = React.useState('');
  const emailIsValid = useEmailValidation(email);
  const [password, setPassword] = React.useState('');
  const passwordIsValid = useEmptyValidation(password);

  const readyToSubmit = React.useMemo(() => {
    return nameIsValid && emailIsValid && passwordIsValid;
  }, [nameIsValid, emailIsValid, passwordIsValid])

  const submitHandler = React.useCallback((e) => {
    // In this example, we conditionally render the form based on whether user details
    // exist in the top-level app state. In practice, this will cause a race condition,
    // because the form will immediately be unmounted, so the form's default submission
    // behaviour may attempt to find a form which no longer exists in the DOM.
    // To solve this, we prevent the default form submit behaviour from occurring.
    // In a real life application, there are much better solutions for this. For example, we could:
    //   * move the form outside of this component so that it is always rendered
    //   * rely on the form tags html behaviour instead of using react state for this work
    // In this application, we choose not to do this so we can encapsulate our components better,
    // which helps us avoid some messiness when we start to add in our tests.
    e.preventDefault();

    if (readyToSubmit) {
      onSubmit({
        name,
        email,
        password
      });
    }
  }, [readyToSubmit, name, email, password, onSubmit]);

  return (
    <form onSubmit={submitHandler}>
      <InputGroup>
        <TextInput 
          name="name"
          valid={nameIsValid}
          placeholder="John Smith" 
          label="Name"
          value={name}
          onChange={e => setName(e.target.value)}
        />
        <TextInput
          name="email"
          valid={emailIsValid}
          placeholder="john.smith@email.com"
          label="Email"
          value={email}
          onChange={e => setEmail(e.target.value)} 
        />
        <TextInput
          name="password"
          valid={passwordIsValid}
          type="password"
          placeholder="password"
          label="Password"
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
        <Button disabled={!readyToSubmit}>
          {readyToSubmit ? 'Submit' : 'Enter Your Details'}
        </Button>
      </InputGroup>
    </form>
  );
});

export default SignupForm;
