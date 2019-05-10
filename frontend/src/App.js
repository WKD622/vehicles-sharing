import React, { Component } from 'react';
import CarOfferView from './components/CarOfferView';
import './App.css';

const Car = { name: 'Mercedes' };

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <p>
            Wypożyczalnia samochodów
          </p>
        </header>
        <CarOfferView
          car={Car}
        />
      </div>
    );
  }
}

export default App;
