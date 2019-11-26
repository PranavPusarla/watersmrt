import React, {Component} from 'react';
import { View, StyleSheet, Image, SafeAreaView } from 'react-native';
import { Text, Button, Block, Icon } from 'galio-framework';

class MainScreen extends Component {
  constructor(props){
    super(props);
    this.state ={ isLoading: true }
  }

  render () {
    return (
      <>
        <SafeAreaView />
        <View style={styles.container}>
          <Text color="#c9e265" h4 bold>Welcome, Team #20</Text> 
          <Block style={styles.space}/>
            <Block style={{display: "flex", flexDirection: "row"}}>
              <Text color="#c9e265" h5 bold>Weekly WaterSTATS </Text>
              <Icon name="clockcircleo" family="AntDesign" color="#c9e265" size={30}/>
            </Block>
          <Block style={styles.space}/>
          <Block shadow style={styles.bordPad}>
            <Text color="#c9e265" h5><Text color="#ff0000">Active</Text> Taps: 0</Text>
            <Text color="#c9e265" h5>Inactive Taps: 1</Text>
            <Text color="#c9e265" h5>Most used: Kitchen 1</Text>
          </Block>
          <Block style={styles.space}/>
          <Button color="#c9e265" onPress={() => this.props.navigation.navigate("Reccomendations")}>SMRTimize</Button>
          <Block style={styles.space}/>
          <Text color="#c9e265" h5 bold>Weekly WaterGRAPH</Text>
          <Block style={styles.space}/>
          <Block shadow style={styles.bord}>
            <Image 
              key={new Date()} 
              source={{uri: this.state.dataSource+'?time'+(new Date()).getTime(), headers: {Pragma: 'no-cache'}}}
              style={{width: 350, height: 250}} />
          </Block>      
        </View>
      </>
    );
  }

  componentDidMount(){
    return fetch('http://143.215.61.136/watersmrt/api/v1.0/graph/weekly')
      .then((response) => response.json())
      .then((responseJson) => {

        this.setState({
          isLoading: false,
          dataSource: responseJson.uri,
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
      alignItems: 'center',
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

export default MainScreen;

//http://143.215.61.136/watersmrt/api/v1.0/graph/weekly