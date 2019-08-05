import React, { Component } from 'react';
import { Route } from 'react-router-dom';
import { connect } from 'react-redux';
import { ConnectedRouter } from 'react-router-redux';

import RootNavigator from './RootNavigator';

class Router extends Component {
    render() {
        return (
            <ConnectedRouter>
                <Route component={RootNavigator} />
            </ConnectedRouter>
        );
    }
}

export default connect()(Router);