
# Description
This module contains scripts used for applying basic checks on the API responses.

# How To Run The Script 

#### System Pre-requisites

  - Python 2.7
  - `requests` and `json` libraries should be installed in the python environment.
  
#### Running The Script

- The scripts `daa.py` and `nadia.py` correspond to the DAA and Nadia endpoints respectively. 
- Upon finishing running either of the scripts, you will see the two output files ('something_out.txt' for successful tests and 'buggy_something_out.txt' for unsuccessful tests) being generated. For each separate query you will see the the output as **(query, docIndex,True)** in the 'something_out.txt' file and as **(query, docIndex,False)** in the 'buggy_something_out.txt' file. For example, (image of cars, 3, True). Since there are a large number of queries in the input files, running the script on the entire input file will take a long time. You can stop the script any time by pressing Ctrl+C .
- Input file ('query_Something.txt') should have each query on a new line because the script treats each newline as a separate query. Make sure that the input file is in the same folder as the scripts. The python scripts have been written with the consideration that input file's names are **"query_DAA.txt"** and **"query_Nadia.txt"** for the scripts "daa.py" and "nadia.py", respectively. If you wish to change the input file's name, then kindly replace the old file name with the new file name in the python script as well.
