from marshmallow import Schema, fields, validate, ValidationError
from marshmallow.validate import Length, Range

class RegistrerControllers_schema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=3, max=20), data_key='name')
    lastname = fields.Str(required=True, validate=validate.Length(min=3, max=20), data_key='lastname')
    identificationCard = fields.Str(required=True, validate=validate.Length(min=1, max=11), data_key='identificationCard')
    phone = fields.Str(required=True, validate=validate.Length(max=11), data_key='phone')
    address = fields.Str(required=True, validate=validate.Length(max=50), data_key='address')
    email = fields.Email(required=True, validate=validate.Email(), data_key='email')
    password = fields.Str(required=True, validate=validate.Length(min=5, max=15), data_key='password')
    rol = fields.Str(required=True, validate=validate.Length(min=1), data_key='rol')


class LoginControllers_schema(Schema):
    email = fields.Email(required=True, validate=validate.Email(), data_key='email')
    password = fields.Str(required=True, validate=validate.Length(min=5, max=15), data_key='password')


class RegisterCustomerControllers_schema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=3,max=20), data_key='name')
    lastname = fields.Str(required=True, validate=validate.Length(min=3,max=20), data_key='lastname')
    identificationCard = fields.Str(required=True, validate=validate.Length(min=1, max=11), data_key='identificationCard')
    phone = fields.Str(required=True, validate=validate.Length(min=10,max=13), data_key='phone')
    dateBorn = fields.Str(required=True,validate=Length(min=1,max=10),data_key='dateBorn' )


class RegisterEquipmentControllers_schema(Schema):
    lineNumber = fields.Str(requiered=True,  validate=validate.Length(min=10, max=13), data_key='lineNumber')
    serial = fields.Str(required=True,validate=validate.Length(max=20), data_key='serial')
    imei = fields.Str(required=True, validate=validate.Length(max=20), data_key='imei')
    trademark = fields.Str(required=True, data_key='trademark')
    state = fields.Boolean(required=True,data_key='state')


class ManageLineControllers_schema(Schema):
    number_line = fields.Str(requiered=True,validate=validate.Length(min=10, max=13), data_key='numberLine')
    customer_dentification_card = fields.Str(required=True, validate=validate.Length(max=12), data_key='customerIdentificationCard')
    state = fields.Boolean(required=True, data_key='state')


class ManageLineControllers_put_schema(Schema):
    line = fields.Str(requiered=True,  validate=validate.Length(min=10, max=13), data_key='line2')
    personID = fields.Str(required=True, validate=validate.Length(max=12), data_key='personID')
    state = fields.Boolean(required=True, data_key='state')

class ManageLineControllers_get_schema(Schema):
    phone=fields.Str(required=True,  validate=validate.Length(min=10,max=13), data_key='phone' )

class     ManageBillControllers_get_Schema(Schema):
    line = fields.Str(required=True,  validate=validate.Length(min=10,max=13), data_key='line')


class ManageBillControllers_delete_Schema(Schema):
    line = fields.Str(required=True,  validate=validate.Length(min=10, max=13), data_key='line')
