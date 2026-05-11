## Credit Risk Scoring

This project builds a credit risk scoring model - the kind a bank would use to decide whether to approve or deny a loan application.

#### Problem overview
When a customer applies for a loan, the bank collects information such as income, loan amount requested, and other financial details. Instead of making that decision manually, a machine learning model can process that data and return a risk score: the probability that the customer will default on the loan. We use historical loan data where each record tells us:

> The customer's profile and loan details
> Whether they repaid the loan (`OK`) or defaulted (`DEFAULT`)

#### Framing as a classification problem
This is a binary classification task. The target variable y takes two values:

| Value     | Meaning                       |
|-----------|-------------------------------|
| 0         | Customer repaid the loan (OK) |
| 1         | Customer defaulted            |

Given a feature matrix `X` (customer information), the model learns to predict:

`g(xᵢ) → probability of default`

The output is a probability between 0 and 1, which the bank can use to set a threshold for approval or denial decisions.

---

The raw dataset is in the file **"CreditScoring.csv"** which contains 4455 rows and 14 columns:

<table>
<tbody>
<tr><td><b>1  Status</b></td> <td>credit status</td></tr>
<tr><td><b>2  Seniority</b></td> <td>job seniority (years)</td></tr>
<tr><td><b>3  Home</b></td> <td>type of home ownership</td></tr>
<tr><td><b>4  Time</b></td> <td>time of requested loan</td></tr>
<tr><td><b>5  Age</b></td> <td>client's age </td></tr>
<tr><td><b>6  Marital</b></td> <td>marital status </td></tr>
<tr><td><b>7  Records</b></td> <td>existance of records</td></tr>
<tr><td><b>8  Job</b></td> <td>type of job</td></tr>
<tr><td><b>9  Expenses</b></td> <td> amount of expenses</td></tr>
<tr><td><b>10 Income</b></td> <td> amount of income</td></tr>
<tr><td><b>11 Assets</b></td> <td> amount of assets</td></tr>
<tr><td><b>12 Debt</b></td> <td> amount of debt</td></tr>
<tr><td><b>13 Amount</b></td> <td> amount requested of loan</td></tr>
<tr><td><b>14 Price</b></td> <td> price of good</td></tr>
</tbody>
</table>
