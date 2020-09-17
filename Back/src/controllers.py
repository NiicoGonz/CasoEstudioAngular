from flask.views import MethodView
from flask import Flask, render_template, request, session, redirect, url_for, jsonify
from marshmallow import Schema, fields, validate, ValidationError
from marshmallow.validate import Length, Range
from validators import LoginControllers_schema, RegistrerControllers_schema, RegisterCustomerControllers_schema, RegisterEquipmentControllers_schema, ManageLineControllers_schema, ManageLineControllers_put_schema, ManageLineControllers_get_schema, ManageBillControllers_get_Schema, ManageBillControllers_delete_Schema
from model import session, User
from helpers import QueryToList
import bcrypt
import jwt
from config import KEY_TOKEN_AUTH
import datetime

create_register_schema=RegistrerControllers_schema()
create_login_schema = LoginControllers_schema()
create_RegisterCustomerControllers_schema = RegisterCustomerControllers_schema()
create_RegisterEquipmentControllers_schema = RegisterEquipmentControllers_schema()
create_ManageLineControllers_schema = ManageLineControllers_schema()
create_ManageLineControllers_put_schema = ManageLineControllers_put_schema()
create_ManageLineControllers_get_schema = ManageLineControllers_get_schema()
create_ManageBillControllers_get_Schema = ManageBillControllers_get_Schema()
create_ManageBillControllers_delete_Schema = ManageBillControllers_delete_Schema()
class RegisterConsultantControllers(MethodView):
    """ Registro  del asesor"""

    def post(self):
        content = request.get_json()
        errors = create_register_schema.load(content)
        if errors:
            content = request.get_json()
            name = content['name']
            lastname = content['lastname']
            identificationCard = content['identificationCard']
            phone = content['phone']
            address = content['address']
            email = content['email']
            password = content.get('password')
            rol = content.get['rol']
            print("----------", email)
            salt = bcrypt.gensalt()
            hash_pass = bcrypt.hashpw(bytes(str(password), encoding='utf-8'), salt)
            user_lines = User(name=name, lastname=lastname,
                              identificationCard=identificationCard, phone=phone, address=address, email=email, password=hash_pass,rol=rol)
            session.add(user_lines)
            session.commit()
            return jsonify({"Status": "Register consultant successfully ",
                           }), 200


##de aqui para abajo no he implementado el content["nombre de la comuna de la bd"]
##porque primero necesitamos arreglar el error de la conexion y que cree la primera tabla con el controller de register
##una vez se solucione eso implementamos en los siguientes
class LoginControllers(MethodView):
    """Logeo para el usuario del sistema"""
    
    def post(self):
        content=request.get_json()
        errors = create_login_schema.load(content)
        if errors:
            content = request.get_json()
            email = content['email']
            user = session.query(User).filter_by(email=email)
            password = bytes(str(content.get("password")), encoding='utf-8')
            ##aqui la duda cae en como recuperar el has de la bd 
            """if consultant.get(email):
                password_db = consultant[email]["password"]
                if bcrypt.checkpw(password, password_db):
                    # Se acude a jwt para generar un token codificado en formato json
                    encoded_jwt = jwt.encode({'exp': datetime.datetime.utcnow(
                    ) + datetime.timedelta(seconds=300), 'email': email}, KEY_TOKEN_AUTH, algorithm='HS256')
                    return jsonify({"Status": "Login exitoso", "auth": True, "token": encoded_jwt.decode()}), 200
                return jsonify({"Status": "Login incorrecto 22",
                                    "email":user[0].email}), 400
            return jsonify({"Status": "Login incorrecto 11"}), 400"""
        return jsonify({"Status": "Datos no validos reintente de nuevo"}),400
      




class RegisterCustomerControllers(MethodView):
    """Registro Clientes """

    def post(self):
        if (request.headers.get('Authorization')):
            content = request.get_json()
            errors = create_RegisterCustomerControllers_schema.load(content)
            if errors:
                name = content.get("name")
                lastname = content.get("lastname")
                identificationCard = content.get("identificationCard")
                line = content.get("phone")
                dateBorn = content.get("dateBorn")
                return jsonify({"Status": "Register customer successfully, Autorizacion por token valida ",
                            "name ": name,
                            "lastname ": lastname,
                            "identification card": identificationCard,
                            "date of born ": dateBorn,
                            "line ": line}), 200
        return jsonify({"Status": "No ha enviado un token"}), 403


class RegisterEquipmentControllers(MethodView):
    """ Registro equipo movil"""

    def post(self):
        if (request.headers.get('Authorization')):
            content = request.get_json()
            errors = create_RegisterEquipmentControllers_schema.load(content)
            if errors:
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
    """Manejo de las lineas telefonicos"""
    def post(self):
        if (request.headers.get('Authorization')):
            content = request.get_json()
            errors = create_ManageLineControllers_schema.load(content)
            if errors:
                number_line = content.get("numberLine")
                customer_dentification_card = content.get("customerIdentificationCard")
                state = content.get("state")
                return jsonify({"Status": "Register line successfully",
                            "number_line ": number_line, "state ": state,
                            "Customer Identification Card": customer_dentification_card}), 200
        return jsonify({"Status": 'no envio un token'}), 400

    def get(self, phone):
        if (request.headers.get('Authorization')):
            errors = create_ManageLineControllers_get_schema.validate(phone)
            if errors:
                return jsonify({"Status": "Line Consulted Successfully",
                            'linea': phone,
                            }), 200
        return jsonify({"Status": "no se envio token"})

    def put(self, id_customer):
        if (request.headers.get('Authorization')):
            errors = create_ManageLineControllers_put_schema.validate(id_customer)
            if errors:
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
    """Manejo de factura 88uu"""

    def get(self,line):
        if(request.headers.get('Authorization')):
            errors = create_ManageBillControllers_get_Schema.validate(line)
            if errors:
                return jsonify({"Status": "Bill Consulted Successfully",}), 200
        return jsonify({"Status": "error en el token"}), 400

    def delete(self,line):
        if(request.headers.get('Authorization')):
            errors = create_ManageBillControllers_delete_Schema.validate(line)
            if errors:
                content = request.get_json(self)
                return jsonify({"Status": "Bill Deleted Successfully",
                            "linea" : line, 
                            }), 200

        return jsonify({"Status":"no se envio un token"

                         }),400
