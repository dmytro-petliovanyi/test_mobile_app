import logging
import os

project_directory = os.path.abspath(os.environ["TEST_MOBILE_APP_DIR"])

log_directory = os.path.join(project_directory, "logs")
os.makedirs(log_directory, exist_ok=True)

log_file = os.path.join(log_directory, "logs.txt")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(log_file)
    ]
)
