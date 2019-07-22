import React, {Component} from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import {withRouter} from "react-router-dom";
import {connect} from "react-redux";
import './style.css';
import axios from "axios";
import {removeToken} from "../../actions/rootActions";
import {bindActionCreators} from "redux";
import Button from "react-bootstrap/Button";

class UserView extends Component {
    constructor() {
        super();
        this.logout = this.logout.bind(this);
    }

    componentWillMount() {
        if (!this.props.token) this.props.history.push('/login');
    }

    componentDidMount() {
        const { token } = this.props;
        document.body.classList.add("background-color");
        axios.get(`http://127.0.0.1:8000/vehicles_sharing/reservations/`, {headers: {Authorization: `Token ${token}`}})
            .then(res => {
                console.log(res);
            });
    };

    logout() {
        this.props.removeToken();
        this.props.history.push('/login');
    }

    render() {
        return (
            <div className="d-flex flex-column align-items-center">
                <Button variant="danger" onClick={this.logout}>Logout</Button>
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
