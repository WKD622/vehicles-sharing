import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';
import MainView from '../views/MainView'
import CarOfferView from "../components/CarOfferView";

export default class RootNavigator extends Component {

    render() {
        return (
            <div>
                <Switch>
                    <Route path="/" exact component={MainView}/>
                    <Route path="/home" component={MainView}/>
                    <Route path="/cars" component={CarOfferView} />
                </Switch>
            </div>
        );
    }
}