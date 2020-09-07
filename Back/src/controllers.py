from flask.views import MethodView
from flask import jsonify, request
from model import consultant, customers, bill, lines
from marshmallow import Schema, fields, validate, ValidationError
from marshmallow.validate import Length, Range
import bcrypt
import jwt
from config import KEY_TOKEN_AUTH
import datetime
class LoginControllers_schema(Schema):
    #asi es tratandolo como diccionario
    #UserSchema = Schema.from_dict(
        #{"email": fields.Email(), "password": fields.Str(
            #required=True, validate=validate.Length(min=5, max=15), data_key='password')}
        #)
    #asi es tratandolos como campos de formularios
    email = fields.Email(
        required=True, validate=validate.Email(), data_key='email')
    password = fields.Str(required=True, validate=validate.Length(
        min=5, max=15), data_key='password')

class RegistrerControllers_schema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=3,max=20), data_key='name')
    lastname = fields.Str(required=True, validate=validate.Length(min=3, max=20), data_key='lastname')
    identificationCard = fields.Str(required=True, validate=validate.Length(min=1, max=11), data_key='identificationCard')
    phone = fields.Str(required=True, validate=validate.Length( max=11), data_key='phone')
    address = fields.Str(required=True, validate=validate.Length(max=50), data_key='address')
    email = fields.Email(required=True, validate=validate.Email(), data_key='email')
    password = fields.Str(required=True, validate=validate.Length( min=5, max=15), data_key='password')
    rol = fields.Str(required=True, validate=validate.Length(min=1), data_key='rol')

create_login_schema = LoginControllers_schema()
create_register_schema=RegistrerControllers_schema()
class RegisterConsultantControllers(MethodView):
    """
        Registro  del asesor
    """

    def post(self):
        content = request.get_json()
        errors = create_register_schema.load(content)
        print(content)
        print(errors)
        if errors:
            content = request.get_json()
            name = content.get("name")
            lastname = content.get("lastname")
            identificationCard = content.get("identificationCard")
            phone = content.get("phone")
            address = content.get("address")

            email = content.get("email")
            password = content.get("password")
            rol = content.get("rol")
            salt = bcrypt.gensalt()
            hash_pass = bcrypt.hashpw(bytes(str(password), encoding='utf-8'), salt)
            consultant[email] = {"name": name,
                                "lastname": lastname,
                                "id": identificationCard,
                                "phone": phone,
                                "address": address,
                                "email": email,
                                "password": hash_pass,
                                "rol": rol}
            return jsonify({"Status": "Register consultant successfully ",
                            "name ": name,
                            "password ": str(hash_pass)}), 200







class LoginControllers(MethodView):
    """
        Logeo para el usuario del sistema
    """
    
    def post(self):
        content=request.get_json()
        errors = create_login_schema.load(content)
        print(content)
        print(errors)
        if errors:
            content = request.get_json()
            email = content.get("email")
            password = bytes(str(content.get("password")), encoding='utf-8')
            if consultant.get(email):
                password_db = consultant[email]["password"]
                if bcrypt.checkpw(password, password_db):
                    # Se acude a jwt para generar un token codificado en formato json
                    encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow(
                    ) + datetime.timedelta(seconds=300), 'email': email}, KEY_TOKEN_AUTH, algorithm='HS256')
                    return jsonify({"Status": "Login exitoso", "auth": True, "token": encoded_jwt.decode()}), 200
                return jsonify({"Status": "Login incorrecto 22"}), 400
            return jsonify({"Status": "Login incorrecto 11"}), 400
        return jsonify({"Status": "Datos no validos reintente de nuevo"}),400
      




class RegisterCustomerControllers(MethodView):
    """
        Registro Clientes 
    """

    def post(self):
        if (request.headers.get('Authorization')):
            content = request.get_json()
            name = content.get("name")
            lastname = content.get("lastname")
            identificationCard = content.get("identificationCard")
            phone = content.get("phone")
            dateBorn = content.get("dateBorn")
            customers[phone] = {
                "name": name,
                "lastname": lastname,
                "identificationCard": identificationCard,
                "line": phone,
                "dateBorn": dateBorn,
            }
            print(customers)
            return jsonify({"Status": "Register customer successfully, Autorizacion por token valida ",
                            "name ": name,
                            "lastname ": lastname,
                            "identification card": identificationCard,
                            "date of born ": dateBorn,
                            "line ": phone}), 200
        return jsonify({"Status": "No ha enviado un token"}), 403


class RegisterEquipmentControllers(MethodView):
    """
        Registro equipo movil
    """

    def post(self):
        if (request.headers.get('Authorization')):
            content = request.get_json()
            lineNumber = content.get("lineNumber")
            serial = content.get("serial")
            imei = content.get("imei")
            trademark = content.get("trademark")
            state = content.get("state")
            return jsonify({"Status": "Proceso valido por autenticacion. Registro de equipo movil realizado con satisfaccion ",
                            "lineNumber ": lineNumber,
                            "serial ": serial,
                            "imei ": imei,
                            "trademark": trademark,
                            "state ": state}), 200
        return jsonify({"Status": "No ha enviado un token"}), 403


class ManageLineControllers(MethodView):
    """
        Example register
    """

    def post(self):
        if (request.headers.get('Authorization')):
            content = request.get_json()
            print(content)
            number_line = content.get("numberLine")
            customer_dentification_card = content.get(
                "customerIdentificationCard")
            state = content.get("state")
            return jsonify({"Status": "Register line successfully",
                            "number_line ": number_line, "state ": state,
                            "Customer Identification Card": customer_dentification_card}), 200
        return jsonify({"Status": 'no envio un token'}), 400

    def get(self, phone):
        if (request.headers.get('Authorization')):
            print(customers[phone])
            return jsonify({"Status": "Line Consulted Successfully",
                            'linea': phone,
                            'usuario': customers[phone]
                            }), 200
        return jsonify({"Status": "no se envio token"})

    def put(self, id_customer):
        if (request.headers.get('Authorization')):
            content = request.get_json(self)
            line = content.get("line2")
            personID= content.get("personID")
            state=content.get("state")
            return jsonify({"Status": "Line update successfully",
                            # "line":line,
                            # "idcustomer":identificationCard,
                            # "state":state
                            }), 200
        return jsonify({"Status" "no se envio un token"})


class ManageBillControllers(MethodView):
    """
        Example register
    """

    def get(self, line):
        if(request.headers.get('Authorization')):
            return jsonify({"Status": "Bill Consulted Successfully",
                            "usuario": customers[line],
                            "factura": bill[line]}), 200
        return jsonify({"Status": "error en el token"}), 400

    def delete(self, line):
        return jsonify({"Status": "Bill Deleted Successfully"}), 200
