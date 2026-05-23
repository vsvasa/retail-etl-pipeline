import os

def validate_file_exists(filepath):

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found {filepath}")

def validate_columns(df,expected_columns):

    missing_columns = [
        col for col in expected_columns
        if col not in df.columns
    ]

    if missing_columns:
        raise Exception(f"missing columns: {missing_columns}")
            
        