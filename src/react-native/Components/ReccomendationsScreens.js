import React, {Component} from 'react';
import { View, StyleSheet, StatusBar } from 'react-native';
import { Text, Button } from 'galio-framework';

var x = 0;

class ReccomendationsScreens extends Component {
  constructor(props){
    super(props);
    this.state ={ isLoading: true, dataSource: [] }
  }
  
  render () {
    return (
      <>
        <View style={styles.container}>
        <Text color="#c9e265" bold h5>Your Reccomendations</Text>
        {
          this.state.dataSource.map((y) => {
            {x++}
            return (<Text p>{x}. {y}</Text>);
          })
        }
        </View>
      </>
    );
  }

  componentDidMount(){
    return fetch('http://143.215.61.136/watersmrt/api/v1.0/recommendations')
      .then((response) => response.json())
      .then((responseJson) => {
        this.setState({
          isLoading: false,
          dataSource: responseJson,
        }, function(){
          console.log(this.state.dataSource)
        });

      })
      .catch((error) =>{
        console.error(error);
      });
  }

}

const styles = StyleSheet.create({
  container: {
      padding: 20,
  }
});

export default ReccomendationsScreens;