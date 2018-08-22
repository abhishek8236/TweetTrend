# -*- coding: utf-8 -*-
#Working
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import datetime
import time
import os
#import gc
#gc.collect()

#print(os.stat("c:\\ttest\\tweetdata.json").st_size)
#print(2**10)
#10mb=10485760

def getdatetime():
    runDate= str(datetime.datetime.utcnow()).replace(" ","T").replace(":","").replace("-","").replace(".","_")
    return(str(runDate))


class TweetsListener( StreamListener ):
    def __init(self):
        self._file_index = 0
    
    def on_data(self, data):
        filename="c:\\ttest\\_tweetdata.json"
        new_file="c:\\ttest\\tweetdata_"+getdatetime()+".json"
        if os.path.exists(filename) and os.stat(filename).st_size > 102400:
            os.rename(filename, new_file)
        try:
            with open(filename, 'a') as f:
                f.write(data)
        except BaseException as e:
            print("Error on_data: %s" % str(e))
    def on_error(self, status):
        print(status)

def main():
    #Variables that contains the user credentials to access Twitter API 
    consumer_key = '<>'
    consumer_secret = '<>'
    access_token = '<>'
    access_secret = '<>'
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    delhi_region = [28.5251,76.5539,28.2422,77.2521]
    ams_region = [4.768552,52.316867,5.008689,52.422521]
    nj = [-76,38.5,-73.5,41.5]
    ####################################################################
    #Ref: https://boundingbox.klokantech.com/
    #################################################################
    try:
        twitter_stream = Stream( auth, TweetsListener() )
        twitter_stream.filter( track=['#trump'] )
        #twitter_stream.user_stream()
        #twitter_stream.filter(async=True )
        #twitter_stream.filter(locations=ams_region )
    except BaseException as e:
        print( "Streaming Stopped")

if __name__ == '__main__':
    main()

