def protobuf_to_dict(pb) -> dict:
    result_dict = {}
    for field, value in pb.ListFields():
        result_dict[field.name] = value
    return result_dict
