import  logging

class logMaker:
    @staticmethod
    def logGenerator():
        logging.basicConfig(filename=".\\logs\\chemia.log",format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt="%Y-%m-%d %H:%M:%S",force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
















