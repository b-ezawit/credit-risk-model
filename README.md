# Credit Scoring Business Understanding

## 1. How does the Basel II Accord's emphasis on risk measurement influence the need for an interpretable and well-documented model?

Basel II requires financial institutions to measure, monitor, and manage credit risk in a transparent and consistent manner. Because lending decisions directly affect regulatory capital requirements and financial stability, banks must be able to explain how risk estimates are generated. As a result, credit risk models should be interpretable, well-documented, and auditable. Regulators, auditors, and business stakeholders need to understand the factors influencing predictions and verify that the model operates fairly and reliably. A model that cannot be adequately explained may face regulatory challenges even if it achieves high predictive accuracy.

## 2. Without a direct "default" label, why is a proxy variable necessary, and what business risks does proxy-based prediction introduce?

In many real-world datasets, a direct indicator of customer default may not be available. In such situations, a proxy variable is created to approximate credit risk using observable behaviors such as prolonged delinquency, missed payments, or account inactivity. The proxy serves as a substitute target variable that allows model development to proceed.

However, proxy-based prediction introduces several risks. The proxy may not accurately represent true default behavior, leading to labeling errors and biased model outputs. If the proxy is poorly defined, the model may learn patterns that are unrelated to actual credit risk. This can result in incorrect lending decisions, increased financial losses, reduced customer trust, and potential regulatory concerns.

## 3. What are the key trade-offs between a simple, interpretable model and a high-performance model in a regulated financial context?

Simple models such as Logistic Regression combined with Weight of Evidence (WoE) transformations offer strong interpretability. They allow financial institutions to explain individual predictions, validate model behavior, and satisfy regulatory requirements more easily. These models are also simpler to monitor and maintain over time.

High-performance models such as Gradient Boosting often achieve better predictive accuracy by capturing complex non-linear relationships in the data. However, they are more difficult to interpret and explain to regulators, auditors, and business stakeholders. Additional explainability techniques may be required, increasing implementation complexity.

In regulated financial environments, organizations must balance predictive performance with transparency, fairness, governance, and compliance requirements. A slightly less accurate but highly interpretable model may sometimes be preferred over a more accurate but opaque model.
