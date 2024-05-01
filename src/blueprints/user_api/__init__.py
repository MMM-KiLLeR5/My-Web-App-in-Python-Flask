# blueprints/user_api/__init__.py
from flask import Blueprint, request
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import decode_token
from src.schemas.schemas import UserSchema, AuthSchema, ShareSchema, DataSchema
from src.Authorization.Authorization import Authorization as Auth
from src.User.HandleUser import HandleUser

user = Blueprint('user', __name__, url_prefix='/user_api')


@user.route('/check_token', methods=['POST'])
def protected():
    token = request.json.get('token')
    decoded_token = decode_token(token)  # Декодируем токен
    jwt_identity = decoded_token.get('sub')  # Получаем идентификатор пользователя из токена
    jwt_role = decoded_token.get('role')  # Получаем роль пользователя из токена
    data = {'username': jwt_identity, 'role': jwt_role}
    return data


@user.route('/register', methods=['POST'])
# @marshal_with(AuthSchema)
@use_kwargs(UserSchema)
def user_register(**kwargs):
    if HandleUser.is_user('username', kwargs['username']):
        return {"error": "User not found"}, 411
    if HandleUser.is_user('passport_id', kwargs['passport_id']):
        return {"error": "User not found"}, 409
    if HandleUser.is_user('phone_number', kwargs['phone_number']):
        return {"error": "User not found"}, 410
    HandleUser.create_user_account(**kwargs)
    return {'message': 'good'}, 200


@user.route('/login', methods=['POST'])
@marshal_with(AuthSchema)
@use_kwargs(UserSchema(only=('username', 'password')))
def user_login(**kwargs):
    ans = Auth.user_login(**kwargs)
    if ans is None:
        return {"error": "User not found"}, 401
    token = HandleUser.get_token(ans)
    return {'access_token': token}


@user.route('/data_of_users', methods=['POST'])
@use_kwargs(UserSchema(only=['username']))
@marshal_with(DataSchema)
def data_of_users(username):
    my_user = HandleUser.show_user_details(username)
    return my_user


@user.route('/share_gb/<string:username>', methods=['POST'])
@use_kwargs(ShareSchema(only=['phone_number', 'value']))
def share_gb(username, **kwargs):
    res = HandleUser.share_gb_with_friend(username, **kwargs)
    if res is None:
        return {"error": "There is no user with this phone_number"}, 409
    if not res:
        return {"error": "Not enough gb"}, 410
    return {'message': 'good'}, 200


@user.route('/share_minute/<string:username>', methods=['POST'])
@use_kwargs(ShareSchema(only=['phone_number', 'value']))
def share_minute(username, **kwargs):
    res = HandleUser.share_minute_with_friend(username, **kwargs)
    if res is None:
        return {"error": "There is no user with this phone_number"}, 409
    if not res:
        return {"error": "Not enough minute"}, 410
    return {'message': 'good'}, 200


@user.route('/buy_gb/<string:username>', methods=["POST"])
@use_kwargs(ShareSchema(only=['value']))
def buy_gb(username, value):
    res = HandleUser.handle_buy_gb(username, value)
    if not res:
        return {"error": "Not enough money"}, 406
    return {'message': 'Successed'}, 200


@user.route('/buy_minute/<string:username>', methods=["POST"])
@use_kwargs(ShareSchema(only=['value']))
def buy_minute(username, value):
    res = HandleUser.handle_buy_minute(username, value)
    if not res:
        return {"error": "Not enough money"}, 406
    return {'message': 'Successed'}, 200


@user.route('/deposit/<string:username>', methods=["POST"])
@use_kwargs(ShareSchema(only=['value']))
def deposit(username, value):
    HandleUser.deposit_money(username, value)
    return {'message': 'Successed'}, 200


@user.route('/pay_tariff/<string:username>', methods=["POST"])
def pay_tariff(username):
    res = HandleUser.user_pay_tariff(username)
    if not res:
        return {"error": "Not enough money"}, 406
    return {'message': 'Successed'}, 200


@user.route('/change_tariff/<string:username>', methods=["POST"])
@use_kwargs(ShareSchema(only=['tariff_id']))
def change_tariff(username, tariff_id):
    res = HandleUser.change_tariff(username, tariff_id)
    if res:
        return {"error": "Not such tariff"}, 406
    return {'message': 'Successed'}, 200
