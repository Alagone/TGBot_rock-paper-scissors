import logging

logging.basicConfig(filename="./app_state.log", level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', encoding="UTF-8")
logger = logging.getLogger(__name__)