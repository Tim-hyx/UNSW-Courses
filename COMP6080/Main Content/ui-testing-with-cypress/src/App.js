import Container from './components/container/container';
import FormLayout from './components/form_layout/form_layout';
import SignupForm from './components/signup_form/signup_form';
import Header from './components/header/header';
import SignupSuccessBanner from './components/signup_success_banner/signup_success_banner';
import React from 'react';

function App() {
  const [userDetails, setUserDetails] = React.useState(undefined);

  const formIsSubmitted = React.useMemo(() => {
    return !!userDetails;
  }, [userDetails])

  const reset = React.useCallback(() => setUserDetails(undefined), [setUserDetails]);

  return (
    <Container>
      <FormLayout>
        { formIsSubmitted
          ? <SignupSuccessBanner email={userDetails.email} onReset={reset}/>
          : <React.Fragment>
              <Header>Sign Up ✨</Header>
              <SignupForm onSubmit={setUserDetails} />
            </React.Fragment>
        }
      </FormLayout>
    </Container>
  );
}

export default App;
