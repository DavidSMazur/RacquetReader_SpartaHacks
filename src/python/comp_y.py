import pandas as pd
from pathlib import Path

def calculate_normalized_height_difference(df_0, df_1, height):
    # Merge the two dataframes on the track IDs
    merged_df = pd.merge(df_0, df_1, left_index=True, right_index=True, suffixes=('_0', '_1'))

    # Calculate the normalized height difference for each track
    merged_df['normalized_height_difference'] = (merged_df['1_y'] - merged_df['1_x']) / height

    return merged_df

def main():
    # Define folder number
    file_number_0 = '0'
    file_number_1 = '1'

    # Load the center history CSV files
    csv_path = Path('output/csv')
    height = 1080  # Adjust this value based on your video height
    center_df_0 = pd.read_csv(csv_path / f'center_history_{file_number_0}.csv', index_col=0)
    center_df_1 = pd.read_csv(csv_path / f'center_history_{file_number_1}.csv', index_col=0)

    # Calculate the normalized height difference
    result_df = calculate_normalized_height_difference(center_df_0, center_df_1, height)

    # Display the result dataframe
    print(result_df)

if __name__ == "__main__":
    main()