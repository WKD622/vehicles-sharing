import React, {Component} from 'react';
import PropTypes from 'prop-types';
import 'bootstrap/dist/css/bootstrap.css';
import './style.css';
import axios from 'axios';
import Card from "react-bootstrap/Card";
import CardGroup from "react-bootstrap/CardGroup";
import Button from "react-bootstrap/Button";
import {withRouter} from "react-router-dom";
import {connect} from "react-redux";

class CarOfferView extends Component {
    constructor() {
        super();
        this.state = {
            cars: [],
            photos: [],
        };
    }

    componentWillMount() {
        if (!this.props.token) this.props.history.push('/login');
    }

    componentDidMount() {
        const { token } = this.props;
        document.body.classList.add("background-color");
        Promise.all([axios.get(`http://127.0.0.1:8000/vehicles_sharing/vehicles/`, {headers: {Authorization: `Token ${token}`}}),
                axios.get(`http://127.0.0.1:8000/vehicles_sharing/photos/`, {headers: {Authorization: `Token ${token}`}})])
            .then(([cars, photos]) => {
                if(cars.data.results && photos.data.results) {
                    let carHolders =[];
                    carHolders.length = cars.data.count;
                    photos.data.results.map(p => {
                        if(p.car) {
                            carHolders[p.car] = p.photo;
                        }
                    })
                    this.setState({
                        cars: cars.data.results,
                        photos: carHolders,
                    })
                } else if (cars.data.results) {
                    this.setState({
                        cars: cars.data.results,
                    })
                }
            })
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
        const imgHolder = this.state.photos && this.state.photos[car.id] ? this.state.photos[car.id] :
            `https://hlfppt.org/wp-content/uploads/2017/04/placeholder.png`;
        return (
            <Card className="m-2">
                <Card.Header>
                    <img className="fit-image" src={imgHolder} />
                </Card.Header>
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

const mapStateToProps = (state) => {
    const token = state.token;
    return {
        token,
    };
};

export default withRouter(connect(mapStateToProps)(CarOfferView));
