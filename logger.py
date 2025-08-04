#flake8: noqa: E501

"""
Handles the logic of logging.
Purely for dev maniacs. Normal peeps, kindly hesitate.
"""

import os
import logging

def setup_logging(log_file="logs/shridevcpp.log"):
    log_dir = os.path.dirname(log_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)


        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s,
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(),
            ],
            force=True,
        )
        logging.getLogger('matplotlib').setLevel(logging.WARNING)
        logging.getLogger('scipy').setLevel(logging.ERROR)

