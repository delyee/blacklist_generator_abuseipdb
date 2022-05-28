from config import *
from loguru import logger

logger.add("ChangeMe_{time}.log.log", rotation="1 GB", compression="gz")
# logger.info("Starting...")
# logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")

# handler = logging.handlers.SysLogHandler(address=('localhost', 514))
# logger.add(handler)

# logger.level("SNAKY", no=38, color="<yellow>", icon="🐍")
# logger.log("SNAKY", "Here we go!")
