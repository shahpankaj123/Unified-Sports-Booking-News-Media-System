


def is_none(value):
    if value is None or value == '' or value == 'undefined' or value == 'null' or str(value).lower() == 'nan' or str(value) == 'null':
        return True
    return False

def message(message):
    return {'message': message}