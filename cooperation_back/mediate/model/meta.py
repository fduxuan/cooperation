from .field import Reserved, Normal


class ModelMeta(type):
    def __new__(mcs, name, bases, name_dict):

        reserved_fields = set()
        normal_fields = set()
        if bases:
            last_class = bases[0]
            reserved_fields = getattr(last_class, 'reserved_fields', set()) or set()
            normal_fields = getattr(last_class, 'normal_fields', set()) or set()
        for attr_name, attr_inst in name_dict.items():
            if isinstance(attr_inst, type):  # the class
                if issubclass(attr_inst, Reserved):
                    attr_inst = name_dict[attr_name] = attr_inst(attr_name)  # create the instance
                elif issubclass(attr_inst, Normal):
                    attr_inst = name_dict[attr_name] = attr_inst(attr_name)

            if isinstance(attr_inst, Reserved):
                if attr_inst.mongo_field is None:
                    attr_inst.mongo_field = attr_name
                reserved_fields.add(attr_inst.mongo_field)
            if isinstance(attr_inst, Normal):
                if attr_inst.mongo_field is None:
                    attr_inst.mongo_field = attr_name
                normal_fields.add(attr_inst.mongo_field)

        fields = reserved_fields.union(normal_fields)
        name_dict['reserved_fields'] = reserved_fields
        name_dict['normal_fields'] = normal_fields
        name_dict['fields'] = fields
        result = type(name, bases, name_dict)
        return result
