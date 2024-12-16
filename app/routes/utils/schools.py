from flask import Blueprint, request, jsonify
from app.models.school import School  # Asegúrate de que el modelo esté bien importado
from app.models import db

school_bp = Blueprint('school', __name__)

@school_bp.route('/school', methods=['GET'])
def get_school_by_cct():
    cct = request.args.get('cct', '').strip()
    if not cct:
        return jsonify({'error': 'CCT is required'}), 400

    school = db.session.query(School).filter_by(cct=cct).first()
    if school:
        return jsonify({'school': school.name, 'cct': school.cct})
    else:
        return jsonify({'school': None, 'cct': None})
@school_bp.route('/schools', methods=['GET'])
def get_all_schools():
    schools = db.session.query(School).all()
    result = [{'name': school.name, 'cct': school.cct} for school in schools]
    return jsonify(result)
