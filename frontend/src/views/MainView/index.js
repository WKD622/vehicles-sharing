import React, { Component } from 'react';
//import CarOfferView from './components/CarOfferView';
import './style.css';
import TabBar from "../../components/TabBar";

//const Car = { name: 'Mercedes' };

class MainView extends Component {
    render() {
        return (
            <div className="App">
                <TabBar />
            </div>
        );
    }
}

export default MainView;
