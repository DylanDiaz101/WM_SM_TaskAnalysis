# SM Letter Position Block 1 Analysis

import pandas as pd
import numpy as np

# IMPORTANT: DEFINE YOUR FILE PATHS
datafile_PATH = r'C:\Users\dylan\Desktop\WM_SM_TaskAnalysis\example_data\sm_letterposition_1\sm_letterposition_1_raw_jreimer.csv' # should be a .csv file
desired_output_PATH = r'C:\Users\dylan\Desktop\WM_SM_TaskAnalysis\example_output\sm_letterpos_block1_output.xlsx' # should be an .xlsx file
# ******************************************************************************** #

# Read the csv file
df = pd.read_csv(datafile_PATH)

#IMPORTANT: Filter data to include only rows with SPECIFIC blocknum ex. '6' which indicates real trials *************
df_filtered = df[df['blocknum'] == 6]

# Re-calculate with the count of blocknum 6 or 7 for each subject and update the DataFrame with this information ----- *

# Calculate the mean of 'correct' and count the occurrences for blocknum 6 for each subject
aggregated_data = df_filtered.groupby('subject').agg(
    mean_score=('correct', 'mean'),
    total_number_of_trials=('blocknum', 'size')
)

# Round the mean_score to four decimal places
aggregated_data['mean_score'] = aggregated_data['mean_score'].round(4)

# Write to Excel with the specified precision and count included
aggregated_data.to_excel(desired_output_PATH, index_label='subject_id')

print("COMPLETED")
