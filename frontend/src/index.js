import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { createStore } from 'redux';
// import Router from './routes';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom'
import './index.css';
import rootReducer from './reducers'
import * as serviceWorker from './serviceWorker';
import MainView from "./views/MainView";
import CarOfferView from "./components/CarOfferView";
import Something from "./views/Something";
import CarDetailView from "./views/CarDetailView";

const store = createStore(rootReducer);

ReactDOM.render(
    <Provider store={store}>
        <Router>
            <Switch>
                <Route path="/" exact component={MainView} />
                <Route path="/cars" exact component={MainView}/>
                <Route path="/user" exact component={MainView}/>
                <Route path="/cars/:id" component={CarDetailView} />
            </Switch>
        </Router>
    </Provider>,
    document.getElementById('root'),
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
