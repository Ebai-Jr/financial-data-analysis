from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the financial analysis data
df = pd.read_csv('financial_analysis.csv')

# Store predefined questions and responses
responses = {}

# Query 1: Total revenue in 2025
for company in ['Microsoft', 'Apple', 'Tesla']:
    revenue = df[
        (df['Company'] == company) &
        (df['Year'] == 2025)
    ]['Total Revenue'].iloc[0]

    responses[f"What was {company}'s total revenue in 2025?"] = (
        f"{company}'s total revenue in 2025 was {revenue:,.0f}."
    )


# Query 2: Net income in 2025
for company in ['Microsoft', 'Apple', 'Tesla']:
    net_income = df[
        (df['Company'] == company) &
        (df['Year'] == 2025)
    ]['Net Income'].iloc[0]

    responses[f"What was {company}'s net income in 2025?"] = (
        f"{company}'s net income in 2025 was {net_income:,.0f}."
    )


# Query 3: Revenue change from 2024 to 2025
for company in ['Microsoft', 'Apple', 'Tesla']:
    revenue_growth = df[
        (df['Company'] == company) &
        (df['Year'] == 2025)
    ]['Revenue Growth (%)'].iloc[0]

    responses[f"How did {company}'s revenue change from 2024 to 2025?"] = (
        f"{company}'s revenue changed by {revenue_growth:.2f}% "
        f"from 2024 to 2025."
    )


# Query 4: Net income change from 2024 to 2025
for company in ['Microsoft', 'Apple', 'Tesla']:
    net_income_growth = df[
        (df['Company'] == company) &
        (df['Year'] == 2025)
    ]['Net Income Growth (%)'].iloc[0]

    responses[f"How did {company}'s net income change from 2024 to 2025?"] = (
        f"{company}'s net income changed by {net_income_growth:.2f}% "
        f"from 2024 to 2025."
    )


# Query 5: Average revenue from 2023 to 2025
for company in ['Microsoft', 'Apple', 'Tesla']:
    avg_revenue = df[
        df['Company'] == company
    ]['Total Revenue'].mean()

    responses[
        f"What was the average revenue for {company} from 2023 to 2025?"
    ] = (
        f"{company}'s average revenue from 2023 to 2025 "
        f"was {avg_revenue:,.2f}."
    )


# Chatbot function
def simple_chatbot(user_query):
    if user_query in responses:
        return responses[user_query]
    else:
        return "Sorry, I can only provide information on predefined queries."


# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    response = None
    user_query = ''

    if request.method == 'POST':
        user_query = request.form['user_query']
        response = simple_chatbot(user_query)

    return render_template(
        'index.html',
        response=response,
        user_query=user_query
    )


if __name__ == '__main__':
    app.run(debug=True)


# Boiler Plate for flask
#from flask import Flask, render_template, request

#app = Flask(__name__)

#@app.route('/')
#def home():
#    return render_template('index.html')

#if __name__ == '__main__':
#    app.run(debug=True)