from flask import Flask
from flask_cors import CORS
from routes import consultant, login , customer,equipment, line, bill

app = Flask(__name__)
CORS(app, resources={r"/*": { "origins" : "*"}})

app.add_url_rule(consultant["registerConsultant"], view_func = consultant["register_consultant_controllers"])
app.add_url_rule(login["login"], view_func=login["login_controllers"])
app.add_url_rule(customer["registerCustomer"], view_func=customer["register_customer_controllers"])
app.add_url_rule(equipment['registerEquipment'], view_func=equipment['register_equipment_controllers'])
app.add_url_rule(line["registerLine"], view_func=line["register_line_controllers"])
app.add_url_rule(line["getLine"], view_func=line["get_line_controllers"])
app.add_url_rule(line["putLine"], view_func=line["put_line_controllers"])
app.add_url_rule(bill["getBill"], view_func=bill["get_bill_controllers"])
app.add_url_rule(bill["deleteBill"], view_func=bill["delete_bill_controllers"])