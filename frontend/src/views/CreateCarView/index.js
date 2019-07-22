import React, {Component} from 'react';
import {Link, withRouter} from "react-router-dom";
import './style.css';
import Form from "react-bootstrap/Form";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import axios from "axios";
import {connect} from "react-redux";

class CreateCarView extends Component {

    constructor(props, context) {
        super(props, context);
        this.state = {
            brand: "",
            model: "",
            price: 0,
            city: "",
            street: "",
            year: 0,
            capacity: 0,
            power: 0,
            train: "",
            description: "",
        };

        this.handleBrand = this.handleBrand.bind(this);
        this.handleModel = this.handleModel.bind(this);
        this.handlePrice = this.handlePrice.bind(this);
        this.handleCity = this.handleCity.bind(this);
        this.handleStreet = this.handleStreet.bind(this);
        this.handleYear = this.handleYear.bind(this);
        this.handleCapacity = this.handleCapacity.bind(this);
        this.handlePower = this.handlePower.bind(this);
        this.handleTrain = this.handleTrain.bind(this);
        this.handleDescription = this.handleDescription.bind(this);
        this.createCar = this.createCar.bind(this);
    }

    componentWillMount() {
        if (!this.props.token) this.props.history.push('/login');
    }

    componentDidMount() {
        document.body.classList.add("background-color");
    }

    handleBrand(event) {
        let brand = event.target.value;
        this.setState({brand});
    }

    handleModel(event) {
        let model = event.target.value;
        this.setState({model});
    }

    handlePrice(event) {
        let price = event.target.value;
        this.setState({price});
    }

    handleCity(event) {
        let city = event.target.value;
        this.setState({city});
    }

    handleStreet(event) {
        let street = event.target.value;
        this.setState({street});
    }

    handleYear(event) {
        let year = event.target.value;
        this.setState({year});
    }

    handleCapacity(event) {
        let capacity = event.target.value;
        this.setState({capacity});
    }

    handlePower(event) {
        let power = event.target.value;
        this.setState({power});
    }

    handleTrain(event) {
        let train = event.target.value;
        this.setState({train});
    }

    handleDescription(event) {
        let description = event.target.value;
        this.setState({description});
    }

    getFormData(object) {
        const formData = new FormData();
        Object.keys(object).forEach(key => formData.append(key, object[key]));
        return formData;
    }

    createCar() {
        let data = {
            brand: this.state.brand,
            model: this.state.model,
            price: this.state.price,
            city: this.state.city,
            street: this.state.street,
            production_year: this.state.year,
            capacity: this.state.capacity,
            power: this.state.power,
            drive_train: this.state.train,
            description: this.state.description,
        };
        const { token } = this.props;
        let headers = {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        };
        let formData = this.getFormData(data);
        axios.post(`http://127.0.0.1:8000/vehicles_sharing/vehicles/`, formData, {headers: headers})
            .then(res => {
                const carId = res.data.id;
                this.props.history.push(`addPhoto/${carId}`);
            }).catch(err => {
            console.log(err);
        })
    }

    renderForm() {
        return (
            <div className="w-75 bg-white rounded">
                <Form
                    noValidate
                    className="m-5"
                >
                    <Form.Row>
                        <Form.Group as={Col} md="4" controlId="validationCustom01">
                            <Form.Label>Brand</Form.Label>
                            <Form.Control
                                required
                                type="text"
                                placeholder="Brand"
                                value={this.state.brand}
                                onChange={this.handleBrand}
                            />
                        </Form.Group>
                        <Form.Group as={Col} md="4" controlId="validationCustom02">
                            <Form.Label>Model</Form.Label>
                            <Form.Control
                                required
                                type="text"
                                placeholder="Model"
                                value={this.state.model}
                                onChange={this.handleModel}
                            />
                            <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
                        </Form.Group>
                        <Form.Group as={Col} md="2" controlId="price">
                            <Form.Label>Price ($/day)</Form.Label>
                            <Form.Control
                                required
                                type="number"
                                placeholder="Price"
                                value={this.state.price}
                                onChange={this.handlePrice}
                            />
                        </Form.Group>
                    </Form.Row>
                    <Form.Row>
                        <Form.Group as={Col} md="3" controlId="validationCustom03">
                            <Form.Label>City</Form.Label>
                            <Form.Control type="text" placeholder="City" required
                                          value={this.state.city}
                                          onChange={this.handleCity}/>
                        </Form.Group>
                        <Form.Group as={Col} md="6" controlId="validationCustom04">
                            <Form.Label>Street</Form.Label>
                            <Form.Control type="text" placeholder="Street" required
                                          value={this.state.street}
                                          onChange={this.handleStreet} />
                        </Form.Group>
                    </Form.Row>
                    <Form.Row>
                        <Form.Group as={Col} md="2" controlId="year">
                            <Form.Label>Production year</Form.Label>
                            <Form.Control
                                required
                                type="text"
                                placeholder="Year"
                                value={this.state.year}
                                onChange={this.handleYear} />
                        </Form.Group>
                        <Form.Group as={Col} md="2" controlId="capacity">
                            <Form.Label>Capacity</Form.Label>
                            <Form.Control
                                required
                                type="number"
                                placeholder="Capacity"
                                value={this.state.capacity}
                                onChange={this.handleCapacity} />
                        </Form.Group>
                        <Form.Group as={Col} md="2" controlId="power">
                            <Form.Label>Power</Form.Label>
                            <Form.Control
                                required
                                type="number"
                                placeholder="Power"
                                value={this.state.power}
                                onChange={this.handlePower} />
                        </Form.Group>
                        <Form.Group as={Col} md="2" controlId="drive-train">
                            <Form.Label>Drive Train</Form.Label>
                            <Form.Control as="select" value={this.state.train}
                                          onChange={this.handleTrain} >
                                <option>RWD</option>
                                <option>AWD</option>
                                <option>FWD</option>
                            </Form.Control>
                        </Form.Group>
                    </Form.Row>
                    <Form.Row>
                        <Form.Group as={Col} md="8" controlId="description">
                            <Form.Label>Description</Form.Label>
                            <Form.Control
                                as="textarea"
                                rows="3"
                                value={this.state.description}
                                onChange={this.handleDescription} />
                        </Form.Group>
                    </Form.Row>
                    <Button onClick={this.createCar}>Submit form</Button>
                </Form>
            </div>
        )
    }

    render() {
        return (
            <div>
                <Link to="/" style={{textDecoration: 'none', color: 'white'}}>
                    <p className="logo">Vehicles Sharing</p>
                </Link>
                <div className="d-flex flex-column align-items-center mb-3">
                    {this.renderForm()}
                </div>
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

export default withRouter(connect(mapStateToProps)(CreateCarView));
