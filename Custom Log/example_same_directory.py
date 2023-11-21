# If the log file is in the same directory of custom_log.py (configuration), you do this
import logging
from custom_log import CustomLog

# Set file, level, text
CustomLog('example.log', 'info', 'This is an example log')
