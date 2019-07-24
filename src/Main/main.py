from src.Scraper.tweets_scraper import TweetScraper
from src.Database.database import Database
from src.Database.data_to_csv import CSV
from src.UIWidget.widget import UserInterface
from src.Database.PreProcessing import PreProcessing
from src.Database.data_to_csv import CSV
from src.Obj.TweetList import TweetList
from src.Obj.tweet import Tweet
import time
import urllib


def main():
    # TODO(luke-bhan): Move this to a `.env` or similar file
    api = "igiH98aVHuB4zsmwKlWEe6qYs"
    api_secret = "lvECXM12Yh7SKYCU6ge05m7dE8R8evdPiIIIcAje7lIruKjvmf"

    access_token = "1461054643-TZHKekB1XCxqssymTtjzB249dO2YmBNy9bTyzpR"
    acesss_token_secret = "UyeMbBlMRqHgqLJnwSSH6iGn01GYuqxceprJ1kWswnS2q"

    # Gather users
    api = TweetScraper(api, api_secret, access_token, acesss_token_secret)

    # TODO(luke-bhan): Move this to a `.env` or similar file
    db = Database('luke', 'password', '127.0.0.1', '5432')
    db_column_name = ['Id', 'Text', 'Username', 'Favorite_Count', 'Retweet_Count', 'Follower_Count', 'Date',
                      'Nlp_Score',
                      'Given_Score']
    db_column_type = ['INTEGER', 'VARCHAR', 'VARCHAR', 'INTEGER', 'INTEGER', 'INTEGER', 'VARCHAR', 'VARCHAR', 'INTEGER']

    db_user_column = ['Username']
    db_usre_type = ['VARCHAR']
    list = db.get_column_data('users', 'username')
    tweet_list = TweetList()
    for member in list:
        print(member)
        tweets = api.search(urllib.parse.urlencode('bitcoin btc bit #btc'), member[0])
        for json in tweets.data:
            print(tweets.data[json])
            tweet_list.insert_list(tweets)
    db.insert_tweet_list('bitcoin', tweet_list)

if __name__ == "__main__":
    main()
