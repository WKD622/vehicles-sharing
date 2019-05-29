import React, {Component} from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios';
import {Link} from "react-router-dom";
import './style.css';
import Carousel from "react-bootstrap/Carousel";
import ListGroup from "react-bootstrap/ListGroup";
import Container from "react-bootstrap/Container";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Button from "react-bootstrap/Button";

class CarDetailView extends Component {
    constructor() {
        super();
        this.state = {
            car: null,
        };
    }

    componentDidMount() {
        document.body.classList.add("background-color");
        const carId = this.props.match.params.id;
        axios.get(`http://127.0.0.1:8000/vehicles_sharing/vehicles/${carId}`, {headers: {Authorization: 'Token 63ffa1d39174ea797d0b78db0ad5f8178363dfe3'}})
            .then(res => {
                const car = res.data;
                this.setState({car});
            });
    };

    renderCarousel() {
        const carimg = `https://images.pexels.com/photos/170811/pexels-photo-170811.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940`;
        return (
            <Carousel>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src={carimg}
                        alt="First slide"
                    />
                </Carousel.Item>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src={carimg}
                        alt="Third slide"
                    />
                </Carousel.Item>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src={carimg}
                        alt="Third slide"
                    />
                </Carousel.Item>
            </Carousel>
        )
    }

    renderCarInfo() {
        const car = this.state.car;
        if (!car) return null;
        return (
            <ListGroup className="">
                <ListGroup.Item>{car.brand + " " + car.model}</ListGroup.Item>
                <ListGroup.Item>{"Price: " + car.price + "$/day"}</ListGroup.Item>
                <ListGroup.Item>{"Production year: " + car.production_year}</ListGroup.Item>
                <ListGroup.Item>{"Adress: " + car.street + ", " + car.city}</ListGroup.Item>
                <ListGroup.Item>{"Capacity: " + car.capacity}</ListGroup.Item>
                <ListGroup.Item>{"Drive train: " + car.drive_train}</ListGroup.Item>
                <ListGroup.Item>{"Power: " + car.power + " HP"}</ListGroup.Item>
            </ListGroup>
        )

    }

    render() {
        return (
            <div className="container">
                <Link to="/" style={{textDecoration: 'none', color: 'white'}}>
                    <p className="logo">Vehicles Sharing</p>
                </Link>
                <Container>
                    <Row>
                        <Col sm={8}>{this.renderCarousel()}</Col>
                        <Col sm={4} className="d-flex flex-column">
                            {this.renderCarInfo()}
                            <Button variant="outline-light">Make Reservation!</Button>
                        </Col>
                    </Row>
                </Container>
                <div className="mb-5"/>
            </div>
        )
    }
}

export default CarDetailView;
