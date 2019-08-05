import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom';
import { connect } from 'react-redux';
import MainView from '../views/MainView'

class RootNavigator extends Component {

    render() {
        return (
            <div>
                <Switch>
                    <Route path="/" exact component={MainView}/>
                </Switch>
            </div>
        );
    }
}

export default connect()(RootNavigator);