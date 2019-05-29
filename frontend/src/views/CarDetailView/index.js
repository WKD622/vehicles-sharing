import React, {Component} from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios';

class CarDetailView extends Component {
    constructor() {
        super();
        this.state = {
            cars: []
        };
    }

    componentDidMount() {
        axios.get(`http://127.0.0.1:8000/vehicles_sharing/vehicles/`, {headers: {Authorization: 'Token 63ffa1d39174ea797d0b78db0ad5f8178363dfe3'}})
            .then(res => {
                const cars = res.data.results;
                this.setState({cars});
            });
    };

    renderCarOffers() {
        return (
            this.state.cars.map(car => this.renderCarOffer(car))
        )
    }

    renderCarOffer(car) {
        return (
            <div className="card flex-wrap w-50 mt-3 mb-3">
                <div className="card-header border-0">
                    <img src="//placehold.it/200" alt=""/>
                </div>
                <div className="card-block">
                    <h4 className="card-title text-md-center">{car.brand + " " + car.model}</h4>
                    <ul className="list-group list-group-flush text-md-left">
                        <li className="list-group-item">{"Price: "+car.price+"/day"}</li>
                        <li className="list-group-item">{"Production year: "+car.production_year}</li>
                        <li className="list-group-item">{"City: "+car.city}</li>
                        <li className="list-group-item">{"Capacity: "+car.capacity}</li>
                    </ul>
                    <a href="/" className="stretched-link"></a>
                </div>
            </div>
        )
    }


    render() {
        return (
            <div class="d-flex flex-column align-items-center">
                {this.renderCarOffers()}
            </div>
        )

    }
}

export default CarDetailView;
