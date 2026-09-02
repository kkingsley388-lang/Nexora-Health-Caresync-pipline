import os
import pandas as pd # pandas is a Python library commonly used for working with tables and CSV files. The as pd part gives pandas a shorter name.
# so when we need to call pandas we do df = pd.read_csv() instead of df = pandas.read_csv()
from dataset_specs import Dataset

def extract_dataset(dataset_key):
  rules = Dataset[dataset_key] # this is basics syntax of accessing a data in a pyhton dictionary or Accesses the "Encounter" key in the Dataset dictionary and stores its contents in the variable, rules.
  file_path = rules["file_name"]
  mapping = rules["column_mappings"]

  columns_to_keep = list(mapping.keys()) #mapping.keys() is a dictionary method, that returns the keys(which are inorder words the raw column names) in the dictionary name mapping. list() is a data type conversion that represent those keys as a list, which is then store in the vairable columns_to_keep.

    #implement fast-fail check
  if not os.path.exists(file_path): #"If the file does NOT exist..."
    raise FileNotFoundError(f"Contract broken: File '{file_path}' does not exist.")# raise means stops the program and report an error.
  
# 2. Read only the header to check the expected columns
  actual_source_columns = pd.read_csv(file_path,nrows=0).columns.tolist()

  missing_columns = [] 

  for column in columns_to_keep:
    if column not in actual_source_columns:# this has been explained in the loops.py
      missing_columns.append(column)# ths how access a list with .append()being a list method. .append() adds the columns in columns_to_keep to missing-columns if its not in actual_source_columns

# 3. Are all expected columns present in the file? Fail fast if expected columns are missing.
    if missing_columns:
        raise ValueError(
            f"Contract broken for '{dataset_key}':",
            f"Missing required columns in CSV: {missing_columns}"
        )
  df = pd.read_csv(file_path, dtype=str, keep_default_na=False, usecols=columns_to_keep)

  df = df.rename(columns=mapping)
  return df 

Encounter_df = extract_dataset("Encounter") #return extracted df bsck into where the fucntion was called and the variable encounter_df stores the df/dataframe
Condition_df = extract_dataset("Condition/Diagnosis") 
Patient_df = extract_dataset("Patient") 
Organization_df = extract_dataset("Organization") 
Provider_df = extract_dataset("Provider") 
Payer_df = extract_dataset("Payer" ) 







