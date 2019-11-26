import PropTypes from 'prop-types';
import React, {Component} from 'react';
import styles from './SideMenu.style';
import {NavigationActions, SafeAreaView} from 'react-navigation';
import {ScrollView, View, TouchableOpacity} from 'react-native';
import { Text } from 'galio-framework';

class SideMenu extends Component {
  navigateToScreen = (route) => () => {
    const navigateAction = NavigationActions.navigate({
      routeName: route
    });
    this.props.navigation.dispatch(navigateAction);
  }

  render () {
    return (
      <>
        <SafeAreaView />
        <View style={styles.container}>
          <ScrollView>

            <Text style={styles.sectionHeadingStyle} h5>
                SMRT Checks
            </Text>

            <TouchableOpacity onPress={() => this.props.navigation.navigate("Week")}>
              <Text style={styles.navItemStyle} title="Weekly" size={17}>
                    Weekly Report
              </Text>
            </TouchableOpacity>

            <TouchableOpacity onPress={() => this.props.navigation.navigate("Month")}>
              <Text style={styles.navItemStyle} title="Monthly" size={17}>
                    Total Report
              </Text>
            </TouchableOpacity>

            <TouchableOpacity onPress={() => this.props.navigation.navigate("Savings")}>
              <Text style={styles.navItemStyle} title="Savings" size={17}>
                    Savings
              </Text>
            </TouchableOpacity>

            <TouchableOpacity onPress={() => this.props.navigation.navigate("Reccomendations")}>
              <Text style={styles.navItemStyle} title="Reccomendations" size={17}>
                    Reccomendations
              </Text>
            </TouchableOpacity>

          </ScrollView>
        </View>
      </>
    );
  }

}

SideMenu.propTypes = {
  navigation: PropTypes.object
};


export default SideMenu;