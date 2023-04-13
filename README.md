# Data Analyst Assignment
This is my solution to the Data Analyst assignment at Specialisterne Academy (Spring 2023). The assignment entails writing a program that can insert information extracted from from a large body of json files into a tabular data format, as well as creating scatterplots of the variables within this dataset. 

## Design Considerations
I decided to split this assignment into two; a python program that can extract and format the data, and an R script that can create the plots.   
I made this decistion because Python is more nimble when it comes to dealing with the json format (dictionaries), while the `GGplot2` package in R allows for more control when creating plots (at least in my opninion).    
This decition is not without issues; I could have tried to use `matplotlib` if I wanted to limit the project to using only Python - which might in turn have made it easier for others to use my code. 

### Data extraction
The extraction is not perfect - unlabbled positions will not be included, ant there were 7 files I could not load into the program - the comments seem to be a frequent contributer to this problem. 
