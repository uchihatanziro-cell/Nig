Here is your updated **README.md** file.
The output is placed inside a fenced code block so GitHub will automatically display a **copy button**.

---

# Bayesian Network Inference for Infection Type Prediction

## Overview

This project performs probabilistic inference using a trained Bayesian Network to predict the probability of different infection types based on observed symptoms.

Inference is performed using `VariableElimination` from the `pgmpy` library.

---

## Evidence Used for Inference

The model computes:

* **Fever = 1** → Fever is present
* **Cough = 1** → Cough is present
* **BodyTemperature_Binned = 3** → High temperature (bin 3)

We compute:

[
P(InfectionType \mid Fever=1, Cough=1, BodyTemperature_Binned=3)
]

---

## Requirements

* Python 3.x
* pgmpy
* numpy
* pandas

Install dependencies:

```bash
pip install pgmpy numpy pandas
```

---

## Inference Code

```python
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel
import pandas as pd

# Assume 'model' is your already trained Bayesian Network

# Create inference engine
inference = VariableElimination(model)

# Query posterior probabilities
posterior = inference.query(
    variables=['InfectionType'],
    evidence={
        'Fever': 1,
        'Cough': 1,
        'BodyTemperature_Binned': 3
    }
)

print("Posterior probabilities for InfectionType given Fever=1, Cough=1, BodyTemperature_Binned=3:")
print(posterior)
```

---

## Output

You can copy the output directly using the copy button in the top-right corner of the code block below:

```text
Posterior probabilities for InfectionType given Fever=1, Cough=1, BodyTemperature_Binned=3:
+------------------+----------------------+
| InfectionType    |   phi(InfectionType) |
+==================+======================+
| InfectionType(0) |               0.1913 |
+------------------+----------------------+
| InfectionType(1) |               0.5468 |
+------------------+----------------------+
| InfectionType(2) |               0.2619 |
+------------------+----------------------+
```

---

## Interpretation

* **InfectionType(1)** → 54.68% (Most likely infection)
* **InfectionType(2)** → 26.19%
* **InfectionType(0)** → 19.13%

Given the observed symptoms, the model predicts **InfectionType(1)** as the most probable diagnosis.

---

## Conclusion

This Bayesian Network provides probabilistic diagnosis rather than deterministic classification, enabling more informed and uncertainty-aware decision making in medical prediction systems.

---
