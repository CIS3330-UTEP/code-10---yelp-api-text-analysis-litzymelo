## CIS3330-CODE-10-Yelp-API-Text-Analysis

## Instructions

Text analysis allows the quantification of information from textual datasets. In this CODE assignment, you are asked to perform your first text analysis using data retrieved from the Yelp Fusion API. In this CODE assignment, your job is to provide initial insights about one or several businesses in the food industry.

## Deliverables

In a Word or PDF, deliver a report of your analysis. Your report must include the following sections.

1. Plan for data retrieval and analysis
  * Offer a quick summary of the insights you want to discover using the Yelp Fusion API
  * Explain the search parameters (e.g., term, location, sort criteria) that you plan to use
  * Explain how you plan to use that information from the Yelp Fusion API to provide the business insights you want to discover
  * Explain what text analysis (e.g., sentiment, most used words) you plan to use for obtaining the desired business insights

2. Text insights report
  * Report the results of your analysis
  * Offer a conclusion with the information you obtained from the analysis
  
You need to submit the report in Blackboard and in your code repository. Finally, **do not forget** to submit all the code you use for your analysis, and that will be needed to replicate your work in the code repository.

## Useful Python code

* `search_results = yelp_api.search_query(term='TERM', location='LOCATION', sort_by='CRITERIA', limit=#) # Replace all UPPERCASE values and pound sign accordingly`
* `review_response = yelp_api.reviews_query(id="ALIAS FOR BUSINESS") # Replace all UPPERCASE values accordingly`

## Useful resources

* Valence Aware Dictionary and sEntiment Reasoner - https://github.com/cjhutto/vaderSentiment
* Natural Language Toolkit - https://www.nltk.org/
