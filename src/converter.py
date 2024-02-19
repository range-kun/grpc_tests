import six

from google.protobuf.descriptor import FieldDescriptor


EXTENSION_CONTAINER = '___X'

TYPE_CALLABLE_MAP = {
    FieldDescriptor.TYPE_DOUBLE: float,
    FieldDescriptor.TYPE_FLOAT: float,
    FieldDescriptor.TYPE_INT32: int,
    FieldDescriptor.TYPE_INT64: int if six.PY3 else six.integer_types[1],
    FieldDescriptor.TYPE_UINT32: int,
    FieldDescriptor.TYPE_UINT64: int if six.PY3 else six.integer_types[1],
    FieldDescriptor.TYPE_SINT32: int,
    FieldDescriptor.TYPE_SINT64: int if six.PY3 else six.integer_types[1],
    FieldDescriptor.TYPE_FIXED32: int,
    FieldDescriptor.TYPE_FIXED64: int if six.PY3 else six.integer_types[1],
    FieldDescriptor.TYPE_SFIXED32: int,
    FieldDescriptor.TYPE_SFIXED64: int if six.PY3 else six.integer_types[1],
    FieldDescriptor.TYPE_BOOL: bool,
    FieldDescriptor.TYPE_STRING: six.text_type,
    FieldDescriptor.TYPE_BYTES: six.binary_type,
    FieldDescriptor.TYPE_ENUM: int,
}


def repeated(type_callable):
    return lambda value_list: [type_callable(value) for value in value_list]


def enum_label_name(field, value, lowercase_enum_lables=False):
    label = field.enum_type.values_by_number[int(value)].name
    label = label.lower() if lowercase_enum_lables else label
    return label


def _is_map_entry(field):
    return (field.type == FieldDescriptor.TYPE_MESSAGE and
            field.message_type.has_options and
            field.message_type.GetOptions().map_entry)


def protobuf_to_dict(
        pb,
        type_callable_map=TYPE_CALLABLE_MAP,
        use_enum_labels=False,
        including_default_value_fields=False,
        lowercase_enum_lables=False
):
    result_dict = {}
    extensions = {}
    for field, value in pb.ListFields():
        type_callable = _get_field_value_adaptor(
            pb,
            field,
            type_callable_map,
            use_enum_labels,
            including_default_value_fields,
            lowercase_enum_lables
        )
        if field.label == FieldDescriptor.LABEL_REPEATED:
            type_callable = repeated(type_callable)

        if field.is_extension:
            extensions[str(field.number)] = type_callable(value)
            continue

        result_dict[field.name] = type_callable(value)

    # Serialize default value if including_default_value_fields is True.
    if including_default_value_fields:
        for field in pb.DESCRIPTOR.fields:
            # Singular message fields and oneof fields will not be affected.
            if ((
                    field.label != FieldDescriptor.LABEL_REPEATED and
                    field.cpp_type == FieldDescriptor.CPPTYPE_MESSAGE) or
                    field.containing_oneof):
                continue
            if field.name in result_dict:
                # Skip the field which has been serailized already.
                continue
            if _is_map_entry(field):
                result_dict[field.name] = {}
            elif field.label == FieldDescriptor.LABEL_REPEATED:
                result_dict[field.name] = []
            elif field.type == FieldDescriptor.TYPE_ENUM and use_enum_labels:
                result_dict[field.name] = enum_label_name(field, field.default_value, lowercase_enum_lables)
            else:
                result_dict[field.name] = field.default_value

    if extensions:
        result_dict[EXTENSION_CONTAINER] = extensions
    return result_dict


def _get_field_value_adaptor(
        pb,
        field,
        type_callable_map=TYPE_CALLABLE_MAP,
        use_enum_labels=False,
        including_default_value_fields=False,
        lowercase_enum_lables=False
):

    if field.type == FieldDescriptor.TYPE_MESSAGE:
        # recursively encode protobuf sub-message
        return lambda pb: protobuf_to_dict(
            pb, type_callable_map=type_callable_map,
            use_enum_labels=use_enum_labels,
            including_default_value_fields=including_default_value_fields,
            lowercase_enum_lables=lowercase_enum_lables,
        )

    if use_enum_labels and field.type == FieldDescriptor.TYPE_ENUM:
        return lambda value: enum_label_name(field, value, lowercase_enum_lables)

    if field.type in type_callable_map:
        return type_callable_map[field.type]

    raise TypeError("Field %s.%s has unrecognised type id %d" % (
        pb.__class__.__name__, field.name, field.type))