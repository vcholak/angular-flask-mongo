__author__ = 'vcholak'

import datetime
import bson


def json_dict(dict_obj):
    """ Converts non-JSON types to JSON types
    :param dict_obj: source dictionary
    :return: new dictionary
    """
    new_dict = {}
    for key in dict_obj:
        val = dict_obj[key]
        if isinstance(val, bson.ObjectId):
            new_dict['id'] = str(val)
        elif isinstance(val, datetime.datetime):
            new_dict[key] = val.isoformat()
        else:
            new_dict[key] = val
    return new_dict