# WaterSMRT: Be Weary of Your Water. :droplet:

### WaterSMRT is an application that monitors water usage in a residence, providing real-time predictions and recommendations on how to better optimize your home's water consumption patterns. 
*Using a waterflow sensor connected to an Arduino, WaterSMRT is able to accurately display weekly and monthly water usage data through graphs and qualitative reports showing progress from the previous week.Then, the app takes your data and gives you custom recommendations based on your largest water contributor and predicts your future water consumption using machine learning.* :chart_with_upwards_trend:

## What we used:

![React](https://img.icons8.com/ios/150/000000/react-native.png)
![Flask](https://www.olirowan.xyz/static/images/icons/flask-plain.svg)
![SQLite](https://cdn.mybrowseraddon.com/icons/sql-reader128.png)
![Arduino](https://embeddedcomputing.weebly.com/uploads/1/1/6/2/11624344/128-logo-arduino-extension_orig.png)  
  * **React Native** :iphone::computer:
    * This allows our interface to be compatible as an Android, iOS, and web app application, allowing for universal access across any device.
  * **Custom API using Flask** :outbox_tray:
    * Our custom built API takes data from the Arduino (connected to the waterflow sensor) and renders the data in various graphs, as well as calculates important statistics that are useful to the consumer. The API then sends a response back the front-end React Native App, displaying all the data for the user.
  * **SQLite Database** :memo:
    * Using a database allows us to keep a long-term record of water consumption, giving us the ability to make future predictions, compare the current rate with previous weeks, and estimate expected costs/savings over time.
  * **Arduino Microcontroller** :pager:
    * Allows us to collect live data straight from the water sources and create a text document ready for processing straight from the hardware.
 
## How it Works: 
After placing the waterflow sensor at any of the 4 primary water users of a household with a compatible valve (faucet, toilet, hose, or shower), our Arduino records the flowrate, total volume of water, and time of day and records the data in a temporary text file that gets deleted every week.:pencil: When the recording stops, the data is sent to an SQL database where it is stored for future predictions and graphing of previous weeks. The flow data will be graphed for the user to gain a visual representation of their consumption patterns and their data from the previous week will also be shown to show any potential improvements from before. The app then takes the data and tells the user where they are using the most water and tell the user some tips they could use to solve the problem. The tips were webscraped and sorted to assign them to their corresponding water types to customize the user's recommendations.

Using a linear regression model, the app will take the recommendations it made based on the data and will predict the savings you will gain when you implement the recommendations into your everyday life. This incentivizes users to conserve water, not only saving their wallets but also the environment! :moneybag: :deciduous_tree:

## Team:
 @yashp121 @PranavPusarla @computer-geek64 @therealsharath
