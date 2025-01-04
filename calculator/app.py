import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from carbon_calculator import CarbonFootprintCalculator

def main():
    st.title('Carbon Footprint Calculator')
    
    calculator = CarbonFootprintCalculator()
    
    # Sidebar for type selection
    calculation_type = st.sidebar.selectbox(
        'Select Type',
        ('Industry', 'Household')
    )
    
    if calculation_type == 'Industry':
        st.header('Industry Carbon Footprint Calculator')
        
        # Input fields
        name = st.text_input('Industry Name')
        electricity = st.number_input('Electricity Consumption (kWh)', min_value=0.0)
        fuel = st.number_input('Fuel Consumption (L)', min_value=0.0)
        waste = st.number_input('Waste Production (kg)', min_value=0.0)
        employees = st.number_input('Number of Employees', min_value=0)
        production = st.number_input('Production Volume (units)', min_value=0.0)
        
        if st.button('Calculate Industry Footprint'):
            data = {
                'name': name,
                'electricity_consumption': electricity,
                'fuel_consumption': fuel,
                'waste_production': waste,
                'employee_count': employees,
                'production_volume': production
            }
            
            footprint = calculator.calculate_industry_footprint(data)
            
            st.success(f'Total Carbon Footprint: {footprint:.2f} kg CO2e')
            
            # Visualization
            components = {
                'Electricity': electricity * 0.85,
                'Fuel': fuel * 2.68,
                'Waste': waste * 0.5
            }
            
            fig = px.pie(
                values=list(components.values()),
                names=list(components.keys()),
                title='Carbon Footprint Components'
            )
            st.plotly_chart(fig)
            
    else:
        st.header('Household Carbon Footprint Calculator')
        
        # Input fields
        address = st.text_input('Address')
        electricity = st.number_input('Electricity Consumption (kWh)', min_value=0.0)
        gas = st.number_input('Gas Consumption (m³)', min_value=0.0)
        vehicles = st.number_input('Number of Vehicles', min_value=0)
        residents = st.number_input('Number of Residents', min_value=0)
        waste = st.number_input('Waste Production (kg)', min_value=0.0)
        
        if st.button('Calculate Household Footprint'):
            data = {
                'address': address,
                'electricity_consumption': electricity,
                'gas_consumption': gas,
                'vehicle_count': vehicles,
                'resident_count': residents,
                'waste_production': waste
            }
            
            footprint = calculator.calculate_household_footprint(data)
            
            st.success(f'Total Carbon Footprint: {footprint:.2f} kg CO2e')
            
            # Visualization
            components = {
                'Electricity': electricity * 0.85,
                'Gas': gas * 2.03,
                'Vehicles': vehicles * 2.31 * 365,
                'Waste': waste * 0.5
            }
            
            fig = px.pie(
                values=list(components.values()),
                names=list(components.keys()),
                title='Carbon Footprint Components'
            )
            st.plotly_chart(fig)

if __name__ == '__main__':
    main()