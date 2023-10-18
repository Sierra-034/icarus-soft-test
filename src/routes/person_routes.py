from flask import Blueprint, request, jsonify
from models import Person, Bitacora

persons = Blueprint('person', __name__, url_prefix='/persons')

@persons.route('/searchByName', methods=['POST'])
def get_person():
    json = request.get_json(force=True)
    raw_name = json.get('nombre')
    lower_nombre_completo = json.get('nombre').lower()
    upper_nombre_completo = json.get('nombre').upper()
    lower_person = Person.query.filter_by(nombre_completo=lower_nombre_completo).first()
    upper_person = Person.query.filter_by(nombre_completo=upper_nombre_completo).first()
    
    bitacora: Bitacora
    if lower_person is None and upper_person is None:
        bitacora = Bitacora.new_bitacora(params=raw_name, response=False)
        bitacora.save()
        return jsonify({
            'encontrado': False,
        }), 404
    
    bitacora = Bitacora.new_bitacora(params=raw_name, response=True)
    bitacora.save()
    return jsonify({
        'encontrado': True,
    }), 200

@persons.route('/insertName', methods=['POST'])
def insert_person():
    json = request.get_json(force=True)
    lower_nombre_completo = json['nombre'].lower()
    person_instance = Person(nombre_completo=lower_nombre_completo)

    if person_instance.save():
        return jsonify({
            'message': 'Successful operation'
        }), 201
    
    return jsonify({
        'message': 'Operation failed'
    }), 500
