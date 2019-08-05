import React, {Component} from 'react';
import ToggleButton from "react-bootstrap/ToggleButton";
import ButtonGroup from "react-bootstrap/ButtonGroup";

export default class LoginRegisterChangeButton extends Component {

    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div className="d-flex flex-column">
                <ButtonGroup toggle>
                    <ToggleButton type="radio" name="radio" defaultChecked value="1" onClick={this.props.handleLoginChange}>
                        Login
                    </ToggleButton>
                    <ToggleButton type="radio" name="radio" value="2" onClick={this.props.handleRegisterChange}>
                        Register
                    </ToggleButton>
                </ButtonGroup>
            </div>
        );
    }

}