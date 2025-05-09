✅ Scenario 1: Email Spam Detection
Goal: Classify emails as "Spam" or "Not Spam".

Important: Avoid marking important emails as spam (False Positive).

Key Metric:

Precision – We care more that the predicted spam emails actually are spam.

Why? High FP (normal email marked as spam) is more annoying than missing a few spam emails (FN).

✅ Scenario 2: Cancer Detection (Medical Diagnosis)
Goal: Detect if a patient has cancer.

Important: Don’t miss actual cancer cases (False Negative is dangerous).

Key Metric:

Recall – We want to catch all actual positives (cancer cases), even if a few healthy people are wrongly flagged.

Why? FN (missed cancer) is life-threatening; FP leads to extra tests, which is acceptable.

✅ Scenario 3: Credit Card Fraud Detection
Goal: Detect fraudulent transactions.

Important: Balance between catching fraud and not bothering users unnecessarily.

Key Metric:

F1 Score – We want a balance between precision and recall.

Why? Fraud cases are rare (imbalanced data), and both FN (missed fraud) and FP (blocking a legit purchase) are costly.

✅ Scenario 4: Sentiment Analysis on Product Reviews
Goal: Predict if a review is positive or negative.

Important: Overall accuracy is fine for business analytics, unless you're filtering abusive content.

Key Metric:

Accuracy – If classes are balanced, accuracy gives a good measure.

Why? You want an overall picture, and false positives/negatives don't have severe consequences.

🎯 Quick Decision Guide:
Situation	Metric to Focus On
Cost of false positives is high	Precision
Cost of false negatives is high	Recall
Need a balance	F1 Score
Classes are balanced, equal cost	Accuracy

