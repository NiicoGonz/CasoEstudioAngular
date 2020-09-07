from controllers import RegisterConsultantControllers, LoginControllers , RegisterCustomerControllers, RegisterEquipmentControllers,ManageLineControllers, ManageBillControllers

consultant = {
    "registerConsultant" : "/api/v01/consultant/register" , "register_consultant_controllers" : RegisterConsultantControllers.as_view("register_consultant_api")
}

login = {
    "login" : "/api/v01/login" , "login_controllers" : LoginControllers.as_view("login_api")
}

#cliente
customer = {
    "registerCustomer" : "/api/v01/customer/register", "register_customer_controllers": RegisterCustomerControllers.as_view("register_customer_api")
}

equipment = {
    "registerEquipment" : "/api/v01/equipment/register" , "register_equipment_controllers" : RegisterEquipmentControllers.as_view("register_equipment_api")
}

line = {
    "registerLine": "/api/v01/line/register", "register_line_controllers": ManageLineControllers.as_view("register_line_api"),
    "getLine": "/api/v01/line/get/<phone>", "get_line_controllers": ManageLineControllers.as_view("get_line_api"),
    "putLine": "/api/v01/line/put/<id_customer>", "put_line_controllers": ManageLineControllers.as_view("put_line_api")
}

#factura
bill  = {
    "getBill": "/api/v01/bill/get/<line>", "get_bill_controllers": ManageBillControllers.as_view("get_bill_api"),
    "deleteBill": "/api/v01/bill/delete/<line>", "delete_bill_controllers": ManageBillControllers.as_view("delete_bill_api")
}