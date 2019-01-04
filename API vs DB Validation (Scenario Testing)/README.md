# Description
This module contains scripts used for validating API requests and responses against the entries registered in the database. 

# How To Run The Script 
#### System Pre-requisites
  - Python 3.5 or above
  - The following libraries should be set up on the python environment : 
-- requests
-- pyodbc (you will need a Microsoft ODBC Driver before installing pyodbc. The complete process of installing pyodbc can be found [here](https://docs.microsoft.com/en-us/sql/connect/python/pyodbc/step-1-configure-development-environment-for-pyodbc-python-development?view=sql-server-2017))
-- json
-- urllib3

#### Running The Script

- `common_config.ini` has the credentials for database connection. In case you want to use a different database or different server, change this file accordingly.
- Input file ('query_Something.txt') should have each query on a new line because the script treats each newline as a separate query. Make sure that the input file is in the same folder as the scripts. 
- `utils.py` has API request as well as database related variables, such as database query, endpoint, location of input and config files, request format, etc. These all can be edited from this file, without having to make changes in the main `scenarios.py` file. All the queries will use these configurations only. Make sure that you adhere to the format while making changes.
- `scenarios.py` is the main script which has to be run. Upon execution, you will see the results as a tuple of the form **(query, True/False)** . True/False value indicates whether that specific query passed the test or not.