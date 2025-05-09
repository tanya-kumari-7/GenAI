🏠 Scenario: Home Loan Approval
You are part of a loan approval system, where you predict whether someone will get approved for a home loan.

Positive result = The system says "Approved".

Negative result = The system says "Not approved".

🔍 Situation:
A person actually is eligible for the loan (they qualify for approval).
But the system predicts that they will not be approved.

❓Question:
What is this?

True Positive (TP)

True Negative (TN)

False Positive (FP)

False Negative (FN)

And why?

Take your time!







You said:
FN


ChatGPT said:
✅ Correct!

Here’s why:

Actual condition: The person is eligible for the loan, meaning they should be approved (so it's a positive case).

Model’s prediction: The system predicted "Not approved" (a negative prediction).

✅ This is a False Negative (FN) because:
The system missed approving the person (it predicted No when the truth was Yes).

In simple terms:
The system wrongly predicted "Not approved" when the person actually was eligible. That’s a False Negative (FN).

Quick Recap:
Condition	Model says Yes	Model says No
Actually Yes	✅ True Positive (TP)	❌ False Negative (FN)
Actually No	❌ False Positive (FP)	✅ True Negative (TN)`