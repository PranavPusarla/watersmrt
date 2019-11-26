import React, {Component} from 'react';
import { NavBar } from 'galio-framework';
import {ScrollView, View} from 'react-native';

class Head extends Component {
    render () {
      return (
        <NavBar 
            title="Screen Title" 
            style={{ backgroundColor: '#000' }}
        />
      );
    }
}

export default Head;