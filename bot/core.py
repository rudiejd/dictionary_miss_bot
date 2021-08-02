import twint
from PyDictionary import PyDictionary
from io import StringIO
import sys
from datetime import datetime, timedelta
# this is a hack to figure out whether something wasn't found in the dictionary
ERROR_MESSAGE_HASH = hash('Error: The Following Error occured: list index out of range')

class Bot:
    def parse_tweet(self, tweet):
        print(tweet)
        for word in tweet['text'].split(' '):    
            old_stdout = sys.stdout 
            sys.stdout = error_capture = StringIO()
            # begin stdout capture in stringio
            PyDictionary.meaning(word)
            # end stdout capture
            sys.stdout = old_stdout
            if hash(error_capture.getvalue()) == ERROR_MESSAGE_HASH:
                self.non_dictionary_words[word] = self.non_dictionary_words.get(word, 0) + 1
        
    def find_words_in_tweets(self):
        twint_conf = twint.Config()
        twint_conf.Since = (datetime.now() - timedelta(hours = 1)).strftime("%Y-%m-%d %H:%M:%S")
        twint_conf.Until = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        twint.run.Search(twint_conf, self.parse_tweet)

        print(dict)





    def __init__(self):
        self.non_dictionary_words = dict()


if __name__ == "__main__":
    twitter_bot = Bot()
    twitter_bot.find_words_in_tweets()