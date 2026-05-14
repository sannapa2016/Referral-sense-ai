import pandas as pd

def build_physician_profile(claims_df):
    """
    Groups claims by NPI to find patterns of 'pre-diagnostic' symptoms.
    """
    # Count specific ICD-10 codes that are 'proxies' for the rare disease
    profile = claims_df.groupby('npi').agg({
        'proxy_symptom_claims': 'sum',
        'diagnostic_test_count': 'sum',
        'patient_volume': 'nunique'
    })
    
    # Calculate a density score: Proxies per Patient
    profile['referral_score'] = profile['proxy_symptom_claims'] / profile['patient_volume']
    return profile
