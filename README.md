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
The flow rate data was imported from NOAA archives and converted from cubic feet per second to cubic meters per second. 
The interpolated data files, and converted flow rate data is turned into csv files which are also found within the repository.
All of the original matlab files and csv files before data processing are found in the repository as well. 

For processing the data, I identified areas where there was definite biofouling or the sensors were clearly buried or out of the water. These areas had consistent salinity readings over several days and/or weeks. 

