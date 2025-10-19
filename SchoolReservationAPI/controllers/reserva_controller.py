from flask import Blueprint, jsonify, request
from models import db
from models.reserva import Reserva


# Classe responsável por controlar as ações relacionadas as reservas
class ReservaController:
    
    @staticmethod
    def listar_reservas():
        """
        Lista todas as reservas cadastradas no Banco de Dados.

        Retorna:
            - Se houver registros retorna JSON contendo a lista de reservas e código HTTP 200
            - Se não houver registros retorna JSON com mensagem de erro e código HTTP 404
        """

        # Consulta registros da tabela "Reserva" usando SQLAlchemy e salva em reservas
        reservas = Reserva.query.all()

        # Se houver reservas cadastradas
        if reservas:
            lista = []
            for reserva in reservas:
                # Converte para dicionario e adiciona na lista
                lista.append(reserva.para_dicionario())
            return jsonify(lista), 200
        # Se não houver reservas cadastradas
        else:
            mensagem = {"Erro": "Lista de Reservas Vazia!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    def exibir_reserva(reserva_id):
        """
        Exibe os dados de uma reserva específica com base no ID informado

        Parâmetros:
            reserva_id (int): ID da reserva a ser consultada

        Retorna:
            - Se a reserva for encontrada retorna JSON com seus dados e código HTTP 200
            - Se não for encontrada retorna JSON com mensagem de erro e código HTTP 404
        """

        # Busca uma reserva pelo ID usando SQLAlchemy e salva em reserva 
        reserva = Reserva.query.get(reserva_id)

        # Se a reserva for encontrada
        if reserva:
            # Converte para dicionario e retorna como JSON
            return jsonify(reserva.para_dicionario()), 200
        # Se a reserva não existir no banco de dados
        else:
            mensagem = {"Erro": "Reserva Não Cadastrada!"}
            return jsonify(mensagem), 404
        
    @staticmethod
    def deletar_reserva(reserva_id):
        """
        Delete os dados de uma reserva específica com base no ID informado

        Parâmetros:
            reserva_id (int): ID da reserva a ser deletada

        Retorna:
            - Se a reserva for encontrada retorna JSON com mensagem confirmando a exclusão e código HTTP 200
            - Se não for encontrada retorna JSON com mensagem de erro e código HTTP 404
        """

        # Busca uma reserva pelo ID usando SQLAlchemy e salva em reserva
        reserva = Reserva.query.get(reserva_id)

        # Se a reserva não for encontrada
        if reserva is None:
            mensagem = {"Erro": "Reserva Não Cadastrada!"}
            return jsonify(mensagem), 404
            
        # Deletar registro no Banco de Dados
        db.session.delete(reserva)
        db.session.commit()
            
        mensagem = {"Mensagem": "Reserva Deletada com Sucesso!"}
        return jsonify(mensagem), 200