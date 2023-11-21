#If the log's file is in the different directory of custom_log (configuration), you do this
import logging
import sys
sys.path.append('personal/directory/log/config/') #add position of log configurator
from custom_log import CustomLog

#Set file, level, text
logpy('example.log', 'info', 'This is an example log')
