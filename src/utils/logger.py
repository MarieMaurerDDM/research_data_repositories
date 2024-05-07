import logging


def log(message, level='info'):
    # Configure logging to write to a file
    logging.basicConfig(filename='error.log',
                        level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    if level == 'error':
        # Print error message to console
        print(f"ERROR - {message}")
        # Write stack trace to log file
        logging.exception(message)
    elif level == 'info':
        # Print info to console
        print(f"INFO - {message}")
