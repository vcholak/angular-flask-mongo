import React from 'react';
import ReactDOM from 'react-dom';
import AppRouter from './route/app-route.jsx';
import 'normalize.css/normalize.css';
import 'bootstrap/dist/css/bootstrap.css';
import './style/main.scss';

ReactDOM.render(<AppRouter/>, document.getElementById('app'));