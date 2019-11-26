import React from 'react';
import {
  Platform,
  StyleSheet,
  Text,
  View, TouchableOpacity
} from 'react-native';

import { createStackNavigator } from  'react-navigation';
import IOSIcon from "react-native-vector-icons/Ionicons";
import MainScreen from "./MainScreen";
import WeeklyScreen from './WeeklyScreen';
import MonthlyScreen from "./MonthlyScreens";
import SavingsScreen from "./SavingsScreens";
import ReccomendationsScreens from "./ReccomendationsScreens";

const stackNav = createStackNavigator({
  Main : {
    screen: MainScreen,
    navigationOptions: ({navigation}) => ({
      headerLayoutPreset: 'center',
      title: "WaterSMRT",
      headerStyle: {
        backgroundColor: '#c9e265',
      },
      headerTitleStyle: {
        color: '#fff',
        textAlign: 'center',
     
      },
      headerLeft:(<TouchableOpacity onPress={() => navigation.openDrawer()}>
                    <View style={{
                      paddingLeft: 20
                    }}>
                      <IOSIcon
                        name="ios-menu"
                        size={30}
                        color='#fff'
                      />
                    </View>
                  </TouchableOpacity>
      ),
      headerRight:(<TouchableOpacity onPress={() => navigation.navigate("Main")}>
                    <View style={{
                      paddingRight: 20
                    }}>
                      <IOSIcon
                        name="ios-home"
                        size={30}
                        color='#fff'
                      />
                    </View>
                  </TouchableOpacity>
      ),
      headerShown: false,
    })
  },

  Week: {
    screen: WeeklyScreen,
    navigationOptions: ({navigation}) => ({
      title: "Weekly Report",
      headerStyle: {
        backgroundColor: '#c9e265',
      },
      headerTitleStyle: {
        color: '#fff',
        textAlign: 'center',
     
      },
      headerLeft:(<TouchableOpacity onPress={() => navigation.openDrawer()}>
                    <View style={{
                      paddingLeft: 20
                    }}>
                      <IOSIcon
                        name="ios-menu"
                        size={30}
                        color='#fff'
                      />
                    </View>
                  </TouchableOpacity>
      ),
      headerRight:(<TouchableOpacity onPress={() => navigation.navigate("Main")}>
                    <View style={{
                      paddingRight: 20
                    }}>
                      <IOSIcon
                        name="ios-home"
                        size={30}
                        color='#fff'
                      />
                    </View>
                  </TouchableOpacity>
      ),
    })     
  },
  Month: {
    screen: MonthlyScreen,
    navigationOptions: ({navigation}) => ({
      title: "Total Report",
      headerStyle: {
        backgroundColor: '#c9e265',
      },
      headerTitleStyle: {
        color: '#fff',
        textAlign: 'center',
     
      },
      headerLeft:(<TouchableOpacity onPress={() => navigation.openDrawer()}>
                    <View style={{
                      paddingLeft: 20
                    }}>
                      <IOSIcon
                        name="ios-menu"
                        size={30}
                        color='#fff'
                      />
                    </View>
                  </TouchableOpacity>
      ),
      headerRight:(<TouchableOpacity onPress={() => navigation.navigate("Main")}>
                    <View style={{
                      paddingRight: 20
                    }}>
                      <IOSIcon
                        name="ios-home"
                        size={30}
                        color='#fff'
                      />
                    </View>
                  </TouchableOpacity>
      ),
    })     
  },
  Savings: {
    screen: SavingsScreen,
    navigationOptions: ({navigation}) => ({
      title: "Improve Savings",
      headerStyle: {
        backgroundColor: '#c9e265',
      },
      headerTitleStyle: {
        color: '#fff',
        textAlign: 'center',
     
      },
      headerLeft:(<TouchableOpacity onPress={() => navigation.openDrawer()}>
                    <View style={{
                      paddingLeft: 20
                    }}>
                      <IOSIcon
                        name="ios-menu"
                        size={30}
                        color='#fff'
                      />
                    </View>
                  </TouchableOpacity>
      ),
      headerRight:(<TouchableOpacity onPress={() => navigation.navigate("Main")}>
                    <View style={{
                      paddingRight: 20
                    }}>
                      <IOSIcon
                        name="ios-home"
                        size={30}
                        color='#fff'
                      />
                    </View>
                  </TouchableOpacity>
      ),
    })     
  },
  Reccomendations: {
    screen: ReccomendationsScreens,
    navigationOptions: ({navigation}) => ({
      title: "Reccomendations",
      headerStyle: {
        backgroundColor: '#c9e265',
      },
      headerTitleStyle: {
        color: '#fff',
        textAlign: 'center',
     
      },
      headerLeft:(<TouchableOpacity onPress={() => navigation.openDrawer()}>
                    <View style={{
                      paddingLeft: 20
                    }}>
                      <IOSIcon
                        name="ios-menu"
                        size={30}
                        color='#fff'
                      />
                    </View>
                  </TouchableOpacity>
      ),
      headerRight:(<TouchableOpacity onPress={() => navigation.navigate("Main")}>
                    <View style={{
                      paddingRight: 20
                    }}>
                      <IOSIcon
                        name="ios-home"
                        size={30}
                        color='#fff'
                      />
                    </View>
                  </TouchableOpacity>
      ),
    }) 
  }
});

export default stackNav;