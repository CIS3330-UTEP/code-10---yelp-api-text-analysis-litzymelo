from yelpapi import YelpAPI
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter

# set up Yelp API
yelp_api_key = 'i2ktpopshc9TRmH7eOhYWjSPOsSGfgI5wv6wrBXIIoQcHQFJ1noZHN1npJAc_nR6udeO5eJptIQGRseS8fc6t5uHPBTtP0pnsPeT32N-v715nEcyWaObpJAYV_cxZHYx'
yelp_api = YelpAPI(yelp_api_key, timeout_s=3.0)

search_term = "ramen"
search_location = "El Paso, TX"
search_sort = "rating"
search_limit = 20

# search for top 20 ramen restaurants in El Paso, Texas and get their reviews
search_results = yelp_api.search_query(term=search_term, location=search_location, sort_by=search_sort, limit=search_limit)
businesses = []
for result in search_results['businesses']:
    business = {'Name': result['name'], 'rating': result['rating'], 'alias': result['alias']}
    review_response = yelp_api.reviews_query(id=business['alias'])
    business['reviews'] = [review['text'] for review in review_response['reviews']]
    businesses.append(business)

# clean the reviews by removing punctuation, stop words, and numbers
stop_words = set(stopwords.words('english'))
for business in businesses:
    clean_reviews = list(map(lambda review: ' '.join([token.lower() for token in word_tokenize(review) if token.isalpha() and token.lower() not in stop_words]), business['reviews']))
    business['clean_reviews'] = clean_reviews

# get the most common words and topics with ramen
all_words = [word for business in businesses for review in business['clean_reviews'] for word in word_tokenize(review)]
most_common_words = Counter(all_words).most_common(40)
print('Most common words:')
for word, count in most_common_words:
    print(f'{word}: {count}')

# sentiment scores for each review
sia = SentimentIntensityAnalyzer()
for business in businesses:
    sentiment_scores = [sia.polarity_scores(review)['compound'] for review in business['clean_reviews']]
    business['sentiment'] = sum(sentiment_scores) / len(sentiment_scores)

# overall customer satisfaction for each business
for business in businesses:
    if business['sentiment'] >= 0.5:
        satisfaction = 'positive'
    elif business['sentiment'] <= -0.5:
        satisfaction = 'negative'
    else:
        satisfaction = 'mixed'
    business['satisfaction'] = satisfaction

# printing the name, rating, and satisfaction for each ramen restaurant
for business in businesses:
    print(f"{business['Name']} ({business['rating']} stars): {business['satisfaction']} sentiment")

import csv

# sorting the businesses by rating
businesses.sort(key=lambda x: x['rating'], reverse=True)

# selecting top 10 businesses based on rating
top_businesses = sorted(businesses, key=lambda x: x['rating'], reverse=True)[:10]

# retrieving 3 reviews and their satisfaction from each of the top 10 ramen businesses
with open('Top_10_ramen_reviews.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Business Name', 'Rating', 'Review', 'Satisfaction'])

    for business in top_businesses:
        reviews = business['reviews'][:3]
        satisfaction = business['satisfaction']
        for review in reviews:
            writer.writerow([business['Name'], business['rating'], review, satisfaction])