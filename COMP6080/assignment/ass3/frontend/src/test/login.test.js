import {mount} from 'enzyme';
import React from "react";
import {Provider} from "react-redux";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import { MemoryRouter as Router } from 'react-router-dom';
import sinon from 'sinon';
import store from "../redux/stores";
import Login from "../pages/login/Login";


// test login page
describe('test login page static html', () => {


    let loginPage;
    let wrapper;
    beforeEach(()=>{
        wrapper= mount(
            <Provider store={store}>
                <Login  />
            </Provider>);
        loginPage = wrapper.children();
    });
    afterEach(() => {
        wrapper.unmount();
	 });

    
    it('render a button to login', () => {
       
       
        const loginButton = loginPage.find(Button);
        expect(loginButton.text()).toBe("Log in");
        expect(loginButton).toMatchSnapshot();
    })

    it('render a textfield to input user email', () => {
      
        expect(loginPage.find(TextField).first().text()).toBe("Email *");
    });

    it('render a textfield to input user password ', () => {
      
        expect(loginPage.find(TextField).last().text()).toBe("Password *");
    });
    
    


})


describe('test login page dynamic behavior', () => {
    it('do not submit the form when click the submit button', () => {
	
        const onSubmit = sinon.spy();
        const mountWithRouter = node => mount(
            <Router>
                <Provider store={store}>
                    {node}
                </Provider>
            </Router>
        );
        const wrapper2 = mountWithRouter(<Login onSubmit={onSubmit} />);
        const form = wrapper2.find('form');
        form.simulate('submit');

        // because we build a SPA in react
        // when the form submit, we use preventDefault
        // and use react router to direct page without refresh
        expect(onSubmit.called).toBe(false);
    })
})