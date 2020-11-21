import {mount} from "enzyme";
import {Provider} from "react-redux";
import Typography from "@material-ui/core/Typography";
import React from "react";
import store from "../redux/stores";
import Dashboard from "../pages/home/Dashboard";

describe('test dashboard page static html', () => {
    // test dashboard welcome text
    it('Dashboard page should have a welcome text', () => {
        const wrapper = mount(
            <Provider store={store}>
                <Dashboard/>
            </Provider>);
        const dashboard = wrapper.children();
        const dashboardText = dashboard.find(Typography);
        expect(dashboardText.text()).toBe("Welcome to the BigBrain game, please log in to play!");
        expect(dashboardText).toMatchSnapshot();
    })
})
