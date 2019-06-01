import React, {Component} from 'react';
import PropTypes from 'prop-types';
import 'bootstrap/dist/css/bootstrap.css';
import './style.css';
import axios from 'axios';
import Card from "react-bootstrap/Card";
import CardGroup from "react-bootstrap/CardGroup";
import Button from "react-bootstrap/Button";
import {withRouter} from "react-router-dom";

class CarOfferView extends Component {
    constructor() {
        super();
        this.state = {
            cars: []
        };
    }

    componentDidMount() {
        document.body.classList.add("background-color");
        axios.get(`http://127.0.0.1:8000/vehicles_sharing/vehicles/`, {headers: {Authorization: 'Token 63ffa1d39174ea797d0b78db0ad5f8178363dfe3'}})
            .then(res => {
                const cars = res.data.results;
                this.setState({cars});
            });
    };

    renderCarOffers() {
        // return (
        //     this.state.cars.map(car => this.renderCarOffer(car))
        // )
        const cars = this.state.cars;
        let carRows = [];
        while (cars.length) {
            carRows.push(cars.splice(0,3));
        };
        return (
            carRows.map(row => this.renderRow(row))
        )
    }

    renderRow(cars) {
        if (cars.length === 1) {
            return (
                <CardGroup className="w-25">
                    {cars.map(car => this.renderCarOffer(car))}
                </CardGroup>
            );
        } else if(cars.length === 2) {
            return (
                <CardGroup className="w-50">
                    {cars.map(car => this.renderCarOffer(car))}
                </CardGroup>
            );
        }
        return (
            <CardGroup className="w-75">
                {cars.map(car => this.renderCarOffer(car))}
            </CardGroup>
        );
    }

    renderCarOffer(car) {
        const imgHolder = `https://img.autobytel.com/car-reviews/autobytel/130878-10-cute-small-cars/BMW-i3.jpg`;
        return (
            <Card className="m-2">
                <Card.Img variant="top" src={imgHolder}/>
                <Card.Body>
                    <Card.Title>{car.brand + " " + car.model}</Card.Title>
                    <Card.Text>
                        {car.price+"$/day - capacity: "+car.capacity}
                    </Card.Text>
                    <a  href={`/cars/${car.id}`} className="stretched-link">{}</a>
                </Card.Body>
            </Card>
        )
    }


    render() {
        return (
            <div className="d-flex flex-column align-items-center">
                <div className="w-75">
                    <Button variant="info" size="lg" block onClick={() => this.props.history.push('/addCar')}>
                        You have a car to share? Click here!
                    </Button>
                </div>
                {this.renderCarOffers()}
            </div>
        )

    }
}

export default withRouter(CarOfferView);
