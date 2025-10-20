from flask import Blueprint, jsonify, request
from models import db
from models.atividade import Atividade


# Classe responsável por controlar as ações relacionadas as atividades
class AtividadeController:
    
    # Usando Blueprint para organinar Rotas
    atividade_bp = Blueprint('atividades', __name__)

    @staticmethod
    @atividade_bp.route('/', methods=['GET'])
    def listar_atividades():
        """
        Lista todas as atividades cadastradas no Banco de Dados.

        Retorna:
            - Se houver registros retorna JSON contendo a lista de atividade e código HTTP 200
            - Se não houver registros retorna JSON com mensagem de erro e código HTTP 404
        """

        # Consulta registros da tabela "Atividades" usando SQLAlchemy e salva em atividades
        atividades = Atividade.query.all()

        # Se houver atividades cadastradas
        if atividades:
            lista = []
            for atividade in atividades:
                # Converte para dicionario e adiciona na lista
                lista.append(atividade.para_dicionario())
            return jsonify(lista), 200
        # Se não houver atividades cadastradas
        else:
            mensagem = {"Erro": "Lista de Atividades Vazia!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    @atividade_bp.route('/<int:atividade_id>', methods=['GET'])
    def exibir_atividade(atividade_id):
        """
        Exibe os dados de uma atividade específica com base no ID informado

        Parâmetros:
            atividade_id (int): ID da atividade a ser consultada

        Retorna:
            - Se a atividade for encontrada retorna JSON com seus dados e código HTTP 200
            - Se não for encontrada retorna JSON com mensagem de erro e código HTTP 404
        """

        # Busca uma atividade pelo ID usando SQLAlchemy e salva em atividade 
        atividade = Atividade.query.get(atividade_id)

        # Se a atividade for encontrada
        if atividade:
            # Converte para dicionario e retorna como JSON
            return jsonify(atividade.para_dicionario()), 200
        # Se a atividade não existir no banco de dados
        else:
            mensagem = {"Erro": "Atividade Não Cadastrada!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    @atividade_bp.route('/<int:atividade_id>', methods=['DELETE'])
    def deletar_atividade(atividade_id):
        """
        Delete os atividade de uma nota específica com base no ID informado

        Parâmetros:
            atividade_id (int): ID da atividade a ser deletada

        Retorna:
            - Se a atividade for encontrada retorna JSON com mensagem confirmando a exclusão e código HTTP 200
            - Se não for encontrada retorna JSON com mensagem de erro e código HTTP 404
            - Se existir nota vinculada a atividade retorna JSON com mensagem de erro e código HTTP 409
        """

        # Busca uma atividade pelo ID usando SQLAlchemy e salva em atividade
        atividade = Atividade.query.get(atividade_id)

        # Se a atividade não for encontrada
        if atividade is None:
            mensagem = {"Erro": "Atividade Não Cadastrada!"}
            return jsonify(mensagem), 404
        
        # Se existir nota vinculada a atividade
        if atividade.notas:
           return jsonify({"Erro": "Atividade com Nota Vinculado!"}), 409
            
        # Deletar registro no Banco de Dados
        db.session.delete(atividade)
        db.session.commit()
            
        mensagem = {"Mensagem": "Atividade Deletada com Sucesso!"}
        return jsonify(mensagem), 200