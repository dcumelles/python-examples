import logging

# Primera config, a de append
logging.basicConfig(filename="log.txt",
                    filemode='a',
                    format='%(asctime)s: %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.info("")
logging.warning("")