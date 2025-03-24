Alsea surface heat flux readme
Margaret Conley
13 March 2025

These csv files contain timeseries of:
- Tm: time in UTC
- U: wind speed at 10 m (m s-1)
- Tair: air temperature at 2 m (degrees C)
- RH: relative humidity at 2 m (%)
- P: sea level air pressure (mb)
- SW_dn: downward shortwave radiation (W m-2)
- LW_dn: downward longwave radiation (W m-2)
- Lat: site latitude (constant)
- Lon: site longitude (constant)

There are two files each for 7 sites:
- coastal ocean
- weather station downriver (to compare observed and modeled data)
- downriver
- minilander
- mid-estuary
- upriver
- river at Tidewater gauge

The two sets of files contain data from 2012-12-12 to 2013-05-21 and 2013-10-24 to 2014-03-12, respectively. Data are hourly values from a WRF (Weather Research & Forecasting) model of the Pacific Northwest at 4 km resolution, spatially interpolated to the measurement sites by calculating a distance-weighted average of the 4 nearest grid points to each measurement site. On 2014-01-07, no data were available at 4 km resolution and data from a 12 km resolution model were used instead, following the same procedure. On 2024-01-29, two gaps (14:00-18:00 UTC and 20:00-23:00 UTC) were filled using linear interpolation.

To calculate the surface heat flux at each site, you will need to match the heat flux variables in these files (U, Tair, RH, P, SW_dn, and LW_dn) to the water temperature (Tsea) and salinity (Ss) at each measurement site (using the data that is closest to the surface for that site). You will also need to include the depth of the water temperature and salinity measurement (Ts_depth). If you have temperature data but no salinity data, you can fill in the salinity using a default value that makes sense for that site and time of year.

COARE also requires some constants that are the same for all sites:
- Zu = 10 (height of wind measurement in m)
- Zt = 2 (height of air temperature measurement in m)
- Zq = 2 (height of humidity measurement in m)
- Zi = 600 (inversion height in m)

COARE requires that the time be in Julian days (Jd), which is the number of days since 1858-11-17.

We will skip the rain heat flux calculation, so you can set Rainrate = NaN.

To get the surface heat flux, you need to call the coare36vnWarm_et function using all of the variables discussed above. You only need some of the outputs from the function, which will be stored in an array called "A":

A=coare36vnWarm_et(Jd, U, Zu, Tair, Zt, RH, Zq, P, Tsea, SW_dn, LW_dn, Lat, Lon, Zi, Rainrate, Ts_depth, Ss)

If the output array has the same structure as in Matlab, you'll want all the values in a particular column to get that component of heat flux for all times (rows = time, columns = output variables)
- hsb = sensible heat flux = third column
- hlb = latent heat flux = fourth column
- lw_net = net longwave  = 28th column
- sw_net = net shortwave = 29th column

Then you can calculate the net surface heat flux, Qnet:
Qnet = sw_net + lw_net - hsb - hlb

The sensible and latent heat fluxes are multiplied by -1 because they are defined as positive when heating the air, and the net sw and lw are defined as positive when heating the ocean. We want Qnet to be positive when heating the ocean. You can repeat this for each site and each year to get net heat flux values for all of your temperature data sites and times.

References:

MacCready, P., McCabe, R. M., Siedlecki, S. A., Lorenz, M., Giddings, S. N., Bos, J., et al. (2021). Estuarine Circulation, Mixing, and Residence Times in the Salish Sea. Journal of Geophysical Research: Oceans, 126(2), e2020JC016738. https://doi.org/10.1029/2020JC016738

Mass, C. F., Albright, M., Ovens, D., Steed, R., Maciver, M., Grimit, E., et al. (2003). Regional Environmental Prediction Over the Pacific Northwest. Bulletin of the American Meteorological Society, 84(10), 1353–1366. https://doi.org/10.1175/BAMS-84-10-1353

Fairall, C. W., Blomquist, B., Bariteau, L., & Edson, J. B. (2022). COARE-algorithm/Python/COARE3.6: Original Release [software]. Github. Retrieved from https://github.com/NOAA-PSL/COARE-algorithm/tree/master/Python/COARE3.6

Fairall, C. W., Bradley, E. F., Rogers, D. P., Edson, J. B., & Young, G. S. (1996). Bulk parameterization of air-sea fluxes for Tropical Ocean-Global Atmosphere Coupled-Ocean Atmosphere Response Experiment. Journal of Geophysical Research: Oceans, 101(C2), 3747–3764. https://doi.org/10.1029/95JC03205

Edson, J. B., Jampana, V., Weller, R. A., Bigorre, S. P., Plueddemann, A. J., Fairall, C. W., et al. (2013). On the Exchange of Momentum over the Open Ocean. Journal of Physical Oceanography, 43(8), 1589–1610. https://doi.org/10.1175/JPO-D-12-0173.1
