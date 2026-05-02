import requests

url = 'http://localhost:2909/predict'
customer_id = 'xyz-123'

customer = {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 5,
    "monthlycharges": 79.85,
    "totalcharges": 5 * 79.85
}

response = requests.post(url, json=customer).json()
print(response)

if response['churn'] == True:
    print('send promo: %s' % customer_id)
else:
    print('not send promo: %s' % customer_id)