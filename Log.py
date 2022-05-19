import logging


def slogger(log_message, log_object):
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s',
                        filename='output.log')
    logger = logging.getLogger(log_object)
    print(log_message)
    logger.debug(log_message)


if __name__ == "__main__":
    slogger("test")
else:
    pass
