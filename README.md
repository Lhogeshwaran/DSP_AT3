# DSP_AT3
### Repository for DSP Assignment 3. Reproducibility and risk audit

In the terminal execute the following commands to set up the project space and environment  
$ git clone https://github.com/Lhogeshwaran/DSP_AT3.git  
$ cd DSP_AT3  
$ pip install --user --requirement requirements.txt

The iPython notebook is updated with inforamtion about the analysis and can be executed block-by-block.   
https://github.com/Lhogeshwaran/DSP_AT3/blob/master/13313491_AT3.ipynb

Python file 'analysis_rep_api provides' an API to repeat the exercise with a new dataset. The API can be called from the command line like -  
$ cd /path/to/repo  
$ python analysis_rep_api.py <<Name_of_excel.xlsx>> <<Name_of_sheet_with_data>> 

The analysis plots and the csv file with the sentiment scores will be created in the project repo. 
