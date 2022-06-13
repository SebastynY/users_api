from flask import request
from flask_restful import Resource
from http import HTTPStatus

from custom_type.type import F
from models.user import User, user_list


class UserListResource(Resource):
    @staticmethod
    def get() -> tuple[dict[str, list], int]:
        data = [user.data for user in user_list if user.identification]
        return {'data': data, 'status': HTTPStatus.OK}, HTTPStatus.OK

    @staticmethod
    def post() -> tuple[dict[str, int], int]:
        data = request.get_json()
        user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            age=data['age'],
            email=data['email'],
        )
        user_list.append(user)
        return user.data, HTTPStatus.CREATED


class UserResource(Resource):
    @staticmethod
    def get(user_id) -> F:
        user = next((user for user in user_list if user.id == user_id and user.identification), None)
        if user is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND
        return user.data, HTTPStatus.OK

    @staticmethod
    def put(user_id) -> tuple[dict[str, str], int]:
        data = request.get_json()
        user = next((user for user in user_list if user.id ==
                     user_id), None)
        if user is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.age = data['age']
        user.email = data['email']
        return user.data, HTTPStatus.OK


class UserIdentificationResource(Resource):
    @staticmethod
    def put(user_id) -> tuple[dict[str, str], int]:
        user = next((user for user in user_list if user.id ==
                     user_id), None)
        if user is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND
        user.identification = True
        return {}, HTTPStatus.NO_CONTENT

    @staticmethod
    def delete(user_id) -> tuple[dict[str, str], int]:
        user = next((user for user in user_list if user.id ==
                     user_id), None)
        if user is None:
            return {'message': 'user not found'}, HTTPStatus.NOT_FOUND
        user.identification = False
        return {}, HTTPStatus.NO_CONTENT
