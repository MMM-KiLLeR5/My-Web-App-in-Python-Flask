from flask import Blueprint, request
from flask_apispec import use_kwargs, marshal_with
from flask_jwt_extended import decode_token
from schemas.schemas import AdminSchema, TariffSchema, AuthSchema
from Authorization.Authorization import Authorization as Auth
from Admin.HandleAdmin import HandleAdmin
from Constants.Constant import AdminErrorMessages, AdminApprovalMessages

adm = Blueprint('adm', __name__, url_prefix='/admin')


@adm.route('/login', methods=['POST'])
@marshal_with(AuthSchema)
@use_kwargs(AdminSchema(only=('username', 'password')))
def admin_login(**kwargs):
    ans = Auth.admin_login(**kwargs)
    if ans is None:
        return {"error": AdminErrorMessages.NON_EXISTING_ADMIN}, 401
    token = HandleAdmin.get_token(ans)
    return {'access_token': token}


@adm.route('/check_token', methods=['POST'])
def protected():
    token = request.json.get('token')
    decoded_token = decode_token(token)  # Декодируем токен
    jwt_identity = decoded_token.get('sub')  # Получаем идентификатор пользователя из токена
    jwt_role = decoded_token.get('role')  # Получаем роль пользователя из токена
    data = {'username': jwt_identity, 'role': jwt_role}
    return data


@adm.route('/register', methods=['POST'])
@marshal_with(AuthSchema)
@use_kwargs(AdminSchema)
def admin_register(**kwargs):
    if HandleAdmin.is_admin('username', kwargs['username']):
        return {"error": AdminErrorMessages.NON_EXISTING_ADMIN}, 411
    if HandleAdmin.is_admin('passport_id', kwargs['passport_id']):
        return {"error": AdminErrorMessages.NON_EXISTING_ADMIN}, 409
    if HandleAdmin.is_admin('phone_number', kwargs['phone_number']):
        return {"error": AdminErrorMessages.NON_EXISTING_ADMIN}, 410
    token = HandleAdmin.create_admin_account(**kwargs)
    return {'access_token': token}, 200


@adm.route('/list_tariff', methods=['GET'])
# @jwt_required()
@marshal_with(TariffSchema(many=True))
def get_list_of_tariff():
    return HandleAdmin.get_list_of_tariffs()


@adm.route('/edit_tariff/<int:tariff_id>', methods=['POST'])
# @jwt_required()
@use_kwargs(TariffSchema)
def edit_tariffs(tariff_id, **kwargs):
    data = request.json
    if HandleAdmin.update_tariffs(tariff_id, **kwargs) is None:
        return {'error': AdminApprovalMessages.EDIT_TARIFF_SUCCESSFULLY}, 403
    return {'message': AdminApprovalMessages.EDIT_TARIFF_SUCCESSFULLY}


@adm.route('/list_tariff/<int:tariff_id>', methods=['GET'])
@marshal_with(TariffSchema)
def get_tariffs(tariff_id):
    tariff = HandleAdmin.get_tariff(tariff_id)
    if tariff is None:
        return {"error": AdminErrorMessages.NON_EXISTING_TARIFF}, 405
    return tariff, 201


@adm.route('/login/create_tariff', methods=['POST'])
# @jwt_required()
@use_kwargs(TariffSchema)
def create_tariffs(**kwargs):
    HandleAdmin.create_new_tariff(**kwargs)
    return {'message': AdminApprovalMessages.CREATE_TARIFF_SUCCESSFULLY}, 200
