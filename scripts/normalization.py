import pandas as pd

def normalize_indicator(file_name, indicator_name, output_name=None):

    df = pd.read_csv('../cleaned_data/' + file_name)

    # normalize the indicator values using min-max normalization
    df[indicator_name + ' (normalized)'] = (df[indicator_name] - df[indicator_name].min()) / (df[indicator_name].max() - df[indicator_name].min())

    # save new column to file
    output_file = output_name if output_name is not None else file_name
    df.to_csv('../cleaned_normalized_data/' + output_file, index=False)

    return df


def normalize_indicator_flip(file_name, indicator_name, output_name=None):

    df = pd.read_csv('../cleaned_data/' + file_name)

    # normalize the indicator values using min-max normalization
    df[indicator_name + ' (normalized)'] = (df[indicator_name] - df[indicator_name].min()) / (df[indicator_name].max() - df[indicator_name].min())

    # flip the normalized values by subtracting from 1
    df[indicator_name + ' (normalized)'] = 1 - df[indicator_name + ' (normalized)']

    # save new column to file
    output_file = output_name if output_name is not None else file_name
    df.to_csv('../cleaned_normalized_data/' + output_file, index=False)

    return df