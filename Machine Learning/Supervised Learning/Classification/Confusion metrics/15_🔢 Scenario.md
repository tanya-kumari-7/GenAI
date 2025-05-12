## 🔢 Scenario 10:
You're creating a loan defaulter prediction model for a bank. If a defaulter is predicted as safe, the bank may lose money. But if a safe customer is marked risky, it might just lose a potential customer.

Which metric should you focus on?

You should focus on Recall, not Precision.

Recall = TP / (TP + FN)
It answers: "Out of all actual defaulters, how many did we correctly catch?"
→ Higher Recall = fewer defaulters missed.

So the corrected answer:

We should focus on Recall because missing a defaulter (FN) is costlier than rejecting a good customer (FP).

