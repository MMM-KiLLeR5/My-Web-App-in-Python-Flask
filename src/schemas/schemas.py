from marshmallow import Schema, validate, fields


class AdminSchema(Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True, validate=[
        validate.Length(max=250)])
    last_name = fields.String(required=True, validate=[validate.Length(max=250)])
    birth_date = fields.String(required=True, validate=[
        validate.Length(max=250)])
    passport_id = fields.String(required=True, validate=[
        validate.Length(max=500)])
    sex = fields.String(required=True, validate=[
        validate.Length(max=250)])
    username = fields.String(required=True, validate=[
        validate.Length(max=250)])
    password = fields.String(required=True, validate=[
        validate.Length(max=250)])
    phone_number = fields.String(required=True, validate=[
        validate.Length(max=250)])


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    first_name = fields.String(required=True, validate=[
        validate.Length(max=250)])
    birth_date = fields.String(required=True, validate=[
        validate.Length(max=250)])
    last_name = fields.String(required=True, validate=[validate.Length(max=250)])

    passport_id = fields.String(required=True, validate=[
        validate.Length(max=500)])
    sex = fields.String(required=True, validate=[
        validate.Length(max=250)])
    username = fields.String(required=True, validate=[
        validate.Length(max=250)])
    password = fields.String(required=True, validate=[
        validate.Length(max=250)])
    phone_number = fields.String(required=True, validate=[
        validate.Length(max=250)])

    tariff_id = fields.Integer(required=True)
    gb = fields.Integer(required=False)
    minutes = fields.Integer(required=False)
    balance = fields.Integer(required=False)


class TariffSchema(Schema):
    id = fields.Integer(dump_only=True)
    cost_one_gb = fields.Integer(required=True)
    cost_one_minute = fields.Integer(required=True)
    gb = fields.Integer(required=True)
    minute = fields.Integer(required=True)
    price = fields.Integer(required=True)


class AuthSchema(Schema):
    access_token = fields.String(dump_only=True)
    message = fields.String(dump_only=True)


class ShareSchema(Schema):
    phone_number = fields.String(required=True, validate=[
        validate.Length(max=250)])
    value = fields.Integer(required=True)
    tariff_id = fields.Integer()


class DataSchema(Schema):
    gb = fields.Integer(required=False)
    user_minutes = fields.Integer(required=False)
    balance = fields.Integer(required=False)
    cost_one_gb = fields.Integer(required=True)
    cost_one_minute = fields.Integer(required=True)
    user_gbs = fields.Integer(required=True)
    minute = fields.Integer(required=True)
    price = fields.Integer(required=True)


class StockMarketSchema(Schema):
    id = fields.Integer(dump_only=True)
    cost = fields.Integer(required=True)


class StockMarketMin(StockMarketSchema):
    min = fields.Integer(required=True)


class StockMarketGB(StockMarketSchema):
    gb = fields.Integer(required=True)
