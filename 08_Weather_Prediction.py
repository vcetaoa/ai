# Bayesian Weather Predictor

from collections import defaultdict

# Prior probabilities
P_weather = {
    "Rain": 0.3,
    "Sunny": 0.7
}

# Likelihoods: P(Evidence | Weather)
P_evidence_given_weather = {
    "Humidity=High": {"Rain": 0.8, "Sunny": 0.2},
    "Humidity=Low": {"Rain": 0.2, "Sunny": 0.8},
    "Pressure=High": {"Rain": 0.3, "Sunny": 0.7},
    "Pressure=Low": {"Rain": 0.7, "Sunny": 0.3}
}

def bayesian_inference(evidence):
    unnormalized_posteriors = defaultdict(float)

    # Calculate numerator: P(E|W) * P(W)
    for weather in P_weather:
        prob = P_weather[weather]
        for e in evidence:
            prob *= P_evidence_given_weather[e][weather]
        unnormalized_posteriors[weather] = prob

    # Normalization
    total = sum(unnormalized_posteriors.values())
    for weather in unnormalized_posteriors:
        unnormalized_posteriors[weather] /= total

    return dict(unnormalized_posteriors)

# Example evidence: High Humidity and Low Pressure
evidence = ["Humidity=High", "Pressure=Low"]
posterior = bayesian_inference(evidence)

print("Posterior Probabilities:")
for weather, prob in posterior.items():
    print(f"{weather}: {prob:.4f}")


# output:
# Posterior Probabilities:
# Rain: 0.8000
# Sunny: 0.2000

#Algo: 

# Algorithm: Bayesian Inference (Naive Bayes Classifier)

# Purpose: Predicts weather probabilities given observed evidence (humidity and pressure)

# Core Formula:
# P(Weather | Evidence) ∝ P(Evidence | Weather) * P(Weather)

# Why This Approach?
# Handles Uncertainty: Combines multiple evidence sources
# Interpretable: Clear probabilistic reasoning
# Extendable: Easy to add more weather factors (e.g., temperature)

# Complexity
# Time: O(n) for n evidence variables
# Space: O(1) (fixed probability tables)