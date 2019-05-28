import React, { Component } from 'react';
import PropTypes from 'prop-types';
import './style.css';
import axios from 'axios';

class CarOfferView extends Component {
    constructor() {
        super();
        this.state = {
            cars: []
        };
    }

    componentDidMount() {
        axios.get(`http://127.0.0.1:8000/vehicles_sharing/vehicles/`,  { headers: { Authorization: 'Token 63ffa1d39174ea797d0b78db0ad5f8178363dfe3' } })
            .then(res => {
                const cars = res.data.results;
                this.setState({ cars });
            });
    };

    renderCarOffers() {
        return (
            this.state.cars.map(car =>
                (<header className="carHeader">{car.brand}</header>)
            ))
    }


    render() {
        return (
            <div className="carContainer">
                {this.renderCarOffers()}
            </div>
        )

    }
}

export default CarOfferView;
