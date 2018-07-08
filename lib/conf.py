import os
import console.config as conf


def get_path_to_logger():
    """
    This function tries to get the path to the log files based on the path specified in the console configuration
    file, and if the console configuration is not available, the standard library paths will be used
    :return: path to the log files

    """
    try:
        path = conf.get_path_to_log()
        return path
    except Exception as e:
        print(e)
        path = os.path.dirname(os.path.abspath(__file__))
        return path[:-3]


def get_path_to_db():
    """
    This function tries to get the path to the database files based on the path specified in the console
    configuration file, and if the console configuration is not available, the standard library paths will be used
    :return: path to the database files

    """
    try:
        path = conf.get_path_to_db()
        print(path)
        return path
    except Exception as e:
        print(e)
        path = os.path.dirname(os.path.abspath(__file__))
        path = path[:-3]
        path = os.path.join(path, 'database.sqlite3')
        print(path)
        return path


def get_logging_level():
    """
        This function tries to get the logging-level based on the path specified in the console
        configuration file, and if the console configuration is not available, the standard library paths will be used
        :return: path to the database files

    """
    try:
        level = int(conf.get_logging_level())
        return level
    except Exception as e:
        print(e)
        return 1
