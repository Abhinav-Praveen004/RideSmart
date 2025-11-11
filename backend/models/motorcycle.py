from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Motorcycle(db.Model):
    __tablename__ = 'motorcycles'
    
    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100))
    model = db.Column(db.String(200))
    year = db.Column(db.Integer)
    category = db.Column(db.String(100))
    rating = db.Column(db.Float)
    displacement = db.Column(db.Float)
    power = db.Column(db.Float)
    torque = db.Column(db.Float)
    engine_cylinder = db.Column(db.String(100))
    engine_stroke = db.Column(db.String(100))
    gearbox = db.Column(db.String(100))
    bore = db.Column(db.Float)
    stroke = db.Column(db.Float)
    fuel_capacity = db.Column(db.Float)
    fuel_system = db.Column(db.String(200))
    fuel_control = db.Column(db.String(100))
    cooling_system = db.Column(db.String(100))
    transmission_type = db.Column(db.String(100))
    dry_weight = db.Column(db.Float)
    wheelbase = db.Column(db.Float)
    seat_height = db.Column(db.Float)
    front_brakes = db.Column(db.String(100))
    rear_brakes = db.Column(db.String(100))
    front_tire = db.Column(db.String(100))
    rear_tire = db.Column(db.String(100))
    front_suspension = db.Column(db.String(200))
    rear_suspension = db.Column(db.String(200))
    color_options = db.Column(db.String(500))
    
    def to_dict(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'model': self.model,
            'year': self.year,
            'category': self.category,
            'rating': self.rating,
            'displacement': self.displacement,
            'power': self.power,
            'torque': self.torque,
            'engine_cylinder': self.engine_cylinder,
            'engine_stroke': self.engine_stroke,
            'gearbox': self.gearbox,
            'bore': self.bore,
            'stroke': self.stroke,
            'fuel_capacity': self.fuel_capacity,
            'fuel_system': self.fuel_system,
            'fuel_control': self.fuel_control,
            'cooling_system': self.cooling_system,
            'transmission_type': self.transmission_type,
            'dry_weight': self.dry_weight,
            'wheelbase': self.wheelbase,
            'seat_height': self.seat_height,
            'front_brakes': self.front_brakes,
            'rear_brakes': self.rear_brakes,
            'front_tire': self.front_tire,
            'rear_tire': self.rear_tire,
            'front_suspension': self.front_suspension,
            'rear_suspension': self.rear_suspension,
            'color_options': self.color_options
        }
