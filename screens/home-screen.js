import React from 'react';
import { StyleSheet, View, TouchableOpacity } from 'react-native';
import { Icon } from 'react-native-elements';
import axios from 'axios';

export default class HomeScreen extends React.Component {
    constructor() {
        super();
        this.state = {
            articleDetails : {}
        }
    }

    timeConvert(num) {
        hours = Math.floor(num/60)
        minutes = num%60
        return `${hours} hrs ${minutes} mins`
    } 

    getArticleDetails = () => {
        const url = ''
        axios.get(url).then((response) => {
            let details = response.data.data
            details['runtime'] = this.timeConvert(details.runtime)
            this.setState({
                articleDetails : details
            })
        })
    } 

    componentDidMount() {
        this.getArticleDetails()
    }

    likedArticle = () => {
        const url = ''
        axios.post(url).then((response) => {
            this.getArticleDetails()
        })
    }

    unlikedArticle = () => {
        const url = ''
        axios.post(url).then((response) => {
            this.getArticleDetails()
        })
    }

    render() {
        return (
            <View style={styles.container}>

                <View style={styles.lowerBottomContainer}>
                    <TouchableOpacity onPress = {this.likedArticle}>
                        <Icon
                            reverse
                            name = {'check'}
                            type = {'entypo'}
                            size = {30}
                        />
                    </TouchableOpacity>

                    <TouchableOpacity onPress = {this.unlikedArticle}>
                        <Icon
                            reverse
                            name = {'cross'}
                            type = {'entypo'}
                            size = {30}
                        />
                    </TouchableOpacity>
                </View>

            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
        alignItems: 'center',
        justifyContent: 'center',
    },
    lowerBottomContainer: {
        flex : 0.45
    }
});
