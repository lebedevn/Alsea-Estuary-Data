import pandas as pd
import scipy.io as sio
import numpy as np
import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

#import down river data
matDataD1 = sio.loadmat('C:\\Users\\23nik\\Downloads\\mcat_dnriver_7162_Dep1.mat')
matDataD2 = sio.loadmat('C:\\Users\\23nik\\OneDrive - Oregon State University\\Desktop\\Python\\mcat_dnriver_7162_Dep2.mat')
matDataD3 = sio.loadmat('C:\\Users\\23nik\\OneDrive - Oregon State University\\Desktop\\Python\\mcat_dnriver_6865_Dep3.mat')

#import upriver data
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

matDDF = pd.concat([matD1DF, matD2DF, matD3DF])
tmsDownriver = matDDF['DN'] * np.timedelta64(1, 'D') + origin


#combining the upriver data
matDataU1Filtered = {dictKey:dictValue for dictKey, dictValue in matDataU1.items() if dictKey[0] != '_'}
matU1DF = pd.DataFrame({dictKey: np.array(dictValue).flatten() for dictKey, dictValue in matDataU1Filtered.items()})
matDataU2Filtered = {dictKey:dictValue for dictKey, dictValue in matDataU2.items() if dictKey[0] != '_'}
matU2DF = pd.DataFrame({dictKey: np.array(dictValue).flatten() for dictKey, dictValue in matDataU2Filtered.items()})
matDataU3Filtered = {dictKey:dictValue for dictKey, dictValue in matDataU3.items() if dictKey[0] != '_'}
matU3DF = pd.DataFrame({dictKey: np.array(dictValue).flatten() for dictKey, dictValue in matDataU3Filtered.items()})

matUDF = pd.concat([matU1DF, matU2DF, matU3DF])
tmsUpriver = matUDF['DN'] * np.timedelta64(1, 'D') + origin

#plotting subplots
fig, (ax,axdiff) = plt.subplots(2,figsize=(14, 8))
ax.set_title("Temperature Downriver and Upriver vs. Time")
#add second plot below that shows temperature difference
axdiff.set_title("Difference Between Temperature at Downriver and Upriver vs. Time")
plt.setp(ax, ylabel = "Temperature ($^\circ$C)")
plt.setp(axdiff, ylabel = "Temperature ($^\circ$C)")
ax.plot(tmsUpriver, matUDF['T'], color = 'orange', label='Upriver')
ax.plot(tmsDownriver,matDDF['T'], color = 'blue', label = 'Downriver')
axdiff.plot(tmsDownriver,matDDF['T']-matUDF['T'],color = 'black', label = "Difference")

# Change the tick interval
ax.xaxis.set_major_locator(mdates.DayLocator(interval=5)) 
axdiff.xaxis.set_major_locator(mdates.DayLocator(interval=5))
# Puts x-axis labels on an angle
ax.xaxis.set_tick_params(rotation = 30)  
axdiff.xaxis.set_tick_params(rotation = 30)
plt.subplots_adjust(hspace=1)

ax.legend() 
plt.show()
