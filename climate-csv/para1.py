
from netCDF4 import Dataset 
import numpy as np



rootgrp = Dataset("CZ16_1_2000m_Temp_year_2019_month_01.nc", "r", format="NETCDF4")

print(rootgrp)

rootgrp.close()