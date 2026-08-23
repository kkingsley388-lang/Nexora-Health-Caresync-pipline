#Understanding,  Fail fast with a clear error when a file or expected column is missing, a broken batch contract should stop the run, not limp through it. 

import os
import pandas as pd
from dataset_specs import Dataset

#this is a clean implementation of our extraction engine which also validate the contract before processing the file.
def extract_encounter():
    rules = Dataset["Encounter"]
    file_path = rules["file_name"]
    mapping = rules["column_mappings"]

    columns_to_keep = list(mapping.keys())

    # 1. Fail fast if the file does not exist
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Contract broken: File '{file_path}' does not exist."
        )

    # 2. Read only the header to check the expected columns
    actual_columns = pd.read_csv(
        file_path,
        nrows=0
    ).columns.tolist()

    missing_columns = [            # this is a list comprehension that contains a for loop and if statement to understand it visit the  loops.py file
        column for column in columns_to_keep
        if column not in actual_columns
    ]

    # 3. Fail fast if expected columns are missing
    if missing_columns:
        raise ValueError(
            f"Contract broken: File '{file_path}' is missing "
            f"expected column(s): {missing_columns}"
        )

    # 4. Only process the file once the contract is valid
    df = pd.read_csv(
        file_path,
        dtype=str,
        keep_default_na=False,
        usecols=columns_to_keep
    )

    return df

# for the code let focus on the middle part 

  # 1. Fail fast if the file does not exist
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Contract broken: File '{file_path}' does not exist."
        )



    # 2. Read only the header to check the expected columns
    actual_columns = pd.read_csv(
        file_path,
        nrows=0
    ).columns.tolist()

    missing_columns = [
        column for column in columns_to_keep
        if column not in actual_columns
    ]

    # 3. Fail fast if expected columns are missing
    if missing_columns:
        raise ValueError(
            f"Contract broken: File '{file_path}' is missing "
            f"expected column(s): {missing_columns}"
        )

    