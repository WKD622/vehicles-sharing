import React, {Component} from 'react';
import Modal from "react-bootstrap/Modal";
import Button from "react-bootstrap/Button";
import DayPicker from 'react-day-picker';
import 'react-day-picker/lib/style.css';
import DaysRangePicker from "../DaysRangePicker";
import Form from "react-bootstrap/Form";
import Alert from "react-bootstrap/Alert";
import axios from "axios";
import {withRouter} from "react-router-dom";


class ReservationModal extends Component {
    constructor() {
        super();
        this.state = {
            startDate: null,
            endDate: null,
            message: '',
            wrongInput: false,
        };

        this.handleDate = this.handleDate.bind(this);
        this.handleMessage = this.handleMessage.bind(this);
        this.onReservation = this.onReservation.bind(this);
        this.showAlert = this.showAlert.bind(this);
    }

    handleDate(date) {
        if(date.from) {
            let startDate = date.from.toISOString().split('T')[0];
            this.setState({startDate});
        }
        if(date.to) {
            let endDate = date.to.toISOString().split('T')[0];
            this.setState({endDate});
        }
    }

    handleMessage(event) {
        let message = event.target.value;
        this.setState({message});
    }

    getFormData(object) {
        const formData = new FormData();
        Object.keys(object).forEach(key => formData.append(key, object[key]));
        return formData;
    }

    reserve() {
        const carId = this.props.match.params.id;;
        let data = {
            message: this.state.message,
            start_date: this.state.startDate,
            end_date: this.state.endDate,
        };
        let headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Token 2c61b7ba8b73de2f431157b40c975163a41d84d1',
        };
        let formData = this.getFormData(data);
        axios.post(`http://127.0.0.1:8000/vehicles_sharing/vehicles/${carId}/make_reservation/`, formData, {headers: headers})
            .then(res => {
                this.props.history.push('/cars');
            })
            .catch(() => this.showAlert());
    }

    onReservation() {
        if(this.state.startDate && this.state.endDate && this.state.message) {
            this.reserve();
        } else {
            this.setState({wrongInput: true});
        }
    }

    showAlert() {
        return (
            <Alert variant="danger">
                <Alert.Heading>Something is Wrong</Alert.Heading>
                <p>
                    Please select valid start date, end date and add message
                </p>
                <div className="d-flex justify-content-end">
                    <Button onClick={() => this.setState({wrongInput: false})} variant="outline-danger" >
                        Okay
                    </Button>
                </div>
            </Alert>)
    };

    render() {
        const divProps = Object.assign({}, this.props);
        delete divProps.staticContext;
        return (
            <Modal
                {...divProps}
                size="lg"
                aria-labelledby="contained-modal-title-vcenter"
                centered
            >
                <Modal.Body>
                    <h4>Select start date, end date and add message</h4>
                    <DaysRangePicker handleDate={this.handleDate}/>
                    <Form>
                        <Form.Group controlId="exampleForm.ControlTextarea1">
                            <Form.Label>Message:</Form.Label>
                            <Form.Control
                                as="textarea"
                                rows="3"
                                value={this.state.message}
                                onChange={this.handleMessage}
                            />
                        </Form.Group>
                    </Form>
                    {this.state.wrongInput && this.showAlert()}
                </Modal.Body>
                <Modal.Footer>
                    <Button variant="secondary" onClick={this.props.onHide}>Close</Button>
                    <Button variant="primary" onClick={this.onReservation}>
                        Reserve
                    </Button>
                </Modal.Footer>
            </Modal>
        );
    }
}

export default withRouter(ReservationModal);