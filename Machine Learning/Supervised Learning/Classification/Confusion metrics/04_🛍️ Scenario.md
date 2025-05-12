## 🛍️ Scenario 3:
You’re working for an online fraud detection system. If a fraud transaction is missed, the company could lose money. But if a normal transaction is wrongly marked as fraud, it just asks the user to verify — a small inconvenience.

In short:

Missing fraud = costly (False Negative)

Flagging genuine user = inconvenient (False Positive)

Question: Which metric should we focus on here — Precision, Recall, Accuracy, or F1-Score?


## here FN is dangerous , there for we will check recall which is FN / (TP+FN)

Breakdown:
False Negatives (FN) = Fraud that goes undetected → huge financial loss 💸

You’d rather catch every fraud, even if it means some normal users get flagged (FP).

Recall = TP / (TP + FN)
→ Out of all actual fraud cases, how many did we catch?

So, yes — minimize FN, and maximize Recall.

🎯 Final Note:
It’s okay if some normal transactions are wrongly flagged (FP), as long as we don’t miss a real fraud.

Just like disease detection, Recall is crucial in fraud detection.

