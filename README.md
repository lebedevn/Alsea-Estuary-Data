Alsea River Data Analysis of Temperature & Salinity Variability and Flow Rate for 2012-2013 and 2013-2014
Copyright (C) 2024 Nika Lebedev, Oregon State University 

These code files import matlab data files that contain temperature and time data from three different sites in the Alsea Estuary for surface files, and four different sites in the Alsea Estuary for bottom files. 
The code relies on the following Python modules:
  pandas - data frame support
  scipy.io - matlab files import
  numpy - math functions and arrays support
  datetime - timestamps support
  matplotlib - graphin and visualizations

The temperature data is extracted and the files for each site are added to contain the full season that the data was taken. The same is done for the salinity data for each site and year.

Running through all the files for a specific season and surface/bottom, the initial and final date are found for the site. A master timeline is made from these initial and final values with a data point every five minutes, using Matlab date format.
Each location is interpolated along this time standard using numpy's interpol function. Gaps longer than 3 hours are marked as NaNs and not shown on the later plots.
The time is then converted from matlab date num to python date time format. 
For each season and surface/bottom, there are three subplots: temperature, salinity, and the Flow Rate data taken from the USGS dashboard. 
The flow rate data was imported from USGS archives and converted from cubic feet per second to cubic meters per second. 
The interpolated data files, and converted flow rate data is turned into csv files which are also found within the repository.
All of the original matlab files and csv files before data processing are found in the repository as well. 

For processing the data, I identified areas where there was definite biofouling or the sensors were clearly buried or out of the water. These areas had consistent salinity readings over several days and/or weeks. 

For starters I went through the entirety of the time record for the mid estuary and upriver locations. I determined all of the data to be valid and correct.

With the downriver data however, there were obvious cases of biofouling, missing data due to plugged sensors, and generally drifting of sensor data. For this reason, I removed certain bottom salinity and temperature data from the record that were bad data. 
I used the remainder of the bottom salinity data to scale the surface salinity data that had drifted using two main methods. The first was to take the average values of the maxes of both the surface and bottom salinity and divide the bottom salinity average by the surface
salinity. I then multiplied this scale factor to every data point for that range in the salinity time series. The second method I used was to take a roving scale factor. This consisted of identifying a singular data point and taking the average of the 99th percentile of the values 
of the surface and bottom salinity for the previous and future 24 hours. When 24 hours before or after were not available these were marked as NaNs in the calculations. The data point was then multiplied by the ratio of bottom to surface. 

After each time series was processed and all data scaled and deemed to be correct, the arrays were combined into one DataFrame that was then exported to CSV format. The summary files were then created by importing the CSV files. 



