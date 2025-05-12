## 🔹 QUICK OVERVIEW (Keep This as Reference)
Metric	Focuses On...	Formula	When Important
Accuracy	Overall correctness	(TP + TN) / (TP + FP + TN + FN)	When classes are balanced and cost of FP & FN is equal
Precision	How many predicted positives are correct	TP / (TP + FP)	When False Positives are costly (e.g., cancer false alarm)
Recall	How many actual positives are detected	TP / (TP + FN)	When False Negatives are costly (e.g., missing a disease case)
F1-Score	Balance between precision & recall	2 * (Precision * Recall) / (P + R)	When we need a balanced view between precision and recall