#If the log's file is in the same directory of custom_log (configuration), you do this
import logging
from test import CustomLog

#Set file, level, text
logpy('example.log', 'info', 'This is an example log')
