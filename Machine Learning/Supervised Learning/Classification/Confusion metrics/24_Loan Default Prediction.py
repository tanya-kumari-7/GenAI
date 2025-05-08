Question 7: Loan Default Prediction
A financial model predicts whether a person will default on their loan.

Out of 1,200 customers:

300 actually defaulted on their loan

The model correctly predicted 250 defaults

It missed 50 defaults

It falsely predicted 100 non-defaulters as defaulters

The rest were correctly predicted as non-defaulters

Can you fill in the confusion matrix (TP, FP, TN, FN)?

Your turn!







You said:
TP:  250
FP: 100
TN: 800
FN: 50


ChatGPT said:
Excellent try, Tanya! You got TP, FP, and FN right — just a slight miscalculation on TN. Let's work it out together:

Total customers = 1,200

Actual defaulters = 300

So actual non-defaulters = 1,200 − 300 = 900

TP (correct default predictions) = 250

FN (missed defaulters) = 50

FP (non-defaulters incorrectly predicted as defaulters) = 100

TN = 900 − 100 = 800 ✅

So your confusion matrix is:

TP = 250

FP = 100

TN = 800

FN = 50