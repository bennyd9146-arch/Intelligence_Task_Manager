import logging

logging.basicConfig(
    level = logging.INFO,
    format="[%(levelname)s] | %(asctime)s | %(message)s | %(filename)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("./logs/app.log"),


]
)

logger = logging.getLogger(__name__)