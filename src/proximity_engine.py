import numpy as np

def calculate_haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculates the distance between two points on Earth in miles.
    """
    R = 3958.8 # Earth radius in miles
    phi1, phi2 = np.radians(lat1), np.radians(lat2)
    dphi = np.radians(lat2 - lat1)
    dlambda = np.radians(lon2 - lon1)
    
    a = np.sin(dphi/2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(dlambda/2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
    return R * c

def find_nearest_coe(physician_lat, physician_lon, coe_list):
    """
    Finds the closest Center of Excellence for a given physician.
    """
    distances = coe_list.apply(lambda row: calculate_haversine_distance(
        physician_lat, physician_lon, row['lat'], row['lon']), axis=1)
    return distances.min(), distances.idxmin()
