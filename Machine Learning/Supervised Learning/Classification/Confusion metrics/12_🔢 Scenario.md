## 🔢 Scenario 7:
You're working on a review moderation system for an e-commerce website. You want to automatically remove abusive reviews. Removing a clean review by mistake hurts user trust, but leaving an abusive review is also not acceptable.

Which metric should you focus on?







You said:
## F1 score because here FN and FP both are dangerous which is 2* ( precision * recall) / ( precision + recall) 


ChatGPT said:
✅ Perfectly reasoned!

🛒 Review Moderation → F1 Score
False Positive (FP) = A clean review is wrongly removed → Hurts trust 😕

False Negative (FN) = An abusive review is left visible → Harms platform quality 😠

Since both errors can damage the platform’s reputation, you need a balanced approach → F1 Score is the right choice.

You’re crushing this exercise! 🔥