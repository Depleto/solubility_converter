import pandas as pd
import numpy as np
import re

X = None
Y = None


data = pd.read_csv("reaxysleft2.csv")

exp_sol = data["comment"]  # column with experimental sol
mol_mass = data["Molar Mass"] # column with molar mass
conv_sol = data["Experimental Solubility in Water (mg/L)"] # column for converted sol

real = r'-?(\d\.?\d*[Ee][+\-]?\d+|(\d+\.\d*|\d*\.\d+)|\d+)'
up_to_solvent = r'.+?(?=solvent)'
up_to_substance = r'.+?(?=substance)'
for i,sol in enumerate(exp_sol):
    if "percent" in sol and "mol" in sol:
        pass

    elif "percent" in sol:
        pass

    elif "part" in sol and "Substance" in sol:
        pass

    elif "g/kg" in sol:
        pass

    elif "mug/ml" in sol:

















