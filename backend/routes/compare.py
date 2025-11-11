from flask import Blueprint, render_template, request, jsonify
from backend.models.motorcycle import Motorcycle, db
from sqlalchemy import or_

compare_bp = Blueprint('compare', __name__)

@compare_bp.route('/compare')
def compare_page():
    return render_template('compare.html')

@compare_bp.route('/api/search')
def search_motorcycles():
    query = request.args.get('q', '').lower()
    try:
        limit = int(request.args.get('limit', 10))
    except (ValueError, TypeError):
        limit = 10
    
    if not query:
        motorcycles = Motorcycle.query.limit(limit).all()
    else:
        motorcycles = Motorcycle.query.filter(
            or_(
                Motorcycle.brand.ilike(f'%{query}%'),
                Motorcycle.model.ilike(f'%{query}%')
            )
        ).limit(limit).all()
    
    return jsonify([{
        'id': m.id,
        'brand': m.brand,
        'model': m.model,
        'year': m.year
    } for m in motorcycles])

@compare_bp.route('/api/motorcycle/<int:id>')
def get_motorcycle(id):
    motorcycle = Motorcycle.query.get_or_404(id)
    return jsonify(motorcycle.to_dict())
