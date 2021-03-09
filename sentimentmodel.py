from nltk.corpus import twitter_samples,stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag # it tells what kind that word is ? whether it is verb, adjective etc
import re
import numpy as np
import random
from sklearn.model_selection import train_test_split
from nltk import NaiveBayesClassifier


def clean_data(token):
    return [item for item in token if not item.startswith('@') and not item.startswith('http')]

def to_lower(token):
    return [item.lower() for item in token]

def lemmatize(token):
    lemmatizer = WordNetLemmatizer()

    result = []
    for item, tag in pos_tag(token):
        if tag[0].lower() in "nva": #nva : noun, verb, adjective
            result.append(lemmatizer.lemmatize(item, tag[0].lower()))
        else:
            result.append((lemmatizer.lemmatize(item)))

    return result

def stopwordRemoval(token, stop_words):
    return [item for item in token if item not in stop_words]

def transform_features(token):
    feature_set = {}
    for feature in token:
        if feature not in feature_set:
            feature_set[feature] = 0
        feature_set[feature] += 1
    return feature_set



def main():
    # gathering tweets
    positive_tweets = twitter_samples.tokenized('positive_tweets.json')
    negative_tweets = twitter_samples.tokenized('negative_tweets.json')
    stop_words = stopwords.words('english')
    # cleaning data
    positive_tweet = [ stopwordRemoval(lemmatize(clean_data(to_lower(item))),stop_words) for item in positive_tweets]
    negative_tweet = [ stopwordRemoval(lemmatize(clean_data(to_lower(item))), stop_words) for item in negative_tweets]
    #print((positive_tweets[0]))
    

    # transform data
    positive_tweet = [(transform_features(token), "Positive") for token in positive_tweet]
    negative_tweet = [(transform_features(token), "Negative") for token in negative_tweet]
   # print(positive_tweet[0])
   # print(negative_tweet[0])


    # creating dataset
    dataset = positive_tweet + negative_tweet
    # we need to shuffle this dataset to make it trainable 
    dataset = random.shuffle(dataset)
    training_data = dataset[:7000]
    testing_data = dataset[:3000]
    # train, test = train_test_split()


    # train model 
    classifier = NaiveBayesClassifier.train(training_data)

if __name__ == "__main__":
    main()