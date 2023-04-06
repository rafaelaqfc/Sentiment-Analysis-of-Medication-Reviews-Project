# Sentiment Analysis of Medication Reviews

This is my project about predicting sentiment analysis of medication reviews.

Introduction

Sentiment Analysis is an Natural Language Processing (NLP) application that classifies a text document or corpus’s emotional or sentimental tone, language, expression or point of view. Most of the time, emotions or attitudes can be positive, negative, somewhat positive and negative, mixed and so on. Therefore, sentiment analysis can help us to pick up and interpret the discursive patterns found in the language in order to understand and predict what are the evaluations and representations people are giving about a customer support, item bought, medication that has been taking, feedback analysis, market research, etc. In addition, classification tasks as this one can also give us clue about the audience by analyzing the demographics of the users.

Project Goals

The major goal of this project is to explore a dataset of medication reviews by analyzing the relationship between medications reviews, ratings given by their users, medications popularity throughout the time, testing hypothesis about the dataset distribution, among others. Similarly, it has the goal to create a machine learning model to predict the emotion or sentiment addressed in the users reviews or comments.

Project Steps

1. Data gathering/loading
2. Data exploration (EDA)
3. Text preprocessing
4. Feature engineering
5. Model building, evaluation and hyperparameter tunning
6. Model deployment

Expectations from this Project

This project is organized in modules and notebooks. Similarly, they are suplemented with theory, comments and coding cells. In regards of the repo organization, this repository is divided into the modules below:

1. Notebook 1 about data exploration (EDA) called `notebook_1_data_exploration.ipynb`;
2. Notebook 2 about data preprocessing called  `notebook_2_data_preprocessing.ipynb`;
3. Notebooks 3, 4 and 5 about feature engineering called `notebook_3_feature_engineering.ipynb`, `notebook_4_feature_engineering.ipynb` and `notebook_5_feature_engineering.ipynb`;
4. Notebook 6 and 7 about Random Forest Classifier modeling and testing called `notebook_6_data_modeling_with_random_forest_classifier.ipynb` and `notebook_7_data_testing_with_random_forest_classifier.ipynb`;
5. Notebook 8 and 9 about Naive Bayes Classifier modeling and testing called `notebook_8_data_modeling_with_multinomial_naive_bayes.ipynb` and `notebook_9_data_testing_with_multinomial_naive_bayes.ipynb`;
6. Notebook 10 about an ensemble model composed of Random Forest Classifier and Naive Bayes Classifier called `notebook_10_data_modeling_with_an_ensemble_model.ipynb`;
7. Notebook 11 about data modeling with Word2Vec called `notebook_11_data_modeling_with_word2vec.ipynb` (in progress);
8. Notebook 12 about data modeling with Long-Short Term Memory (LSTM) called `notebook_12_data_modeling_with_LSTM.ipynb` (in progress);
10. Under `models` folder, the models `mnbc_model.joblib` and `rfc_model.pkl`;
11. Uner `app` folder, the model `ensemble_model.pkl`, the model deployed in and API flask app called `app.py`, and the model testing file called `reviews_test_app_with_python.ipynb`.

