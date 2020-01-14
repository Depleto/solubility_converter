import pandas as pd
import re

pd.set_option('mode.chained_assignment', None)


"""
Custom function to convert solubility to mg/L (Assuming water is 

Please make sure csv file is in the script folder, or provide the full path to the csv file.

"""


# Grab data

data = pd.read_csv("reaxysleft2.csv")

exp_sol = data["comment"]  # column with experimental sol
mol_mass = data["Molar Mass"] # column with molar mass
conv_sol = data["Experimental Solubility in Water (mg/L)"] # column for converted sol


real = r'-?(\d\.?\d*[Ee][+\-]?\d+|(\d+\.\d*|\d*\.\d+)|\d+)'   # regular expression for real number

X = None
Y = None # placeholders






for i,sol in enumerate(exp_sol):

    # percent and weight-percent case
    if "percent" in sol and "mol" in sol:
        num = re.findall(real, sol)
        X = float(num[0][0])
        converted_num = (X * 10 * mol_mass[i])
        conv_sol[i] = converted_num

    elif "percent" in sol:
        num = re.findall(real, sol)
        X = float(num[0][0])
        converted_num = X * 1E4
        conv_sol[i] = converted_num

    elif "part" in sol:
        splitsol = sol.split("in")
        for string in splitsol:
            if "solvent" in string:
                n1 = re.findall(real, string)
                Y = float(n1[0][0])


            elif "substance" in string:
                n2 = re.findall(real,string)
                X = float(n2[0][0])

        conv_sol[i] = ( (X / Y) * 1e6)

    elif "g/kg" in sol:
        nums = re.findall(real, sol)
        X = float(nums[0][0])
        conv_sol[i] = X * 1e3

    elif "mug/ml" in sol:
        num = re.findall(real, sol)
        X = float(num[0][0])
        conv_sol[i] = X

    elif "p(" in sol:
        solsplit = sol.split("p(")
        for string in solsplit:
            if "olubility" in string:
                num = re.findall(real, string)
                X = float(num[0][0])

            else:
                num = re.findall(real, string)
                Y = float(num[0][0])
        conv_sol[i] = (X/Y)*1e6

    elif "mol/kg" in sol:
        num = re.findall(real, sol)
        X = float(num[0][0])
        conv_sol[i] = X * mol_mass[i] * 1e3

    elif "mumol/l" in sol:
        num = re.findall(real,sol)
        X = float(num[0][0])
        conv_sol[i] = (X * mol_mass[i]) / 1e3

    elif "mol/" in sol and "g" in sol:
        solsplit = sol.split("/")
        for string in solsplit:
            if "mol" in string:
                num = re.findall(real,string)
                X = float(num[0][0])

            elif "g" in string:
                num = re.findall(real,string)
                Y = float(num[0][0])

        conv_sol[i] = (X / Y) * mol_mass[i] * 1e6








print(conv_sol[329])













