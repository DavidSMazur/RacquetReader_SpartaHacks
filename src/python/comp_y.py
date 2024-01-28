import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

file_number_0 = '6'
file_number_1 = '7'
height = 1080

def visualize_height_differences(center_df, wrist_df, height, file_number):
    '''Visualize the normalized height difference across tracks'''
    plt.figure(figsize=(10, 6))

    # Scatter plot for center_history_0
    plt.scatter(center_df.index, center_df['normalized_height_difference'], label='Center History 0', alpha=0.5)

    # Scatter plot for wrist_history_0
    plt.scatter(wrist_df.index, wrist_df['normalized_height_difference'], label='Wrist History 0', alpha=0.5)

    # Scatter plot for center_history_1
    plt.scatter(center_df.index, center_df['normalized_height_difference'], label='Center History 1', alpha=0.5)

    # Scatter plot for wrist_history_1
    plt.scatter(wrist_df.index, wrist_df['normalized_height_difference'], label='Wrist History 1', alpha=0.5)

    plt.xlabel('Track IDs')
    plt.ylabel('Normalized Height Difference')
    plt.title(f'Normalized Height Difference Across Tracks (File {file_number})')
    plt.legend()
    plt.show()

def extract_numeric_value_from_tuple(string_representation):
    try:
        tuple_values = eval(string_representation)
        numeric_value = float(tuple_values[0])
        return numeric_value
    except (SyntaxError, TypeError, IndexError, ValueError):
        return pd.NaT

def calculate_normalized_height_difference(df_0, df_1, height):
    # Merge the two dataframes on the track IDs
    merged_df = pd.merge(df_0, df_1, left_index=True, right_index=True, suffixes=('_0', '_1'))
    merged_df['1_1'] = merged_df['1_1'].apply(extract_numeric_value_from_tuple)
    merged_df['1_0'] = merged_df['1_0'].apply(extract_numeric_value_from_tuple)
    merged_df['normalized_height_difference'] = (merged_df['1_1'] - merged_df['1_0']) / height
    return merged_df

def visualize_heatmap(df, file_number):
    plt.figure(figsize=(12, 8))
    # sns.heatmap(df, cmap='viridis', annot=True, fmt=".2f", cbar_kws={'label': 'Normalized Height Difference'})
    plt.title(f'Heatmap of Normalized Height Differences (File {file_number})')
    plt.show()

def visualize_trajectory_map(df, file_number):
    plt.figure(figsize=(10, 6))
    for col in df.columns:
        plt.plot(df.index, df[col], label=f'Node {col}')
    plt.xlabel('Timestamp')
    plt.ylabel('Normalized Height Difference')
    plt.title(f'Trajectory Map of Normalized Height Differences (File {file_number})')
    plt.legend()
    plt.show()

def main():
    file_number = '1'
    csv_path = Path('output/csv')
    height = 1080
    # Define folder number
    file_number_0 = '0'
    file_number_1 = '1'

    # Load center history and wrist history for file 0
    # Load the center history CSV files
    csv_path = Path('output/csv')
    height = 1080  # Adjust this value based on your video height
    center_df_0 = pd.read_csv(csv_path / f'center_history_{file_number_0}.csv', index_col=0)
    wrist_df_0 = pd.read_csv(csv_path / f'wrist_history_{file_number_0}.csv', index_col=0)

    # Load center history and wrist history for file 1
    center_df_1 = pd.read_csv(csv_path / f'center_history_{file_number_1}.csv', index_col=0)
    wrist_df_1 = pd.read_csv(csv_path / f'wrist_history_{file_number_1}.csv', index_col=0)

    # Calculate the normalized height differences
    result_center_0 = calculate_normalized_height_difference(center_df_0, center_df_1, height)
    result_wrist_0 = calculate_normalized_height_difference(wrist_df_0, wrist_df_1, height)

    # Display the result dataframes
    print(result_center_0.head())
    print(result_wrist_0.head())

    # Calculate the normalized height difference
    result_df = calculate_normalized_height_difference(center_df_0, center_df_1, height)

    # Visualize the result dataframes
    visualize_height_differences(result_center_0, result_wrist_0, height, file_number)

    # Visualize the heat map
    visualize_heatmap(result_center_0, file_number)

    # Visualize the trajectory map
    visualize_trajectory_map(result_center_0, file_number)

    # Display the result dataframe
    print(result_df)

if __name__ == "__main__":
    main()
