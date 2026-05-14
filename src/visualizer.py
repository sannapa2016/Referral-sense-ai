import matplotlib.pyplot as plt

def plot_access_deserts(physician_df, coe_df):
    """
    Plots physicians by referral score and maps CoE locations.
    Red zones = High score physicians in 'Access Deserts' (>100 miles from CoE).
    """
    plt.figure(figsize=(10, 6))
    
    # Plot Physicians colored by distance to CoE
    plt.scatter(physician_df['lon'], physician_df['lat'], 
                c=physician_df['dist_to_coe'], cmap='Reds', label='HCPs')
    
    # Plot CoEs as prominent stars
    plt.scatter(coe_df['lon'], coe_df['lat'], 
                marker='*', color='blue', s=200, label='CoEs')
    
    plt.title("Referral-Sense AI: Patient Access & Geographic Gaps")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.colorbar(label='Miles to Nearest Treatment Center')
    plt.legend()
    plt.savefig('docs/access_map.png')
