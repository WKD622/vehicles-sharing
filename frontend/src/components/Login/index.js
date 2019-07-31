import React, {Component} from 'react';
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "./styles.css"
import axios from "axios";
import LoginRegisterChangeButton from "./LoginRegisterChangeButton";
import {withRouter} from "react-router-dom";
import {bindActionCreators} from "redux";
import {setToken} from "../../actions/rootActions";
import {connect} from "react-redux";


class LoginForm extends Component {
    constructor(props, context) {
        super(props, context);
        this.state = {
            username: "",
            password: "",
            email: "",
            isCorrect: true,
            login: true,
        };

        this.handleUsername = this.handleUsername.bind(this);
        this.handlePassword = this.handlePassword.bind(this);
        this.handleEmail = this.handleEmail.bind(this);
        this.login = this.login.bind(this);
        this.register = this.register.bind(this);
        this.getFormData = this.getFormData.bind(this);
        this.renderForms = this.renderForms.bind(this);
        this.handleLoginChange = this.handleLoginChange.bind(this);
        this.handleRegisterChange = this.handleRegisterChange.bind(this);
    }

    componentDidMount() {
        document.body.classList.add("background-color");
    }

    register() {
        axios.post(`http://127.0.0.1:8282/vehicles_sharing/users/`, this.getFormData({
            username: this.state.username,
            password: this.state.password,
            email: this.state.email
        })).then(res => {
            this.handleLoginChange()
        }).catch(error => {
            this.setState({isCorrect: false});
        })
    }

    login() {
        console.log('login start');
        axios.post(`http://127.0.0.1:8282/vehicles_sharing/users/login/`, this.getFormData({
            username: this.state.username,
            password: this.state.password
        })).then(res => {
            this.props.setToken(res.data);
            this.props.history.push("/cars");
        }).catch(error => {
            console.log(error);
            this.setState({isCorrect: false});
        })
    };

    getFormData(object) {
        const formData = new FormData();
        Object.keys(object).forEach(key => formData.append(key, object[key]));
        return formData;
    }

    handleUsername(event) {
        let username = event.target.value;
        this.setState({username});
    }

    handlePassword(event) {
        let password = event.target.value;
        this.setState({password});
    }

    handleEmail(event) {
        let email = event.target.value;
        this.setState({email});
    }

    handleLoginChange(){
        this.setState({login: true, username: '', password: '', email: ''})
    }

    handleRegisterChange(){
        this.setState({login: false, username: '', password: '', email: ''})
    }


    renderForms() {
        if (this.state.login) {
            return (
                <Form className="m-4">
                    <Form.Group controlId="formBasicUsername">
                        <Form.Label>Username</Form.Label>
                        <Form.Control
                            type="text"
                            placeholder="Enter username"
                            value={this.state.username}
                            onChange={this.handleUsername}
                        />
                        <Form.Text className="text-muted">
                            We'll never share your email with anyone else.
                        </Form.Text>
                    </Form.Group>

                    <Form.Group controlId="formBasicPassword">
                        <Form.Label>Password</Form.Label>
                        <Form.Control
                            type="password"
                            placeholder="Enter password"
                            value={this.state.password}
                            onChange={this.handlePassword}
                        />
                    </Form.Group>
                    <p>{!this.state.isCorrect && "Wrong username or password"}</p>
                    <Button onClick={this.login}>
                        Submit
                    </Button>
                </Form>
            )
        } else {
            return (
                <Form className="m-4">
                    <Form.Group controlId="formBasicEmail">
                        <Form.Label>Email address</Form.Label>
                        <Form.Control
                            type="email"
                            placeholder="Enter email"
                            value={this.state.email}
                            onChange={this.handleEmail}
                        />
                        <Form.Text className="text-muted">
                            We'll never share your email with anyone else.
                        </Form.Text>
                    </Form.Group>

                    <Form.Group controlId="formBasicUsername">
                        <Form.Label>Username</Form.Label>
                        <Form.Control
                            type="text"
                            placeholder="Enter username"
                            value={this.state.username}
                            onChange={this.handleUsername}
                        />
                        <Form.Text className="text-muted">
                            We'll never share your email with anyone else.
                        </Form.Text>
                    </Form.Group>

                    <Form.Group controlId="formBasicPassword">
                        <Form.Label>Password</Form.Label>
                        <Form.Control
                            type="password"
                            placeholder="Enter password"
                            value={this.state.password}
                            onChange={this.handlePassword}
                        />
                    </Form.Group>
                    <p>{!this.state.isCorrect && "Wrong register data"}</p>
                    <Button onClick={this.register}>
                        Submit
                    </Button>
                </Form>
            )
        }
    }

    render() {
        return (<div className='d-flex flex-column align-items-center mt-5 '>
            <div className="bg-white rounded w-25">
                <LoginRegisterChangeButton handleLoginChange={this.handleLoginChange} handleRegisterChange={this.handleRegisterChange}/>
                {this.renderForms()}
            </div>
        </div>)
    }


}

const mapDispatchToProps = dispatch => bindActionCreators({
    setToken,
}, dispatch);

export default withRouter(connect(null,mapDispatchToProps)(LoginForm));
