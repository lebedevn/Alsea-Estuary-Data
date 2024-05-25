import pandas as pd
import scipy.io as sio
import numpy as np
import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

# mat Data = downriver, mat Data2 = upriver
#combine dictionaries for down river data
matDataD1 = sio.loadmat('C:\\Users\\23nik\\Downloads\\mcat_dnriver_7162_Dep1.mat')
matDataD2 = sio.loadmat('C:\\Users\\23nik\\OneDrive - Oregon State University\\Desktop\\Python\\mcat_dnriver_7162_Dep2.mat')
matDataD3 = sio.loadmat('C:\\Users\\23nik\\OneDrive - Oregon State University\\Desktop\\Python\\mcat_dnriver_6865_Dep3.mat')

#combine dictionaries for upriver data
matDataU1 = sio.loadmat('C:\\Users\\23nik\\Downloads\\mcat_upriver_6865_Dep1.mat')
matDataU2 = sio.loadmat('C:\\Users\\23nik\\OneDrive - Oregon State University\\Desktop\\Python\\mcat_upriver_6865_Dep2.mat')
matDataU3 = sio.loadmat('C:\\Users\\23nik\\OneDrive - Oregon State University\\Desktop\\Python\\mcat_upriver_7162_Dep3.mat')

#mat lab date origin
origin = np.datetime64('0000-01-01', 'D') - np.timedelta64(1, 'D')

#combining the downriver data
matDataD1Filtered = {dictKey:dictValue for dictKey, dictValue in matDataD1.items() if dictKey[0] != '_'}
matD1DF = pd.DataFrame({dictKey: np.array(dictValue).flatten() for dictKey, dictValue in matDataD1Filtered.items()})
matDataD2Filtered = {dictKey:dictValue for dictKey, dictValue in matDataD2.items() if dictKey[0] != '_'}
matD2DF = pd.DataFrame({dictKey: np.array(dictValue).flatten() for dictKey, dictValue in matDataD2Filtered.items()})
matDataD3Filtered = {dictKey:dictValue for dictKey, dictValue in matDataD3.items() if dictKey[0] != '_'}
matD3DF = pd.DataFrame({dictKey: np.array(dictValue).flatten() for dictKey, dictValue in matDataD3Filtered.items()})

#matUDF = pd.concat([matD1DF, matD2DF, matD3DF]) doesn't work well since 11 month gap
matDDF = pd.concat([matD2DF, matD3DF])
tmsDownriver = matDDF['DN'] * np.timedelta64(1, 'D') + origin


#combining the upriver data
matDataU1Filtered = {dictKey:dictValue for dictKey, dictValue in matDataU1.items() if dictKey[0] != '_'}
matU1DF = pd.DataFrame({dictKey: np.array(dictValue).flatten() for dictKey, dictValue in matDataU1Filtered.items()})
matDataU2Filtered = {dictKey:dictValue for dictKey, dictValue in matDataU2.items() if dictKey[0] != '_'}
matU2DF = pd.DataFrame({dictKey: np.array(dictValue).flatten() for dictKey, dictValue in matDataU2Filtered.items()})
matDataU3Filtered = {dictKey:dictValue for dictKey, dictValue in matDataU3.items() if dictKey[0] != '_'}
matU3DF = pd.DataFrame({dictKey: np.array(dictValue).flatten() for dictKey, dictValue in matDataU3Filtered.items()})

#matUDF = pd.concat([matU1DF, matU2DF, matU3DF]) doesn't work well since 11 month gap
matUDF = pd.concat([matU2DF, matU3DF])
tmsUpriver = matUDF['DN'] * np.timedelta64(1, 'D') + origin

#plotting subplots
fig, (ax1,ax2) = plt.subplots(2,figsize=(14, 8))
ax1.set_title("Temperature Upriver vs. Time")
ax2.set_title("Temperature Downriver vs. Time")
plt.setp(ax1, ylabel = "Temperature ($^\circ$C)")
plt.setp(ax2, ylabel = "Temperature ($^\circ$C)")
ax1.plot(tmsUpriver, matUDF['T'])
ax2.plot(tmsDownriver,matDDF['T'], 'tab:orange')
plt.subplots_adjust(hspace=1)
# Change the tick interval
ax1.xaxis.set_major_locator(mdates.DayLocator(interval=5)) 
ax2.xaxis.set_major_locator(mdates.DayLocator(interval=5)) 

# Puts x-axis labels on an angle
ax1.xaxis.set_tick_params(rotation = 30)  
ax2.xaxis.set_tick_params(rotation = 30)  

plt.show()