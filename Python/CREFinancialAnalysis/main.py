import warnings
from runner import Runner
from logging import Logger
from config import DB_LOGIN
from db_server import DBServer

logger = Logger(__name__)

warnings.simplefilter(action='ignore', category=UserWarning)
warnings.simplefilter(action='ignore', category=FutureWarning)




class Server(object):
    def __init__(self, server=None, yearly_projection=None, save_to_db=None):
        self._db_server = server
        self._yearly_projection = yearly_projection
        self._save_to_db = save_to_db


class CREServer(Server):
    def __init__(self, server=None, yearly_projection=None, save_to_db=None):
        super().__init__(server, yearly_projection, save_to_db)

    def _get_projection(self):
        if self._yearly_projection:
            return

        yearly_projection_str = input("How far in years go your projected financials? : ")

        self._yearly_projection = 1
        if not yearly_projection_str.isdigit():
            logger.warning("Will default to 1-year projected financials! ...")
        else:
            self._yearly_projection = int(yearly_projection_str)

    def _get_is_save_to_db(self):
        if self._save_to_db:
            return

        save_to_db_str = input("Do we save the data? (y/n): ")

        # we do not save to db unless specified (as most of the time we are running quick calculations)
        self._save_to_db = False

        if save_to_db_str.lower() == 'y':
            self._save_to_db = True
        elif save_to_db_str.lower() == 'n':
            self._save_to_db = False
        else:
            logger.warning('Will not save entries to db! ...')


    def _set_db_server(self):
        if self._db_server:
            return
        db_info = dict(
            host=DB_LOGIN['host'],
            username=DB_LOGIN['username'],
            password=DB_LOGIN['password'],
            port=DB_LOGIN['port'],
            database=DB_LOGIN['database'],
            password_file=DB_LOGIN['password_file']
        )
        self._db_server = DBServer(**db_info)

    def kick(self):
        print("Running Commercial Real Estate Financial analysis ...\n")
        self._get_projection()
        self._get_is_save_to_db()
        self._set_db_server()

    def run(self):
        self._db_server.start()
        Runner(db_server=self._db_server,
               projection_yrs=self._yearly_projection).run_fast_fasTER_FASTEST(self._save_to_db)

    def shutdown(self):
        self._db_server.close()


if __name__ == '__main__':
    server = CREServer(yearly_projection=1, save_to_db=True)
    server.kick()
    server.run()
    server.shutdown()