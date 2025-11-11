import pandas as pd
from backend.models.motorcycle import db, Motorcycle
import os

def safe_float(value):
    if pd.isna(value):
        return None
    try:
        if isinstance(value, str):
            value = value.replace(',', '')
        return float(value)
    except (ValueError, TypeError):
        return None

def safe_int(value):
    if pd.isna(value):
        return None
    try:
        if isinstance(value, str):
            value = value.replace(',', '')
        return int(float(value))
    except (ValueError, TypeError):
        return None

def load_motorcycles_from_csv(csv_path='data/motorcycles.csv'):
    if Motorcycle.query.first() is not None:
        print("Database already loaded with motorcycles. Skipping CSV import.")
        return
    
    if not os.path.exists(csv_path):
        print(f"CSV file not found at {csv_path}")
        return
    
    print(f"Loading motorcycles from {csv_path}...")
    df = pd.read_csv(csv_path)
    
    count = 0
    for _, row in df.iterrows():
        motorcycle = Motorcycle(
            brand=row.get('Brand'),
            model=row.get('Model'),
            year=safe_int(row.get('Year')),
            category=row.get('Category'),
            rating=safe_float(row.get('Rating')),
            displacement=safe_float(row.get('Displacement (ccm)')),
            power=safe_float(row.get('Power (hp)')),
            torque=safe_float(row.get('Torque (Nm)')),
            engine_cylinder=row.get('Engine cylinder'),
            engine_stroke=row.get('Engine stroke'),
            gearbox=row.get('Gearbox'),
            bore=safe_float(row.get('Bore (mm)')),
            stroke=safe_float(row.get('Stroke (mm)')),
            fuel_capacity=safe_float(row.get('Fuel capacity (lts)')),
            fuel_system=row.get('Fuel system'),
            fuel_control=row.get('Fuel control'),
            cooling_system=row.get('Cooling system'),
            transmission_type=row.get('Transmission type'),
            dry_weight=safe_float(row.get('Dry weight (kg)')),
            wheelbase=safe_float(row.get('Wheelbase (mm)')),
            seat_height=safe_float(row.get('Seat height (mm)')),
            front_brakes=row.get('Front brakes'),
            rear_brakes=row.get('Rear brakes'),
            front_tire=row.get('Front tire'),
            rear_tire=row.get('Rear tire'),
            front_suspension=row.get('Front suspension'),
            rear_suspension=row.get('Rear suspension'),
            color_options=row.get('Color options')
        )
        db.session.add(motorcycle)
        count += 1
        
        if count % 1000 == 0:
            db.session.commit()
            print(f"Loaded {count} motorcycles...")
    
    db.session.commit()
    print(f"Successfully loaded {count} motorcycles into the database!")
