import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';
import MainView from '../views/MainView'

export default class RootNavigator extends Component {

    render() {
        return (
            <div>
                <Switch>
                    <Route path="/" exact component={MainView}/>
                    <Route path="/home" component={MainView}/>
                </Switch>
            </div>
        );
    }
}