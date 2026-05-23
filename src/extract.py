import pandas as pd
from validation import validate_file_exists,validate_columns


def extract_csv(filepath,expected_columns):

    validate_file_exists(filepath)

    df = pd.read_csv(filepath)

    print(f"Loaded {len(df)} rows from {filepath}")

    validate_columns(df,expected_columns)

    return df

