
def to_float(value):
    return 0.0 if not value else value


def to_int(value):
    return 0 if not value else value


def rd(value):
    return '{:20,.2f}'.format(value)


def pc(value):
    return '{:.2%}'.format(value)


def get_password():
    return 'Otetie\@79'
