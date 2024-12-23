from flask import Blueprint, request, jsonify
from app.models.school import School
from app.models import db

school_bp = Blueprint('school', __name__, url_prefix='/api')

@school_bp.route('/schools', methods=['GET'])
def search_schools():
    cct_query = request.args.get('cct', '').strip()
    if not cct_query:
        return jsonify({'error': 'CCT is required'}), 400

    # Limitar resultados a 6 coincidencias
    schools = (
        db.session.query(School)
        .filter(School.cct.ilike(f'%{cct_query}%'))
        .limit(6)
        .all()
    )
    results = [{'name': school.name, 'cct': school.cct} for school in schools]
    return jsonify(results)

@school_bp.route('/schools/<cct>', methods=['GET'])
def get_school_by_cct(cct):
    school = db.session.query(School).filter_by(cct=cct).first()
    if school:
        return jsonify({'name': school.name, 'cct': school.cct})
    else:
        return jsonify({'error': 'School not found'}), 404

@school_bp.route('/schools', methods=['GET'])
def get_all_schools():
    schools = db.session.query(School).all()
    result = [{'name': school.name, 'cct': school.cct} for school in schools]
    return jsonify(result)
