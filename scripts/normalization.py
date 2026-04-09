import pandas as pd

def normalize_indicator(file_name, indicator_name):

    df = pd.read_csv('../cleaned_data/' + file_name)

    # normalize the indicator values using min-max normalization
    df[indicator_name + ' (normalized)'] = (df[indicator_name] - df[indicator_name].min()) / (df[indicator_name].max() - df[indicator_name].min())

    # save new column to file
    df.to_csv('../cleaned_normalized_data/' + file_name, index=False)

    return df