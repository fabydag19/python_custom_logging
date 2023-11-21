# If the script is in a the different directory than custom_log.py (configuration), you do this
import logging
import sys
sys.path.append('personal/directory/log/config/') #add position of log configuration
from custom_log import CustomLog

# Set file, level, text
CustomLog('example.log', 'info', 'This is an example log')
