from flask import Blueprint, request, jsonify
from database.models.estufa import Estufa
 
estufa_route = Blueprint('estufa', __name__)


@estufa_route.route('/', methods=['POST'])
def criar_estufa():
    try:
        data = request.json
        
        new_estufa = Estufa.create(
            temperatura=data['temperatura'],
            umidade=data['umidade'],
            velocidade_fan=data['velocidade_fan'],
            status_lampada=data['status_lampada']
        )
        
        return jsonify(new_estufa.to_dict()), 201  
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@estufa_route.route('/<int:id>')
def obter_estufa_id(id):
    try:
        estufa = Estufa.get_by_id(id)
        
        if not estufa:
            return jsonify({"error": "Estufa não encontrada"}), 404  
        
        return jsonify(estufa.to_dict()), 200  
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@estufa_route.route('/')
def obter_estufa():
    try:
        estufa = Estufa.get()  
        if not estufa:
            return jsonify({"error": "Estufa não encontrada"}), 404
        return jsonify(estufa.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    


@estufa_route.route('/<int:id>', methods=['PUT'])
def atualizar_estufa(id):
    try:
        data = request.json
        estufa_editada = Estufa.get_by_id(id)
        
        if not estufa_editada:
            return jsonify({"error": "Estufa não encontrada"}), 404
        
        if 'temperatura' in data:
            estufa_editada.temperatura = data['temperatura']
        if 'umidade' in data:
            estufa_editada.umidade = data['umidade']
        if 'velocidade_fan' in data:
            estufa_editada.velocidade_fan = data['velocidade_fan']
        if 'status_lampada' in data:
            estufa_editada.status_lampada = data['status_lampada']
        
        estufa_editada.save()
        
        return jsonify(estufa_editada.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    

@estufa_route.route('/<int:id>', methods=['DELETE'])
def deletar_estufa(id):
    try:
        estufa = Estufa.get_by_id(id)
        
        if not estufa:
            return jsonify({"error": "Estufa não encontrada"}), 404
        
        estufa.delete_instance()
        return jsonify({"message": "Estufa deletada com sucesso"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400