from flask import Blueprint, jsonify, request
from models import db
from models.nota import Nota


# Classe responsável por controlar as ações relacionadas as notas
class NotaController:
    
    @staticmethod
    def listar_notas():
        """
        Lista todas as notas cadastradas no Banco de Dados.

        Retorna:
            - Se houver registros retorna JSON contendo a lista de notas e código HTTP 200
            - Se não houver registros retorna JSON com mensagem de erro e código HTTP 404
        """

        # Consulta registros da tabela "Notas" usando SQLAlchemy e salva em notas
        notas = Nota.query.all()

        # Se houver notas cadastradas
        if notas:
            lista = []
            for nota in notas:
                # Converte para dicionario e adiciona na lista
                lista.append(nota.para_dicionario())
            return jsonify(lista), 200
        # Se não houver notas cadastradas
        else:
            mensagem = {"Erro": "Lista de Notas Vazia!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    def exibir_nota(nota_id):
        """
        Exibe os dados de uma nota específica com base no ID informado

        Parâmetros:
            nota_id (int): ID da nota a ser consultada

        Retorna:
            - Se a nota for encontrada retorna JSON com seus dados e código HTTP 200
            - Se não for encontrada retorna JSON com mensagem de erro e código HTTP 404
        """

        # Busca uma nota pelo ID usando SQLAlchemy e salva em nota 
        nota = Nota.query.get(nota_id)

        # Se a nota for encontrada
        if nota:
            # Converte para dicionario e retorna como JSON
            return jsonify(nota.para_dicionario()), 200
        # Se a nota não existir no banco de dados
        else:
            mensagem = {"Erro": "Nota Não Cadastrada!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    def deletar_nota(nota_id):
        """
        Delete os dados de uma nota específica com base no ID informado

        Parâmetros:
            nota_id (int): ID da nota a ser deletada

        Retorna:
            - Se a nota for encontrada retorna JSON com mensagem confirmando a exclusão e código HTTP 200
            - Se não for encontrada retorna JSON com mensagem de erro e código HTTP 404
        """

        # Busca uma nota pelo ID usando SQLAlchemy e salva em nota
        nota = Nota.query.get(nota_id)

        # Se a nota não for encontrada
        if nota is None:
            mensagem = {"Erro": "Nota Não Cadastrada!"}
            return jsonify(mensagem), 404
            
        # Deletar registro no Banco de Dados
        db.session.delete(nota)
        db.session.commit()
            
        mensagem = {"Mensagem": "Nota Deletada com Sucesso!"}
        return jsonify(mensagem), 200