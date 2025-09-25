# NE parameters
rho_pol_0_35C = {}
rho_pol_0_51C = {}
rho_pol_0_81C = {}
ksw_35C = {}
ksw_51C = {}
ksw_81C = {}
ksw_35C['PS'] = {}
ksw_51C['PS'] = {}
ksw_81C['PS'] = {}
ksw_35C['PMMA'] = {}
ksw_51C['PMMA'] = {}
ksw_81C['PMMA'] = {}

# From PVT
rho_pol_0_35C['PS'] = 1.042
rho_pol_0_51C['PS'] = 1.037
rho_pol_0_81C['PS'] = 1.030
rho_pol_0_35C['PMMA'] = 1.178
rho_pol_0_51C['PMMA'] = 1.174
rho_pol_0_81C['PMMA'] = 1.165
# Predicted with default parameters
ksw_35C['PS']['default'] = 0.00914
ksw_51C['PS']['default'] = 0.00728
ksw_81C['PS']['default'] = 0.00517
ksw_35C['PMMA']['default'] = 0.01705
ksw_51C['PMMA']['default'] = 0.01387
ksw_81C['PMMA']['default'] = 0.01025
# Predicted with fitted parameters
ksw_35C['PS']['fitted'] = 0.00829
ksw_51C['PS']['fitted'] = 0.00665
ksw_81C['PS']['fitted'] = 0.00474
ksw_35C['PMMA']['fitted'] = 0.01805
ksw_51C['PMMA']['fitted'] = 0.01356
ksw_81C['PMMA']['fitted'] = 0.00881


def get_lit_data(data_folder_path: str, sol: str, pol: str, T: float, xlxs_sheet_refno_list: list = None) -> tuple[bool, list, list, list, dict]:
    """Function to get literature data for a given solvent and polymer at a specified temperature.
    
    Args:
        data_folder_path (str): Path to the folder containing the data files.
        sol (str): Solvent name (e.g., 'CO2')
        pol (str): Polymer name (e.g., 'PS', 'PMMA')
        T (float): Temperature in Kelvin
        xlxs_sheet_refno_list (list, optional): List of reference numbers to filter sheets. 
            If None, all sheets matching the temperature pattern will be included.
    
    Returns:
        tuple: A tuple containing:
        - hasExpData (bool): True if experimental data was found, False otherwise
        - matched_sheets (list): List of sheet names that match the criteria
        - ref_no (list): List of reference numbers extracted from sheet names
        - ref_ID (list): List of reference IDs from the references file
        - dict (dict): Dictionary containing pandas DataFrames for each matched sheet
    """
    import re
    import pandas as pd
    
    # Initialize empty variables to store results
    hasExpData = None
    matched_sheets = None
    ref_no = None
    ref_ID = None
    dict = {}  # Dictionary to store DataFrames for each matched sheet
    
    # Import experimental data from Excel files
    try:
        # Construct file paths for references and database files
        path = data_folder_path
        refpath = path + "/references.xlsx"  # Path to references file
        databasepath = path + "/%s-%s.xlsx" % (sol, pol)  # Path to solvent-polymer data file
        
        # Read Excel files using pandas
        reffile = pd.ExcelFile(refpath, engine="openpyxl")
        datafile = pd.ExcelFile(databasepath, engine="openpyxl")
        
        # Find all sheets that match the temperature criteria
        matched_sheets = []
        
        if xlxs_sheet_refno_list == None:
            # If no specific reference list provided, search for all sheets at given temperature
            # Pattern matches sheets like "S_35C (...)" where 35 is T-273
            search_pattern = rf"^S_{T-273}C (.*)"
            for sheet in datafile.sheet_names:
                if re.search(search_pattern, sheet):
                    matched_sheets.append(sheet)
                    
        elif isinstance(xlxs_sheet_refno_list, list):
            # If specific reference numbers provided, only match those sheets
            for j in xlxs_sheet_refno_list:
                # Pattern matches sheets like "S_35C.({ref_no})" for specific reference numbers
                search_pattern = rf"^S_{T-273}C.\({j}\)"
                for sheet in datafile.sheet_names:
                    if re.search(search_pattern, sheet):
                        matched_sheets.append(sheet)

        # Extract reference numbers and load data from matched sheets
        ref_no = []
        for sheet in matched_sheets:
            # Load data from each matched sheet into dictionary
            dict[sheet] = pd.read_excel(databasepath, sheet)
            # Remove rows with missing pressure data
            dict[sheet].dropna(subset=["P [MPa]"], inplace=True)
            # Extract reference number from sheet name (text between parentheses)
            ref_no.append(sheet[sheet.find("(") + 1 : sheet.find(")")])

        # Get reference IDs corresponding to reference numbers
        ref_ID = []
        ref_df = pd.read_excel(reffile, "references")  # Load references sheet
        for no in ref_no:
            # Find the reference ID for each reference number
            ref_ID.append(ref_df.loc[ref_df["# ref"] == f"[{no}]", "refID"].item())
            
    except Exception as e:
        # Handle any errors during file reading or data processing
        print("")
        print("Error - importing exp data failed:")
        print(e)
        
    # Determine if experimental data was successfully found
    hasExpData = True if len(matched_sheets) > 0 else False
    
    return hasExpData, matched_sheets, ref_no, ref_ID, dict
