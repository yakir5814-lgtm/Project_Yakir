import logging

def setup_logging():
    logging.basicConfig(
        filename='logs/provisioning.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger()

logger = setup_logging()

def log_message(message, level="info"):
    if level == "error":
        logger.error(message)
    else:
        logger.info(message)
    print(message)

# דוגמה לשימוש:
if __name__ == "__main__":
    log_message("Starting provisioning process.")