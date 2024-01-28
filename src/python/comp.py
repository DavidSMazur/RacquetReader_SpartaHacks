import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

def load_center_history(file_number):
    csv_path = Path('output/csv')
    center_df = pd.read_csv(csv_path / f'center_history_{file_number}.csv', index_col=0)
    
    # Convert string values to numeric (float)
    center_df = center_df.applymap(lambda x: eval(x)[0] if pd.notnull(x) else pd.NaT)

    return center_df

def compare_center_histories(center_df_1, center_df_2, threshold=0.1):
    # Get common columns between the two dataframes
    common_columns = center_df_1.columns.intersection(center_df_2.columns)
    
    # Use only common columns for the comparison
    differences = (center_df_1[common_columns] - center_df_2[common_columns]).abs()

    # Check if any difference exceeds the threshold at different parts of the center history
    exceed_threshold = (differences > threshold).any(axis=1)

    return exceed_threshold

def visualize_center_histories(center_df_1, center_df_2):
    plt.figure(figsize=(10, 6))
    
    # Get common columns between the two dataframes
    common_columns = center_df_1.columns.intersection(center_df_2.columns)
    
    for column in common_columns:
        plt.scatter(center_df_1.index, center_df_1[column], label=f'Subject 1 - {column}')
        plt.scatter(center_df_2.index, center_df_2[column], label=f'Subject 2 - {column}', alpha=0.5)
    
    plt.xlabel('Timestamp')
    plt.ylabel('Coordinate Value')
    plt.title('Comparison of Center Histories')
    plt.legend()
    plt.show()

def main():
    file_number_subject_1 = '6'
    file_number_subject_2 = '7'

    # Load center histories for two subjects
    center_df_1 = load_center_history(file_number_subject_1)
    center_df_2 = load_center_history(file_number_subject_2)

    # Compare center histories
    differences = compare_center_histories(center_df_1, center_df_2, threshold=0.1)

    # Check for differences exceeding the threshold
    if differences.any():
        print("Part of the swing needs work!")
    else:
        print("Center histories match closely.")

    # Visualize center histories
    visualize_center_histories(center_df_1, center_df_2)
    
if __name__ == "__main__":
    main()
