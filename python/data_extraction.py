#==========================================================================================#
#================================> Data Extraction Script <================================#
#==========================================================================================#

#=====> Import modules
# System modules
import os

# Data modules
import json
import glob
import re
import pandas as pd

# Other
from tqdm import tqdm

#=====> Define functions
# > Get list of files in directory
def get_files():
    # Define patterns for json files
    json_pattern = os.path.join("data", "**", "*.json")
    # get filepath for files that match pattern
    file_list = glob.glob(json_pattern)
    
    return file_list

# > Save dataframe as csv
def save_file(df, filename):
    # Define outpath
    outpath = os.path.join("output", filename)
    # Save file
    df.to_csv(outpath)

# > Load json file
def load_file(filepath):
    # Read file
    with open(filepath, 'r') as file:
        file_contents = file.read()
    # Replace invalid values and load
    data = json.loads(file_contents.replace("INF", "0"))
    
    return data

# > Checks if input has position name
def is_position(data, k): 
    try: 
        # Does name of AssayElement match regex?
        value = data[k]["AssayElementResults"]["AssayElementResult[2]"]["Name"]
        boolean = re.match("Position+", value)
    except: 
        # If not possible, default is false
        boolean = False
    
    return boolean

# > Check if input has a name that matches specific position 
def is_this_position(data, k, position):
    try:  
        # Does the name of the parameter match specific position?
        boolean = data[k]["AssayElementName"] == position
    except:  
        # If not possible, default is false
        boolean = False
    
    return boolean

# > Try to get name of element
def get_name(data, result):
    try: 
        # Assign name
        name = data[result]["AssayElementResults"]["AssayElementResult[2]"]["Name"]
    except: 
        # If not possible, default is None
        name = None
        
    return name

# > Try to get model weight
def get_weight(data, result): 
    try: 
        # Assign weight
        weight = data[result]["StatisticTestResults"]["StatisticTestResult[3]"]["Value"]
    except: 
        # If not possible, default is None
        weight = None
    
    return weight

# > Get a, b, c, and d values
def get_abcd(data, result, position):
    try: 
        # Subset data
        fit_result = data[result]["FullModel"]["FitResult"]
    except TypeError:
        # subset does not exist, default is None for all parameters
        abcd_dict = {"A": None, "B": None, "C": None, "D": None}
    else: 
        # Subset only positions
        parameter_dict = {k: fit_result[k] for k in fit_result.keys() if is_this_position(fit_result, k, position)}
        # Arrange output dictionary
        abcd_dict = {parameter_dict[k]["ParameterName"]: parameter_dict[k]["Value"] for k in parameter_dict.keys()}
    
    return abcd_dict

# > Get data on individual positions
def add_position_info(data, agg, template_key, date):
    try:
        # Subset data
        assay_results = data["QuantitativeResponseAssay"]["AssayResults"]
    except KeyError:
        # If subset does not exist, default for parameters is None
        agg.append([template_key, 
                    date, 
                    None, 
                    None, 
                    None, 
                    None, 
                    None, 
                    None])
    else:
        # Get list of keys containing information on positions
        results = [k for k in assay_results.keys() if is_position(assay_results, k)]

        for result in results:
            # Get values for dataframe
            position = get_name(assay_results, result)
            weight = get_weight(assay_results, result)
            abcd_dict = get_abcd(assay_results, result, position)

            # Append to aggregate list
            agg.append([template_key, 
                        date, 
                        position, 
                        abcd_dict.get("A"), 
                        abcd_dict.get("B"), 
                        abcd_dict.get("C"), 
                        abcd_dict.get("D"), 
                        weight])

#=====> Define main()
def main():
    # Info
    print("[info] Start data extraction...")
    
    # Get files
    file_list = get_files()
    # Initiate lists
    agg = [["template_key", "date", "position", "a", "b", "c", "d", "weight"]]
    flag_list = []
    
    for filepath in tqdm(file_list):
        try: 
            # Load data
            data = load_file(filepath) 
        except: 
            # if notpossible, flag file 
            flag_list.append(filepath)
        else: 
            # Get values for file
            template_key = data["QuantitativeResponseAssay"]["Meta"]["Template"]["Key"]
            date = data["QuantitativeResponseAssay"]["Meta"]["Creation"]["Time"][:10]
            add_position_info(data, agg, template_key, date)
    
    # Convert flags and data to pandas DataFrames
    model_df = pd.DataFrame(agg[1:], columns=agg[0])
    flag_df = pd.DataFrame(flag_list, columns=["flagged_files"])
    
    # Save flags and data
    save_file(model_df, "model_data.csv")
    save_file(flag_df, "flagged_files.csv")
    
    # Info 
    print("[info] Data extraction finished!")

# Run main() function from terminal only
if __name__ == "__main__":
    main()