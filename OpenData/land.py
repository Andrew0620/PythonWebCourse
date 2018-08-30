import pandas as pd

res = pd.read_csv('./lvr_landAcsv/A_LVR_LAND_A.CSV', encoding='big5')

print(res.describe())
print(res.mead())