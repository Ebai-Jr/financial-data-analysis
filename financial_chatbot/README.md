# Financial Analysis Chatbot

## 1. Project Overview

The Financial Analysis Chatbot is a simple data-driven chatbot developed using Python, Pandas, and Flask. The chatbot uses financial data for Microsoft, Apple, and Tesla covering the years 2023 to 2025. It provides predefined responses to common financial questions based on the analyzed dataset.

## 2. Technologies Used

* Python
* Pandas
* Flask
* HTML
* CSS
* JavaScript

## 3. How the Chatbot Works

The chatbot loads the `financial_analysis.csv` file using Pandas. The financial data is then used to generate a dictionary of predefined questions and their corresponding responses.

When a user enters a question through the Flask web interface, the question is sent to the Flask application. The `simple_chatbot()` function checks whether the user's question matches one of the predefined questions in the `responses` dictionary.

If a matching question is found, the chatbot returns the corresponding financial response. If the question does not match a predefined query, the chatbot informs the user that it can only provide information for predefined questions.

The web interface also provides clickable example questions to make it easier for users to interact with the chatbot.

## 4. Predefined Queries

The chatbot can answer the following types of questions:

1. What was the total revenue for a company in 2025?
2. What was the net income for a company in 2025?
3. How did a company's revenue change from 2024 to 2025?
4. How did a company's net income change from 2024 to 2025?
5. What was the average revenue for a company from 2023 to 2025?

The supported companies are:

* Microsoft
* Apple
* Tesla

## 5. Testing

The chatbot was tested using all five predefined query types for Microsoft, Apple, and Tesla. The responses were checked against the values contained in the financial analysis dataset.

Additional testing was performed using an unsupported question to confirm that the chatbot correctly handles queries outside its predefined functionality.

## 6. Limitations

The chatbot has several limitations:

* It only responds to predefined questions.
* The user's question must closely match the predefined wording.
* It cannot answer questions that were not included in the chatbot's response dictionary.
* It does not perform natural language understanding or generate new financial analysis dynamically.
* It currently covers only Microsoft, Apple, and Tesla.
* The financial dataset currently covers the years 2023 to 2025.
* The chatbot is a prototype and is intended for demonstration rather than professional financial decision-making.

## 7. Conclusion

The project demonstrates how financial data analyzed with Pandas can be connected to a simple interactive web application using Flask. The resulting chatbot provides an accessible interface for retrieving selected financial information and demonstrates the basic principles of combining data analysis, Python programming, and web development.
