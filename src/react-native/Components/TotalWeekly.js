import React, {Component} from 'react';
import { View, StyleSheet, Image, SafeAreaView } from 'react-native';
import { Text, Button, Block, Icon } from 'galio-framework';

class TotalWeekly extends Component {
  constructor(props){
    super(props);
    this.state ={ isLoading: true }
  }

  render () {
    return (
      <>
        <Text color="#c9e265">Total amount of water used this week: {this.state.dataSource} liters</Text>
      </>
    );
  }

  componentDidMount(){
    return fetch('http://143.215.61.136/watersmrt/api/v1.0/total/weekly')
      .then((response) => response.json())
      .then((responseJson) => {

        this.setState({
          isLoading: false,
          dataSource: responseJson.total,
        }, function(){
        });

      })
      .catch((error) =>{
        console.error(error);
      });
  }
}

const styles = StyleSheet.create({
  container: {
      flex: 1,
      justifyContent: 'center',
      alignItems: 'center'
  },
  space: {
    borderWidth: 10,
    borderColor: "#fff"
  },
  bordPad: {
    borderWidth: 4,
    borderRadius: 4,
    borderColor: "#c9e265",
    width: 370,
    height: 200,
    padding: 20,
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
    alignContent: "space-between"
  },
  bord: {
    borderWidth: 4,
    borderRadius: 4,
    padding: 2,
    borderColor: "#c9e265",
  },
});

export default TotalWeekly;