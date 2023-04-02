# KNN-based Chatbot Answering Science Trivia Questions

## Background
This is a POC for a simple chatbot based on KNN. The data used is limited, with no consideration for performance or parallel processing.  

Next, I plan to add automated testing for the data's relevancy, coverage, and accuracy. I also want to add assessments for data quality based on authority level and subject expert/machine learning evaluation.

## Design
1. Use KNN for semantic search to match asked question with question in master dataset
2. Use nmslib for KNN query
3. Use SentenceTransformer to generate vectors
4. Use all-MiniLM-L6-v2 as data model

## Data  
Number of data points: 50
Source: https://www.radiotimes.com/quizzes/pub-quiz-science/Format: CSV [Question, Answer]
Data is limited due to time and resource limitations.
Coverage of topics and quality of responses is determined by scope of questions and quality of answers.

