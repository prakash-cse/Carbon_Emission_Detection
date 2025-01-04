from django.shortcuts import render
from django.http import JsonResponse
from .models import Industry, Household
from .carbon_calculator import CarbonFootprintCalculator

def calculate_footprint(request):
    if request.method == 'POST':
        data = request.POST
        calculator = CarbonFootprintCalculator()
        
        # Convert form data to appropriate types
        processed_data = {}
        
        if data.get('type') == 'industry':
            processed_data = {
                'name': data.get('name', ''),
                'electricity_consumption': float(data.get('electricity_consumption', 0)),
                'fuel_consumption': float(data.get('fuel_consumption', 0)),
                'waste_production': float(data.get('waste_production', 0)),
                'employee_count': int(data.get('employee_count', 0)),
                'production_volume': float(data.get('production_volume', 0))
            }
            
            try:
                footprint = calculator.calculate_industry_footprint(processed_data)
                
                # Save to database
                Industry.objects.create(**processed_data)
                
                # Calculate component breakdown for visualization
                components = {
                    'Electricity': processed_data['electricity_consumption'] * 0.85,
                    'Fuel': processed_data['fuel_consumption'] * 2.68,
                    'Waste': processed_data['waste_production'] * 0.5
                }
                
            except ValueError as e:
                return JsonResponse({'error': str(e)}, status=400)
                
        else:
            processed_data = {
                'address': data.get('address', ''),
                'electricity_consumption': float(data.get('electricity_consumption', 0)),
                'gas_consumption': float(data.get('gas_consumption', 0)),
                'vehicle_count': int(data.get('vehicle_count', 0)),
                'resident_count': int(data.get('resident_count', 0)),
                'waste_production': float(data.get('waste_production', 0))
            }
            
            try:
                footprint = calculator.calculate_household_footprint(processed_data)
                
                # Save to database
                Household.objects.create(**processed_data)
                
                # Calculate component breakdown for visualization
                components = {
                    'Electricity': processed_data['electricity_consumption'] * 0.85,
                    'Gas': processed_data['gas_consumption'] * 2.03,
                    'Vehicles': processed_data['vehicle_count'] * 2.31 * 365,
                    'Waste': processed_data['waste_production'] * 0.5
                }
                
            except ValueError as e:
                return JsonResponse({'error': str(e)}, status=400)
        
        return JsonResponse({
            'footprint': footprint,
            'components': components
        })
    
    return render(request, 'calculator.html')