import React from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';
import DashboardView from '../component/dashboard.jsx';

const AppRouter = () => (
    <BrowserRouter>
        <Switch>
            <Route path='/' exact={true} component={DashboardView}/>
            <Route path='/products' component={DashboardView}/>            
        </Switch>
    </BrowserRouter>
);

export default AppRouter;