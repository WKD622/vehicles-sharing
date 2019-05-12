import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore } from 'redux';
// import Router from './routes';
import { BrowserRouter as Router, Route } from 'react-router-dom'
import './index.css';
import rootReducer from './reducers'
import * as serviceWorker from './serviceWorker';
import MainView from "./views/MainView";

const store = createStore(rootReducer);

ReactDOM.render(
    <Provider store={store}>
        <Router>
            <Route path="/" component={MainView} />
        </Router>
    </Provider>,
    document.getElementById('root'),
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
