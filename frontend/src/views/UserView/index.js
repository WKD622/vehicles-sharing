import React, {Component} from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import {withRouter} from "react-router-dom";
import {connect} from "react-redux";
import './style.css';
import axios from "axios";
import {removeToken} from "../../actions/rootActions";
import {bindActionCreators} from "redux";
import Button from "react-bootstrap/Button";
import {ButtonGroup, ButtonToolbar, Col, ListGroup, Nav, Row, Tab, Table, Tabs} from "react-bootstrap";
import { FaCheck, FaBan } from 'react-icons/fa';

class UserView extends Component {
    constructor() {
        super();
        this.state = {
            activeTab: '',
            my_reservations: [],
            reservation_requests: [],
        };
        this.logout = this.logout.bind(this);
        this.activate= this.activate.bind(this);
        this.deactivate = this.deactivate.bind(this);
    }

    componentWillMount() {
        if (!this.props.token) this.props.history.push('/login');
    }

    componentDidMount() {
        const {token} = this.props;
        document.body.classList.add("background-color");
        axios.get(`http://127.0.0.1:8000/vehicles_sharing/reservations/`, {headers: {Authorization: `Token ${token}`}})
            .then(res => {
                let my = [];
                let someones = [];
                if (res.data && res.data.results) {
                    res.data.results.forEach(r => r.reservation_on_my_vehicle ?
                        my.push(r) : someones.push(r))
                }
                this.setState({
                    my_reservations: my,
                    reservation_requests: someones,
                })
            });
    };

    getFormData(object) {
        const formData = new FormData();
        Object.keys(object).forEach(key => formData.append(key, object[key]));
        return formData;
    }

    logout() {
        this.props.removeToken();
        this.props.history.push('/login');
    }

    activate(id) {
        const { token } = this.props;
        let headers = {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        };
        axios.post(`http://127.0.0.1:8000/vehicles_sharing/reservations/${id}/activate/`, {headers: headers});
    }

    deactivate(id) {
        const { token } = this.props;
        let headers = {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        };
        axios.post(`http://127.0.0.1:8000/vehicles_sharing/reservations/${id}/deactivate/`, {headers: headers});
    }

    getPrice(reservation) {
        const start = new Date(reservation.start_date);
        const end = new Date(reservation.end_date);
        const diffTime = Math.abs(end.getTime() - start.getTime());
        const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
        return diffDays*reservation.car.price+'$';
    }

    renderReservationTable() {
        if(this.state.activeTab === 'me' && this.state.my_reservations.length) {
            return (
                <div className="w-75 bg-white mt-3">
                    <Table striped bordered hover>
                        <thead>
                        <tr>
                            <th>Car</th>
                            <th>Start</th>
                            <th>End</th>
                            <th>Total Price</th>
                            <th>Active</th>
                        </tr>
                        </thead>
                        <tbody>
                        {this.state.my_reservations.map((reservation) =>
                        <tr>
                            <td onClick={() => this.props.history.push(`/cars/${reservation.car.id}`)}>{reservation.car.brand+' '+reservation.car.model}</td>
                            <td>{reservation.start_date}</td>
                            <td>{reservation.end_date}</td>
                            <td>{this.getPrice((reservation))}</td>
                            <td>{reservation.active ?
                                <FaCheck /> : <FaBan />}</td>
                            {reservation.active ? <Button variant="danger" onClick={() => this.deactivate(reservation.id)}>Deactivate</Button>
                                : <Button variant="success" onClick={() => this.activate(reservation.id)}>Activate</Button>}
                        </tr>)}
                        </tbody>
                    </Table>
                </div>
            )
        } else if(this.state.activeTab === 'someone' && this.state.reservation_requests.length) {
            return (
                <div className="w-75 bg-white mt-3">
                    <Table striped bordered hover>
                        <thead>
                        <tr>
                            <th>Car</th>
                            <th>Start</th>
                            <th>End</th>
                            <th>Total Earnings</th>
                            <th>Active</th>
                            <th></th>
                        </tr>
                        </thead>
                        <tbody>
                        {this.state.reservation_requests.map((reservation) =>
                            <tr>
                                <td onClick={() => this.props.history.push(`/cars/${reservation.car.id}`)}>
                                    {reservation.car.brand+' '+reservation.car.model}
                                </td>
                                <td>{reservation.start_date}</td>
                                <td>{reservation.end_date}</td>
                                <td>{this.getPrice((reservation))}</td>
                                <td>{reservation.active ?
                                    <FaCheck /> : <FaBan />}</td>
                            </tr>)}
                        </tbody>
                    </Table>
                </div>
            )
        }
    }

    render() {
        return (
            <div className="d-flex flex-column align-items-center mt-5">
                <ButtonToolbar aria-label="User buttons">
                    <ButtonGroup className="mr-2" aria-label="Reservation buttons">
                        <Button onClick={() => this.setState({activeTab: 'someone'})}>My Reservations</Button>
                        <Button onClick={() => this.setState({activeTab: 'me'})}>Reservation Requests</Button>
                    </ButtonGroup>
                    <ButtonGroup aria-label="Logout">
                        <Button variant="danger" onClick={this.logout}>Logout</Button>
                    </ButtonGroup>
                </ButtonToolbar>
                {this.renderReservationTable()}

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

const mapDispatchToProps = dispatch => bindActionCreators({
    removeToken,
}, dispatch);

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(UserView));
