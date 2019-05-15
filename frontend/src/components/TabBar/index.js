import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { Tab, TabList, Tabs, TabPanel } from 'react-context-tabs';
import { connect } from 'react-redux';
import classNames from 'classnames';

import './style.css';
import CarOfferView from "../CarOfferView";
import { FaCar, FaUserEdit } from 'react-icons/fa';
import { withRouter } from "react-router-dom";

class TabBar extends Component {

    render() {
        let selectedTabId = 'cars'

        return (
            <Tabs
                className={classNames('tabBar')}
                defaultTabId='cars'
                onTabChange={(nextTabId) => {
                    nextTabId === 'cars' ? this.props.history.push('cars') : this.props.history.push('/');
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
                        <Tab tabId='smth' className='userTab'>
                            <FaCar className="icon"/><span>{'Smth'}</span>
                            <div className='tabStone'/>
                        </Tab>
                    </div>
                </TabList>
                <TabPanel tabId='cars'>
                    <CarOfferView />
                </TabPanel>
                <TabPanel tabId='user'>
                    <CarOfferView />
                </TabPanel>
                <TabPanel tabId='smth'>
                    <CarOfferView />
                </TabPanel>
            </Tabs>
        );
    }
}

export default withRouter(TabBar);
