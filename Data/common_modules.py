import logging
logging.basicConfig(level=logging.INFO,filename="LogFile.log",filemode="a",
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
                    datefmt='%Y/%m/%d %H:%M:%S')
ErrorHandler = logging.StreamHandler()
ErrorHandler.setLevel(logging.ERROR)
ErrorHandler.setFormatter(logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s'))
logger = logging.getLogger()
logger.addHandler(ErrorHandler)