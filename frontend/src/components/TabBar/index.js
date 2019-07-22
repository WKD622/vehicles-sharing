import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Tab, TabList, Tabs, TabPanel } from 'react-context-tabs';
import { connect } from 'react-redux';
import classNames from 'classnames';

import './style.css';
import CarOfferView from "../../views/CarOfferView";
import { FaCar, FaUserEdit } from 'react-icons/fa';
import { withRouter } from "react-router-dom";
import UserView from "../../views/UserView";

class TabBar extends Component {

    render() {
        const pathname = this.props.location.pathname;
        let selectedTabId;
        switch (pathname) {
            case '/cars':
                selectedTabId = 'cars';
                break;
            case '/user':
                selectedTabId = 'user';
                break;
            case '/':
            default:
                selectedTabId = 'cars';
        }

        return (
            <Tabs
                className={classNames('tabBar')}
                defaultTabId={selectedTabId}
                onTabChange={(nextTabId) => {
                    this.props.history.push(nextTabId);
                }}
            >
                <TabList>
                    <div className="tabbarContent">
                        <Tab tabId='cars' className='carsTab'>
                            <FaCar className="icon"/><span>{'Cars'}</span>
                            <div className='tabStone'/>
                        </Tab>
                        <Tab tabId='user' className='userTab'>
                            <FaUserEdit className="icon"/><span>{'User'}</span>
                            <div className='tabStone'/>
                        </Tab>
                    </div>
                </TabList>
                <TabPanel tabId='cars'>
                    <CarOfferView />
                </TabPanel>
                <TabPanel tabId='user'>
                    <UserView />
                </TabPanel>
            </Tabs>
        );
    }
}

export default withRouter(TabBar);
