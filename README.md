# **Working Memory Secondary Memory (SM) Task Analysis**

## **Overview**
These scripts compute **mean accuracy and total trial counts** for working memory performance in the **Secondary Memory (SM) tasks** (letter position and word-word) developed by:
- Oliver Wilhelm (University of Ulm, Germany)  
- Andrea Hildebrandt (Humboldt-Universität zu Berlin, Germany)  
- Klaus Oberauer (University of Zurich, Switzerland)  

The tasks were adapted as a measure of **Long-Term Memory (LTM) retrieval** for the study:  
> **"The Psychometric Structure of Working Memory: An Analysis Utilizing Network Modeling"**  
> Presented at the **65th Annual Meeting of the Psychonomic Society**  
> **Principal Investigators:** Kevin P. Rosales & Jason F. Reimer (California State University, San Bernardino)
(A copy of the poster is included in the `readings` folder.)

## **Reference**
For more details on the **Secondary Memory (SM) tasks**, refer to:  
📄 **Wilhelm et al. (2013):** *"What is working memory capacity, and how can we measure it?"*  
(A copy is included in the `readings` folder.)

## **Repository Structure**
```
📂 example_data/         # Sample participant data (Inquisit .csv files)
📂 example_output/      # Sample output (.xlsx files)
📂 readings/     # Relevant articles and study materials
sm_letterpos_block1_analysis.py   # Script 1
sm_letterpos_block2_analysis.py   # Script 2
sm_wordword_task_analysis.py      # Script 3
README.md        # This document
```

## **Data Collection & Processing**
- **Participant data** was collected using **Inquisit** ([Millisecond Software](https://www.millisecond.com/about)).  
- Raw data was **downloaded and saved as .csv** files for processing.  
- The scripts filter **real trials**, compute **accuracy metrics**, and export summary statistics.  

## **Usage**
1. **Specify input and output file paths:**  
   - The scripts take input specified by the `datafile_PATH` variable.  
   - Processed results are saved at the location specified by `desired_output_PATH`.
   
2. **Run the script:**  
   - Ensure your `.csv` data files are inside a `data/` folder. `example_data/` is included.  
   - Modify `datafile_PATH` and `desired_output_PATH` as needed.  
   - Execute the script in Python.  

3. **View the output:**  
   - Processed results will be stored in **Excel (.xlsx) format** at the designated output path. `example_output/` is included.

## **Example (Python Script)**
```python
# Define file paths
datafile_PATH = r"/path/to/your/input_data.csv"
desired_output_PATH = r"/path/to/your/output_results.xlsx"

# Read the csv file
df = pd.read_csv(datafile_PATH)

# Process and export results
df.to_excel(desired_output_PATH, index=False)
print("Processing Complete.")
```
