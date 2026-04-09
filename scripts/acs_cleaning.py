import pandas as pd

def clean_acs_data(file_name, keep_columns=None, cleaned_name=None):
    # read csv
    df = pd.read_csv(f"../raw_data/{file_name}")

    # filter for only Cobb County data
    df = df[df['Name of geographic unit'].str.contains('Cobb County', na=False)]

    # get tract column
    tract_col = [df.columns[1]]

    # format user input columns
    if keep_columns is not None:
        if isinstance(keep_columns, str):
            keep_columns = [keep_columns]
        extra_cols = [col for col in keep_columns if col in df.columns]
    else:
        extra_cols = []

    # combine columns (tract col + user-inputted cols)
    final_cols = list(dict.fromkeys(tract_col + extra_cols))

    # create subsetted df
    df = df[final_cols]

    # save df to cleaned_data folder
    if cleaned_name is not None:
        df.to_csv(f"../cleaned_data/{cleaned_name}", index=False)

    return df