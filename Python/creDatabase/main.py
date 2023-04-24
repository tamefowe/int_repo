import warnings
from reader_writer import Reader, DBWriter

warnings.simplefilter(action='ignore', category=FutureWarning)


def get_property_info():
    reader = Reader()
    return reader.get_property_info()


def run():
    property_info = get_property_info()
    table_name = 'Property_Lead'
    writer = DBWriter(table_name=table_name, data=property_info)
    writer.write()


if __name__ == '__main__':
    run()
