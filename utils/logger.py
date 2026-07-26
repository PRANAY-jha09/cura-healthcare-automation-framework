import logging
import os

LOG_DIR ="logs"
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=f"{LOG_DIR}/automation.log",
    level =logging.INFO,
    format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s"

)
logger = logging.getLogger()
