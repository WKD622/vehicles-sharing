import React, {Component} from 'react';
import Form from "react-bootstrap/Form";
import Button from "react-bootstrap/Button";
import "./styles.css"
import axios from "axios";

export default class LoginForm extends Component {
    constructor() {
        super();
        this.state = {
            username: "",
            password: "",
        };

        this.handleUsername = this.handleUsername.bind(this);
        this.handlePassword = this.handlePassword.bind(this);
        this.login = this.login.bind(this);
        this.getFormData = this.getFormData.bind(this)
    }

    componentDidMount() {
        document.body.classList.add("background-color");
    }

    login() {
        console.log('login');
        axios.post(`http://127.0.0.1:8000/vehicles_sharing/users/login/`, this.getFormData({
            username: this.state.username,
            password: this.state.password
        })).then(res => {
            console.error(res.data);
            //TODO token jest pod res.data
        }).catch(error => {
            console.error(error);
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

    render() {
        return (
            <div className='d-flex flex-column align-items-center mt-5 '>
                <div className="bg-white rounded w-25">
                    <Form className="m-5">
                        <Form.Group controlId="formBasicEmail">
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
                        <Form.Group controlId="formBasicChecbox">
                            <Form.Check type="checkbox" label="Check me out"/>
                        </Form.Group>
                        <Button onClick={this.login}>
                            Submit
                        </Button>
                    </Form>
                </div>
            </div>
        )
    }


}