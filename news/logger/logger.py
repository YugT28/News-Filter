import logging
import os
from datetime import datetime
from pathlib import Path

LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

logs_path=Path.cwd()/"logs"/LOG_FILE
logs_path.parent.mkdir(exist_ok=True, parents=True)

logging.basicConfig(filename=logs_path,
                    level=logging.INFO,
                    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")

if __name__ == "__main__":
    pass
