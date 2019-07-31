import React, {Component} from 'react';
import {Link, withRouter} from "react-router-dom";
import './style.css';
import axios from "axios";
import {connect} from "react-redux";

class UploadPhotoView extends Component {
    constructor(props) {
        super(props);
        this.state = {file: '', imagePreviewUrl: ''};
        this.renderUploader = this.renderUploader.bind(this);
    }

    componentWillMount() {
        if (!this.props.token) this.props.history.push('/login');
    }

    componentDidMount() {
        document.body.classList.add("background-color");
    }

    _handleSubmit(e) {
        e.preventDefault();
        // TODO: do something with -> this.state.file
        console.log('handle uploading-', this.state.file);
        this.submitPhoto();
    }

    _handleImageChange(e) {
        e.preventDefault();

        let reader = new FileReader();
        let file = e.target.files[0];

        reader.onloadend = () => {
            this.setState({
                file: file,
                imagePreviewUrl: reader.result
            });
        }

        reader.readAsDataURL(file)
    }

    renderUploader() {
        let {imagePreviewUrl} = this.state;
        console.log(imagePreviewUrl);
        let $imagePreview = null;
        if (imagePreviewUrl) {
            $imagePreview = (<img className="carPhoto" src={imagePreviewUrl}/>);
        } else {
            $imagePreview = (<div className="previewText">Please select an Image for Preview</div>);
        }

        return (
            <div className="previewComponent">
                <form onSubmit={(e) => this._handleSubmit(e)}>
                    <input className="fileInput"
                           type="file"
                           onChange={(e) => this._handleImageChange(e)}/>
                    <button className="submitButton"
                            type="submit"
                            onClick={(e) => this._handleSubmit(e)}>Upload Image
                    </button>
                    <button className="skipButton"
                            type="button"
                            onClick={() =>
                                this.props.history.push('/cars')}>Skip
                    </button>
                </form>
                <div className="imgPreview">
                    {$imagePreview}
                </div>
            </div>
        )
    }

    getFormData(object) {
        const formData = new FormData();
        Object.keys(object).forEach(key => formData.append(key, object[key]));
        return formData;
    }

    submitPhoto() {
        const carId = this.props.match.params.id;
        const { token } = this.props;
        let data = {
            car: carId,
            photo: this.state.file,
        };
        let headers = {
            'Content-Type': 'application/json',
            'Authorization': `Token ${token}`,
        };
        let formData = this.getFormData(data);
        axios.post(`http://127.0.0.1:8282/vehicles_sharing/photos/`, formData, {headers: headers})
            .then(res => {
                this.props.history.push('/cars');
            });
    }

    render() {
        return (
            <div>
                <Link to="/" style={{textDecoration: 'none', color: 'white'}}>
                    <p className="logo">Vehicles Sharing</p>
                </Link>
                {this.renderUploader()}
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

export default withRouter(connect(mapStateToProps)(UploadPhotoView));
