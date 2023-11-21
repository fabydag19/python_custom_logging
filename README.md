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

![image](https://github.com/fabydag19/python_custom_logging/assets/62938446/f99c04ab-05ca-4f66-827d-506ccf9e7022)

Furthermore, in the configuration it is possible to choose the type of file, whether daily or common:

```python
handler = logging.FileHandler(f'{log_file}_.log') # Common log file
handler = logging.FileHandler(datetime.now().strftime(f'{log_file}_%Y%m%d.log')) # Single day log file
```

(REMEMBER: one of this must be commented)
