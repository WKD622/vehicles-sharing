import React, {Component} from 'react';
import {Link} from "react-router-dom";
import './style.css';
import axios from "axios";

export default class UploadPhotoView extends Component {
    constructor(props) {
        super(props);
        this.state = {file: '', imagePreviewUrl: ''};
        this.renderUploader = this.renderUploader.bind(this);
    }

    componentDidMount() {
        document.body.classList.add("background-color");
    }

    _handleSubmit(e) {
        e.preventDefault();
        // TODO: do something with -> this.state.file
        console.log('handle uploading-', this.state.file);
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

        reader.readAsBinaryString(file)
    }

    renderUploader() {
        let {imagePreviewUrl} = this.state;
        console.log(imagePreviewUrl);
        let $imagePreview = null;
        if (imagePreviewUrl) {
            $imagePreview = (<img src={imagePreviewUrl}/>);
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
                </form>
                <div className="imgPreview">
                    {$imagePreview}
                </div>
            </div>
        )
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
