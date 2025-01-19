# Data-Cleaning-and-Analysis-for-Tweets InPoDa

Project InPoDa

This is a project that we developed together as a team of two.

Group members:

- Me
- My friend : DEBIANE Rayane, his github : https://github.com/xaevenn


## Project Summary:

This project aims to create a data processing and analysis platform (data cleaning and data analysis) called InPoDa.

The database used, named "aitweets.json," contains JSON dictionaries with tweets. Each tweet includes several pieces of information, which will be specified later in the file tweet.py, where the Tweet class defines the structure of each tweet.

We first proceed with a data cleaning/processing step, where we clean the data and extract useful information for analysis, such as mentions, hashtags, etc.
Important note: We considered that the author of the tweet will be represented by the tweet's ID (since no username is available in the database).
The result of this step will be a new JSON file containing data ready for analysis.

For sentiment extraction, we used the TextBlob module, and for topic extraction, we used the NLTK module with two linguistic resources: "brown" and "punkt."

Afterward, we use the Pandas module, which greatly facilitates data analysis. All analysis functions can be found in the file analyse.py.

Bugs/Issues: No issues to report.

## Data Cleaning and Analysis of Tweets

InPoDa offers a set of data processing operations, including:

- Identification of the tweet's author
- Extraction of the tweet's hashtag list
- Extraction of the users mentioned in the tweet
- Sentiment analysis of the tweet (the sentiment can be positive or negative). You can use the TextBlob module for this.
- Identification of the tweet's topics
  
InPoDa also provides additional data analysis operations:

- Top K hashtags (K is a user-defined parameter)
- Top K users
- Top K mentioned users
- Top K topics
- Number of tweets per user
- Number of tweets per hashtag
- Number of tweets per topic
- All tweets from a specific user
- All tweets mentioning a specific user
- Users mentioning a specific hashtag
- Users mentioned by a specific user
  
These operations allow for in-depth analysis of tweet data, from sentiment and topic extraction to detailed user and hashtag insights.

### Future Improvements:

Add the ability to import a new database directly from the graphical interface.
Replace TextBlob with a custom AI model that we will develop ourselves.


### References:

StackOverflow + ChatGPT: for debugging the program and creating analysis functions.


## Important notes for launching the program:

The program uses the following modules:

- pandas
- nltk
- textblob
- matplotlib
- gradio
- json
- re
- os

Some of these modules (json, re, os) are already included by default if you have a recent version of Python. For the others, please make sure they are properly installed on your machine. Thank you.

The files must be in the same folder.


