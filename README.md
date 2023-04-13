# Data Analyst Assignment
This is my solution to the Data Analyst assignment at Specialisterne Academy (Spring 2023). The assignment entails writing a program that can insert information extracted from from a large body of json files into a tabular data format, as well as creating scatterplots of the variables within this dataset. 

## Design Considerations
I decided to split this assignment into two; a python program that can extract and format the data, and an R script that can create the plots.   
I made this decistion because Python is more nimble when it comes to dealing with the json format (dictionaries), while the `GGplot2` package in R allows for more control when creating plots (at least in my opninion).    
This decition is not without issues; I could have tried to use `matplotlib` if I wanted to limit the project to using only Python - which might in turn have made it easier for others to use my code. 

### Data extraction
A list of jason files across the three folders is genetated.
Attempt to load JSON files (flag if fail)
loop through files
template key and data are subsetted.
subset further. 
loop through positions - get parameters (through iterations). 


The extraction is not perfect - unlabbled positions will not be included, ant there were 7 files I could not load into the program - the comments seem to be a frequent contributer to this problem. 
The finished dataset also contains a number of NAs. 

there are no NAs in the _id_, _template-key_, 
or _date_ columns. The _weight_ column has a lot of NAs, and the four other 
parameters has the exact same number of NAs

The _abcd_ columns have the same number of NAs. I filtered out all the NAs in 
the _a_ column, and as can be seen below, it seems like the _abcd_ columns have 
the 23 NAs in common - though the _weight_ columns doesn't. 

Most of these could perhaps be explained by looking the data 
extraction from the JSON files. 
The program is instructed to leave most of the _position_, _abcd_ and _weight_ 
columns blank if the JSON files does not contain the "AssayResults"-key, which 
stores all information extracted to these columns. 
The program is also instructed to leave the _abcd_ blank when "AssayResults" 
has no "FitResult"-key, which contains the information extracted into these.

I tried to check in the files for further clarification, but as I have not 
written the extraction program to add a column for the name of the JSON file, 
it would have been an arduous task. 
I decided to let this be for now.  
