class QueryToList():
    @staticmethod
    def queryall_admin_to_list(query_result):
        list_data = []
        for row in query_result:
            aux_dict = {}
            aux_dict["email"] = row.email
            aux_dict["name"] = row.name
            aux_dict["lastname"] = row.lastname
            aux_dict["identificationCard"] = row.identificationCard
            aux_dict["phone"] = row.phone
            aux_dict["address"] = row.address
            aux_dict["email"] = row.email
            aux_dict["password"] = row.password
            aux_dict["rol"] = row.rol
        return list_data