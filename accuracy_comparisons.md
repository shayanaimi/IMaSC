|   | INSTRUMENT  | SPACECRAFT  | Both  |
|---|---|---|---|
| Curve training  | 0.63  | 0.62  | 0.63  |
| Batch training  | 0.657  | 0.594  | 0.636  |

Note: Accuracy decreases in the last 25% for INSTRUMENT and when training both. It increases when training SPACECRAFT.
This is using the en_core_web_sm model.


Using a blank:en model, we get the following:

|   | INSTRUMENT  | SPACECRAFT  | Both  |
|---|---|---|---|
| Batch training  | 0.593  | 0.562  | 0.564  |