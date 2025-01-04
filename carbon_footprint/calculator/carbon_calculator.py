import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class CarbonFootprintCalculator:
    def __init__(self):
        self.industry_model = DecisionTreeRegressor(random_state=42)
        self.household_model = DecisionTreeRegressor(random_state=42)
        self.scaler = StandardScaler()
        
    def preprocess_industry_data(self, data):
        features = ['electricity_consumption', 'fuel_consumption', 
                   'waste_production', 'employee_count', 'production_volume']
        X = np.array([[float(row[f]) for f in features] for row in data])
        return self.scaler.fit_transform(X)
    
    def preprocess_household_data(self, data):
        features = ['electricity_consumption', 'gas_consumption',
                   'vehicle_count', 'resident_count', 'waste_production']
        X = np.array([[float(row[f]) for f in features] for row in data])
        return self.scaler.fit_transform(X)
    
    def calculate_industry_footprint(self, data):
        # Converting units to CO2 equivalent
        electricity_factor = 0.85  # kg CO2/kWh
        fuel_factor = 2.68  # kg CO2/L
        waste_factor = 0.5  # kg CO2/kg waste
        
        footprint = (
            data['electricity_consumption'] * electricity_factor +
            data['fuel_consumption'] * fuel_factor +
            data['waste_production'] * waste_factor
        )
        return footprint
    
    def calculate_household_footprint(self, data):
        electricity_factor = 0.85  # kg CO2/kWh
        gas_factor = 2.03  # kg CO2/m3
        vehicle_factor = 2.31  # kg CO2/L (assuming average fuel consumption)
        waste_factor = 0.5  # kg CO2/kg waste
        
        footprint = (
            data['electricity_consumption'] * electricity_factor +
            data['gas_consumption'] * gas_factor +
            data['vehicle_count'] * vehicle_factor * 365 +  # Yearly estimate
            data['waste_production'] * waste_factor
        )
        return footprint
