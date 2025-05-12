## 🚨 Scenario 1:
A hospital is testing patients for a rare but deadly disease. The test should detect the disease even if there's a slight chance of it. Missing a sick person is risky.

Question: Which metric is most important here — Precision, Recall, Accuracy, or F1-score?B

## ANSWER

✅ Correct Answer: Recall
Why?
If someone has the disease (i.e., actual positive), we must detect it.

False Negatives (FN) mean the test says “no disease”, but the person actually has it — very dangerous.

So we want a model that catches all real positive cases, even if it means some healthy people are incorrectly flagged (some FP).

🎯 Conclusion:
Focus on Recall when missing a real case is dangerous.

Even if we get some false alarms (FP), it's better than missing a true case (FN).

