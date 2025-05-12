## 🧪 Scenario 2:
You are building an email spam classifier. If a good email (non-spam) is marked as spam, it goes to the spam folder and might be lost. We want to avoid wrongly marking a good email as spam.

Question: Which metric should you focus on?

## ✅ Correct Metric: Precision
Why?
We want to minimize False Positives (i.e., don’t wrongly classify good emails as spam).

Precision = TP / (TP + FP) → Out of the ones marked spam, how many are actually spam.

High precision = Few good emails wrongly flagged.

🎯 Conclusion:
When False Positives are harmful, focus on Precision.