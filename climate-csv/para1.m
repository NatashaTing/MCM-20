function para1

finfo = ncinfo('CZ16_1_2000m_Temp_year_2019_month_01.nc');
%ncdisp('CZ16_1_2000m_Temp_year_2019_month_01.nc')
disp(finfo);
creation_date = ncreadatt('CZ16_1_2000m_Temp_year_2019_month_01.nc','Temperature','scale_factor');


%vardata = ncread('CZ16_1_2000m_Temp_year_2019_month_01.nc','temp');


end

