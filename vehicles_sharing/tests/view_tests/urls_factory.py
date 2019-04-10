VEHICLES = 'vehicles'


def url_not_detail(content, method=''):
    """
    url on many intems like something/vehicles_sharing/vehicles
    :param content:
    :param method:
    :param options:
    :return:
    """
    return f'/vehicles_sharing/{content}/{method}'


def url_detail(content, id, method=''):
    """
    url on specific item from database like something/vehicles_sharing/vehicles/1
    :param content:
    :param id:
    :param method:
    :param options:
    :return:
    """
    return f'/vehicles_sharing/{content}/{id}/{method}'
