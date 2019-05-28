import React, { Component } from 'react';
//import CarOfferView from './components/CarOfferView';
import './style.css';
import TabBar from "../../components/TabBar";
import {Link} from "react-router-dom";

//const Car = { name: 'Mercedes' };

class MainView extends Component {
    render() {
        return (
            <div className="App">
                <Link to="/" style={{ textDecoration: 'none', color: 'white' }}>
                    <p className="logo">Vehicles Sharing</p>
                </Link>
                <TabBar />
            </div>
        );
    }
}

export default MainView;
