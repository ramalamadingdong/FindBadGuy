"""
To Do: 1. Remove non ASCII text (COMPLETE)
       2. Make look Pretty (in Progress)
       3. Save the settings (Dark / Light) Theme
       4. Maybe analysis? (#ofTweets per User... ECT)
       5. make it display on first click (COMPLETE)
       6. Link to link (in tweet)
       7. Save button for tweets
       8. Text bigger in Tweet Text (COMPLETE)
       9. Make it Display Picture (COMPLETE)
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import json
import pandas as pd
from pandas import DataFrame
from twython import Twython
import webbrowser
from selenium import webdriver


from ui_Main import Ui_Main


class Main(QMainWindow, Ui_Main):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.pic = ""
        self.index1 = 0
        self.submitBtn.clicked.connect(self.OpenWindow1)
        self.linkBtn.clicked.connect(self.openLink)
    def OpenWindow1(self):

        self.QtStack.setCurrentIndex(1)
        query = self.query.text()
        geo = self.geo.text()
        self.getData(query, geo)
        self.nextBadGuy()
        self.nextBtn.clicked.connect(self.nextBadGuy)
        self.prevBtn.clicked.connect(self.prevBadGuy)
        self.showPic.clicked.connect(self.showPicture)

    def getData(self, queryT, geoT):
        with open("twitter_creds.JSON", "r") as file:
            creds = json.load(file)

        # Instantiate an object
        python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'], creds['ACCESS_TOKEN'],
                                creds['ACCESS_SECRET'])

        geocode = geoT.replace(" ", "")
        queryI = queryT

    #    geocode = '40.006038,-105.257716,10mi'  # latitude,longitude,distance(mi/km)
        print(geocode)
        count = 100

        # make a Dict that has all fo the categorizes

        self.dict_ = {'user': [], 'username': [], 'HomeTown': [], 'Bio': [], 'ProfilePicURL': [], 'text': [], 'geo_E': [],
                 'location': [], 'coordinates': [], 'date': [], 'place': [], 'ID': []}

        # parse through the JSON and set it up so that it's in columns for Excel

        for status in \
                python_tweets.search(q=queryI, geocode=geocode, count=count, include_entities=True,
                                     tweet_mode='extended')[
                    'statuses']:
            status['user']['name']        = self.strip_non_ascii(status['user']['name'])
            status['user']['screen_name'] = self.strip_non_ascii(status['user']['screen_name'])
            status['user']['description'] = self.strip_non_ascii(status['user']['description'])
            status['user']['location']    = self.strip_non_ascii(status['user']['location'])
            status['full_text']           = self.strip_non_ascii(status['full_text'])
            status['user']['location']    = self.strip_non_ascii(status['user']['location'])
            status['created_at']          = self.strip_non_ascii(status['created_at'])


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
            self.dict_['geo_E'].append(status['user']['geo_enabled'])  # lets us know if another tweet from user might give us a location.
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
        #f.write(Sfile)
        f.close()

    def openLink(self):
        webbrowser.open(self.dict_['ID'][self.index1-1])  # Go to example.com

    def nextBadGuy(self):

        self.showPic.setChecked(False)
        self.picL.hide()
        if not self.dict_['user']:
            choice = QtWidgets.QMessageBox.question(self, 'Error!',
                                                "No Tweets Found\n"
                                                "Check your Geo / Query and try again",
                                                    QtWidgets.QMessageBox.Ok)
        self.userL.setText(self.dict_['user'][self.index1])
        self.usernameL.setText(self.dict_['username'][self.index1])

        self.bioL.setText(self.dict_['Bio'][self.index1])
        self.textL.setText(self.dict_['text'][self.index1])

        self.dateL.setText(self.dict_['date'][self.index1])
        self.homeTownL.setText(self.dict_['HomeTown'][self.index1])

        self.geoL.setText(str(self.dict_['geo_E'][self.index1]))

        self.index1 = self.index1+1

        if self.darkBtn.isChecked():
            self.BackColor = "background-color: #002b36;"
            self.FontColor = "color: #fdf6e3"

            self.bioL.setStyleSheet(self.FontColor)
            self.textL.setStyleSheet(self.FontColor)

            self.dateL.setStyleSheet(self.FontColor)
            self.homeTownL.setStyleSheet(self.FontColor)

            self.usernameL.setStyleSheet(self.FontColor)
            self.userL.setStyleSheet(self.FontColor)


            self.geoL.setStyleSheet(self.FontColor)

            self.stack2.setStyleSheet(self.BackColor)

        elif not self.darkBtn.isChecked():

            self.BackColor = "background-color: #fdf6e3;"
            self.FontColor = "color: #002b36"

            self.textL.setStyleSheet(self.FontColor)
            self.dateL.setStyleSheet(self.FontColor)
            self.bioL.setStyleSheet(self.FontColor)
            self.homeTownL.setStyleSheet(self.FontColor)
            self.usernameL.setStyleSheet(self.FontColor)
            self.userL.setStyleSheet(self.FontColor)


            self.geoL.setStyleSheet(self.FontColor)

            self.stack2.setStyleSheet(self.BackColor)

    def prevBadGuy(self):

        self.index1 = self.index1 - 2

        self.showPic.setChecked(False)
        self.picL.hide()

        self.userL.setText(self.dict_['user'][self.index1])
        self.usernameL.setText(self.dict_['username'][self.index1])
        self.homeTownL.setText(self.dict_['HomeTown'][self.index1])
        self.bioL.setText(self.dict_['Bio'][self.index1])
        self.dateL.setText(self.dict_['date'][self.index1])
        self.textL.setText(str(self.dict_['text'][self.index1]))

        self.geoL.setText(str(self.dict_['geo_E'][self.index1]))

        self.index1 = self.index1+1

        if self.darkBtn.isChecked():

            self.BackColor = "background-color: #002b36;"
            self.FontColor = "color: #fdf6e3"

            self.textL.setStyleSheet(self.FontColor)
            self.dateL.setStyleSheet(self.FontColor)
            self.bioL.setStyleSheet(self.FontColor)
            self.homeTownL.setStyleSheet(self.FontColor)
            self.usernameL.setStyleSheet(self.FontColor)
            self.userL.setStyleSheet(self.FontColor)

            self.geoL.setStyleSheet(self.FontColor)

            self.stack2.setStyleSheet(self.BackColor)

        elif not self.darkBtn.isChecked():

            self.BackColor = "background-color: #fdf6e3;"
            self.FontColor = "color: #002b36"

            self.textL.setStyleSheet(self.FontColor)
            self.dateL.setStyleSheet(self.FontColor)
            self.bioL.setStyleSheet(self.FontColor)
            self.homeTownL.setStyleSheet(self.FontColor)
            self.usernameL.setStyleSheet(self.FontColor)
            self.userL.setStyleSheet(self.FontColor)

            self.geoL.setStyleSheet(self.FontColor)

            self.stack2.setStyleSheet(self.BackColor)

    def showPicture(self):

        if self.showPic.isChecked():

            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver", chrome_options=options)

            driver.set_window_size(1920, 1080)  # set the window size that you need
            self.index1 = self.index1 -1
            driver.get(self.dict_['ID'][self.index1])
            driver.save_screenshot('currentTweet.png')
            driver.quit()

            pixmap = QtGui.QPixmap('currentTweet.png')
            rect = QtCore.QRect(650, 100, 600, 500)
            cropped = pixmap.copy(rect)
            pic_reszied = cropped.scaled(380, 250)

            self.picL.show()
            self.picL.setPixmap(pic_reszied)
            self.index1 = self.index1 +1

        elif not self.showPic.isChecked():
            self.picL.hide()

    def strip_non_ascii(self, string):
        ''' Returns the string without non ASCII characters'''
        stripped = (c for c in string if 0 < ord(c) < 127)
        return ''.join(stripped)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = Main()
    sys.exit(app.exec_())
