import React, { Component } from 'react';
import PropTypes from 'prop-types';
import './style.css';

class CarOfferView extends Component {
    static propTypes = {
        car: PropTypes.object.isRequired,
    }

    render() {
        const {
            car,
        } = this.props;
        console.log("render car",car.name);
        return (
            <header className="carHeader">
                <p>
                    {car.name}
                </p>
            </header>
        )

    }
}

export default CarOfferView;