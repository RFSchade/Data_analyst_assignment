# Data Analyst Assignment
This is my solution to the Data Analyst assignment at Specialisterne Academy (Spring 2023). The assignment entails writing a program that can insert information extracted from from a large body of json files into a tabular data format, as well as creating scatterplots of the variables within this dataset. 

## Design Considerations
I decided to split this assignment into two; a python program that can extract and format the data, and an R script that can create the plots.   
I made this decistion because Python is more nimble when it comes to dealing with the json format (dictionaries), while the `GGplot2` package in R allows for more control when creating plots (at least in my opninion).    
This decition is not without issues; I could have tried to use `matplotlib` if I wanted to limit the project to using only Python - which might in turn have made it easier for others to use my code. 

### Data extraction
The script extracts a list of JSON files in the data folder, and loops through them. The files are loaded in as dictionaries, and information is extracted through a series of subsets and iterations. The program loops first through files, then positions, then indivisual parameters. In the end, the program saves two files to the output folder: flagged_files.csv, which is a list of files the program failed to load, and model_data.csv, which contains the extracted data.     
THe model_data.csv file has 9 columns: template_key, date, position, ab, b, c, d, weight, and an unnamed ID column.      

The extraction is not perfect - unlabbled positions will not be included, and there were 7 files I could not load into the program - the comments seem to be a frequent contributer to this problem. 
In my case, the finished dataset also contains a number of NAs that seem to be products of how the data was extracted. 
The program is instructed to leave the position, a, b, c, d, and weight columns blank if the JSON files does not contain the "AssayResults"-key, which 
stores all information extracted to these columns.     
The program is also instructed to leave the a, b, c, and d columns blank when "AssayResults" 
has no "FitResult"-key, which contains the information extracted into these.   
A lot of the missing values in the weight columns seem to be because the data does not always report the same no. of statistics under "StatisticTestResults". This could have been mitigated through some extra validation.     
Once the data is extracted, there is also no link between a specific datapoint and the file it was extracted from. This makes it a lot harder to "track" missing data. 

### Plotting
For a more thorough breakdown of the code, see plots_and_code.html in the R folder. 

After loading in the output of the data_extraction.py scipt, I looked through the data to get an overview, and decided to remove NAs in the position, a, b, c, and d columns for easier plotting. I decided agains doing the same with the weight column, because the number of NAs are for greater, and thus a lot more data would be lost. 

