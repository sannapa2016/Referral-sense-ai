import pandas as pd

# 1. Load NPI-level claims data
# If 'data/physician_claims.csv' is not in your Colab environment,
# you will need to upload it. For demonstration, I will create dummy data.
try:
    claims_data = pd.read_csv('data/physician_claims.csv')
except FileNotFoundError:
    print("Required data file 'data/physician_claims.csv' not found. Creating dummy data for demonstration.")
    claims_data = pd.DataFrame({
        'npi': [1001, 1002, 1003, 1004, 1005],
        'proxy_symptom_claims': [10, 5, 12, 3, 8],
        'diagnostic_test_count': [5, 2, 7, 1, 4],
        'patient_volume': [20, 15, 25, 10, 18]
    })

# 2. Build features
npi_profiles = build_physician_profile(claims_data)

# 3. Predict 'Hidden' Referral Targets
# (Assuming we have a small training set of known referrers)
X = npi_profiles[['proxy_symptom_claims', 'diagnostic_test_count']]
# probabilities = rank_physicians(trained_model, X)

print("--- AI Physician Targeting Report ---")
print(npi_profiles.sort_values(by='referral_score', ascending=False).head(10))

import pandas as pd

# Mock CoE Data (Coordinates for major medical centers)
coe_data = pd.DataFrame({
    'coe_name': ['Mayo Clinic', 'Cleveland Clinic', 'Johns Hopkins'],
    'lat': [44.02, 41.50, 39.29],
    'lon': [-92.46, -81.67, -76.59]
})

# Example Physician Location (e.g., a Neurologist in rural Ohio)
dr_lat, dr_lon = 40.00, -82.00 

dist, coe_idx = find_nearest_coe(dr_lat, dr_lon, coe_data)
nearest_name = coe_data.loc[coe_idx, 'coe_name']

print(f"--- Access Barrier Analysis ---")
print(f"Nearest CoE: {nearest_name}")
print(f"Distance: {dist:.1f} miles")

if dist > 100:
    print("Action: High Travel Burden detected. Trigger Patient Travel Assistance Program.")
