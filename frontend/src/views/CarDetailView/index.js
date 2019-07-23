import React, {Component} from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios';
import {Link, withRouter} from "react-router-dom";
import './style.css';
import Carousel from "react-bootstrap/Carousel";
import ListGroup from "react-bootstrap/ListGroup";
import Container from "react-bootstrap/Container";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Button from "react-bootstrap/Button";
import ReservationModal from "../../components/ReservationModal";
import {connect} from "react-redux";

class CarDetailView extends Component {
    constructor() {
        super();
        this.state = {
            car: null,
            showModal: false,
        };
    }

    componentWillMount() {
        if (!this.props.token) this.props.history.push('/login');
    }

    componentDidMount() {
        const { token } = this.props;
        document.body.classList.add("background-color");
        const carId = this.props.match.params.id;
        axios.get(`http://127.0.0.1:8000/vehicles_sharing/vehicles/${carId}`, {headers: {Authorization: `Token ${token}`}})
            .then(res => {
                const car = res.data;
                console.log(car);
                this.setState({car});
            });
        axios.get(`http://127.0.0.1:8000/vehicles_sharing/photos/${carId}`, {headers: {Authorization: `Token ${token}`}})
            .then(res => {
                console.log(res);
            });
    };

    renderCarousel() {
        const carimg1 = `https://otomotopl-imagestmp.akamaized.net/images_otomotopl/924121601_1_1080x720_rev007.jpg`;
        const carimg2 = `https://otomotopl-imagestmp.akamaized.net/images_otomotopl/924121601_4_1080x720_rev007.jpg`;
        const carimg3 = `https://otomotopl-imagestmp.akamaized.net/images_otomotopl/924121601_14_1080x720_rev007.jpg`;
        return (
            <Carousel>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src={carimg1}
                        alt="First slide"
                    />
                </Carousel.Item>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src={carimg2}
                        alt="Third slide"
                    />
                </Carousel.Item>
                <Carousel.Item>
                    <img
                        className="d-block w-100"
                        src={carimg3}
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

    modalClose = () => this.setState({ showModal: false });

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
                            <Button
                                onClick={() => this.setState({ showModal: true })}
                                variant="outline-light">
                                Make Reservation!
                            </Button>
                        </Col>
                    </Row>
                </Container>
                <div className="mb-5"/>
                <ReservationModal
                    show={this.state.showModal}
                    onHide={this.modalClose}
                />
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

export default withRouter(connect(mapStateToProps)(CarDetailView));
