import pandas as pd

res = pd.read_csv('./lvr_landAcsv_201703/A_LVR_LAND_C.CSV', encoding='big5')

print(res.describe())
print(res.mean())