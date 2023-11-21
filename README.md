# PYTHON CUSTOM LOGGGING

This is a simple customization of logging library. It's possible use this in two different ways:
* call the configurator from the same directory of the script that use this;
* call the configurator from different directory.

The called function is the following, CustomLog('log_file', 'log_level', 'log_text'), where:
* log_file: is the log file name;
* log_level: is the log level, and can be:
    * debug
    * info
    * warning
    * critical
    * error
    * (It doesn't matter if you write in uppercase or lowercase: 'info' or 'INFO')
* log_text: is the message of the log.

Furthermore, in the configuration it is possible to choose the type of file, whether daily or common:

```python
handler = logging.FileHandler(f'{log_file}_.log') # Common log file
handler = logging.FileHandler(datetime.now().strftime(f'{log_file}_%d_%m_%Y.log')) # Single day log file
```

(REMEMBER: one of this must be commented)
