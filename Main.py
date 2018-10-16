"""
To Do: 1. Remove non ASCII text
       2. Make look Pretty
       3. add extra features (count)
       4. Maybe analysis?
       5. make it display on first click

"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import json
import pandas as pd
from pandas import DataFrame
from twython import Twython
import webbrowser
import urllib.request

from ui_Main import Ui_Main


class Main(QMainWindow, Ui_Main):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.index1 = 0

        self.submitBtn.clicked.connect(self.OpenWindow1)
        self.linkBtn.clicked.connect(self.openLink)

    def OpenWindow1(self):

        self.QtStack.setCurrentIndex(1)
        query = self.query.text()
        geo = self.query.text()
        self.getData(query, geo)
        self.nextBtn.clicked.connect(self.setLabel)

    def getData(self, queryT, geoT):
        with open("twitter_creds.JSON", "r") as file:
            creds = json.load(file)

        # Instantiate an object
        python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'], creds['ACCESS_TOKEN'],
                                creds['ACCESS_SECRET'])

        geocode = geoT
        queryI = queryT

        geocode = '40.006038,-105.257716,10mi'  # latitude,longitude,distance(mi/km)
        queryI = 'fuck'
        count = 10

        # make a Dict that has all fo the categorizes

        self.dict_ = {'user': [], 'username': [], 'HomeTown': [], 'Bio': [], 'ProfilePicURL': [], 'text': [], 'geo_E': [],
                 'location': [], 'coordinates': [], 'date': [], 'place': [], 'ID': []}

        # parse through the JSON and set it up so that it's in columns for Excel

        for status in \
                python_tweets.search(q=queryI, geocode=geocode, count=count, include_entities=True,
                                     tweet_mode='extended')[
                    'statuses']:
            self.dict_['user'].append(status['user']['name'])
            self.dict_['username'].append(status['user']['screen_name'])
            self.dict_['Bio'].append(status['user']['description'])
            self.dict_['HomeTown'].append(status['user']['location'])
            self.dict_['ProfilePicURL'].append(status['user']['profile_image_url'])
            idStr = str(status['id'])
            twitterLi = "https://twitter.com/user/status/"
            specTweetLi = twitterLi + idStr
            self.dict_['ID'].append(specTweetLi)

            self.dict_['text'].append(status['full_text'])
            self.dict_['geo_E'].append(
                status['user']['geo_enabled'])  # lets us know if another tweet from user might give us a location.
            self.dict_['location'].append(status['user']['location'])
            self.dict_['coordinates'].append(status['coordinates'])
            var4 = str(status['place'])
            index = var4.find('full_name')
            self.dict_['place'].append(var4[(index + 11):(index + 30)])
            self.dict_['date'].append(status['created_at'])

        # Structure data in a pandas DataFrame for easier writing to Excel
        df: DataFrame = pd.DataFrame(self.dict_)
        df.sort_values(by='date', inplace=True, ascending=True)
        df.to_csv('out.csv', float_format='%f')

        # make a file with the entire JSON format
        Sfile = str(
            python_tweets.search(q=queryI, geocode=geocode, count=count, include_entities=True, tweet_mode='extended'))
        f = open('JSON.txt', 'w')
        f.write(Sfile)
        f.close()

    def openLink(self):
        webbrowser.open(self.dict_['ID'][self.index1-1])  # Go to example.com

    def setLabel(self):
        self.userL.setText(self.dict_['user'][self.index1])
        self.usernameL.setText(self.dict_['username'][self.index1])
        self.homeTownL.setText(self.dict_['HomeTown'][self.index1])
        self.bioL.setText(self.dict_['Bio'][self.index1])
        self.dateL.setText(self.dict_['date'][self.index1])
        self.textL.setText(self.dict_['text'][self.index1])
        self.index1 = self.index1+1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = Main()
    sys.exit(app.exec_())
