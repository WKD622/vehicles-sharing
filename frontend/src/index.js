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
import CarDetailView from "./views/CarDetailView";
import CreateCarView from "./views/CreateCarView";
import LoginForm from "./components/Login";
import UploadPhotoView from "./views/UploadPhotoView";
import UserView from "./views/UserView";
import {loadState, saveState} from "./localStorage";
import {throttle} from "lodash";

const persistedState = loadState();
const store = createStore(rootReducer, persistedState);

store.subscribe(throttle(() => {
    saveState({
        token: store.getState().token
    });
}, 1000));

ReactDOM.render(
    <Provider store={store}>
        <Router>
            <Switch>
                <Route path="/" exact component={MainView} />
                <Route path="/cars" exact component={MainView}/>
                <Route path="/user" exact component={MainView}/>
                <Route path="/cars/:id" component={CarDetailView} />
                <Route path="/addCar" component={CreateCarView} />
                <Route path="/addPhoto/:id" component={UploadPhotoView} />
                <Route path="/login" component={LoginForm}/>
                <Route path="/user" component={UserView}/>
            </Switch>
        </Router>
    </Provider>,
    document.getElementById('root'),
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
