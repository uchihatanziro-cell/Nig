from pgmpy.inference import VariableElimination

# Create an instance of VariableElimination
inference = VariableElimination(model)

# Perform a query to calculate the posterior probabilities of InfectionType
# given evidence: Fever is present (1), Cough is present (1), and BodyTemperature_Binned is 3
# Note: Ensure the evidence values match the encoded/binned values from preprocessing.
# In our case, 'Fever' and 'Cough' are 0 for 'No' and 1 for 'Yes'.
# 'BodyTemperature_Binned' is an integer representing the bin.
query_result = inference.query(variables=['InfectionType'], evidence={'Fever': 1, 'Cough': 1, 'BodyTemperature_Binned': 3})

print("Posterior probabilities for InfectionType given Fever=1, Cough=1, BodyTemperature_Binned=3:")
print(query_result)
