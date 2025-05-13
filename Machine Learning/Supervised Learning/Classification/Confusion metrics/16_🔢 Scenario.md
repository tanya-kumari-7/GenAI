## 🔢 Scenario 11:
You're developing a spam email filter. You want to avoid marking important user emails as spam (e.g., job offers, OTPs). However, occasionally letting a spam email through is annoying but not dangerous.

Which metric should you focus on?

A. Precision
B. Recall
C. Accuracy
D. F1 Score

👉 Your turn: What's the correct answer and why?

You said:
## FP is not good , we should check for Precision which is FP/FP+TP
ChatGPT said:
✅ Absolutely right!

📬 Spam Email Detection → Precision
False Positive (FP) = Important email marked as spam → User misses something critical (bad).

False Negative (FN) = Spam email slips through → Just annoying, not critical.

Since the real harm comes from flagging good emails as spam, we want to minimize FP, which means maximizing Precision.

You’ve nailed 11 out of 11 — 🔥 on a roll!

############################
#############################################