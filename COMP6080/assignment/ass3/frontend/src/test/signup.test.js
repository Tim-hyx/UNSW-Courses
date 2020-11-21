import { mount } from "enzyme";
import { Provider } from "react-redux";
import Button from "@material-ui/core/Button";
import React from "react";
import TextField from "@material-ui/core/TextField";
import store from "../redux/stores";
import Signup from "../pages/signup/Signup";
// import Login from "../pages/login/Login";

// test signup button
describe('test signup page static html', () => {

    const wrapper = mount(
        <Provider store={store}>
            <Signup />
        </Provider>);
    
    it('Signup page should have a button to signup', () => {
       
        const signup = wrapper.children();
        const signupButton = signup.find(Button);
        expect(signupButton.text()).toBe("Signup");
        expect(signupButton).toMatchSnapshot();
    })

    it('Signup page has a textfield to input user email', () => {
       
        expect(wrapper.find(TextField).first().text()).toBe("Email *");
    });

    it('Signup page has a textfield to input user email', () => {
      
        expect(wrapper.find(TextField).first().text()).toBe("Email *");
    });

    it('Signup page has a textfield to input user password', () => {
     
        expect(wrapper.find(TextField).at(1).text()).toBe("Password *");
    });

    it('Signup page has a textfield to verify user password', () => {
      
        expect(wrapper.find(TextField).at(2).text()).toBe("Type password again *");
    });


    it('Signup page has a textfield to input user name', () => {
    
        expect(wrapper.find(TextField).last().text()).toBe("Name *");
    });
})
