import glob
import re
import time_htht as htt
import os
# import h5py as h5
import netCDF4 as nc
import numpy as np


# move data to select era dir
if False:  # {{{
    infiles = glob.glob('/pub/ldx/era/src/201*_0.125x0.125_ldx')

    for infile in infiles:
        stime = re.search(r'(\d{10})', infile).group(1)+'0000'
        ctime = htt.str2time(stime)
        outdir = '/home/ldx/mp/newJC/selec-era5/' + \
            htt.time2str(ctime, 'yyyy')+'/'

        os.system('cp '+infile+' "'+outdir+'"')
# }}}

# change the name
if False:  # {{{
    for year in range(2015, 2020):
        indir = '/home/ldx/mp/newJC/selec-era5/'+str(year)+'/'
        infiles = glob.glob(indir+'*_0000_0.125x0.125.ldx.nc')
        os.chdir(indir)

        for infile00 in infiles:
            stime00 = re.search(r'(\d{4}_\d\d_\d\d_\d\d\d\d)',
                                infile00).group(1)
            stime00 = re.sub('_', '', stime00)
            ctime00 = htt.str2time(stime00+'00')
            for hour in [6, 12, 18]:
                ctime = ctime00 + hour*3600
                infile = indir+htt.time2str(ctime, 'yyyymmddHH') +\
                    '_0.125x0.125_ldx'
                outfile = indir+htt.time2str(ctime, 'yyyy_mm_dd_HHMM') +\
                    '_2.125x0.125.ldx.nc'
                cmd = 'mv '+infile+' '+outfile
                print(cmd)
                os.system(cmd)
# }}}

# calculate the yearly mean
if True:  # {{{
    for year in range(2015, 2020):
        indir = '/home/ldx/mp/newJC/selec-era5/'+str(year)+'/'
        ty = 0
        spdy = 0
        uy = 0
        vy = 0
        i = 0
        for doy in range(1, 366):
            for hour in [0, 6, 12, 18]:
                ctime = htt.vec2time(year, 1, doy, hour, 0, 0)
                infile = indir+htt.time2str(ctime, 'yyyy_mm_dd_HHMM') +\
                    '_2.125x0.125.ldx.nc'

                if not(os.path.exists(infile)):
                    continue

                dataset = nc.Dataset(infile, 'r')
                i += 1
                t = np.array(dataset['t'])
                u = np.array(dataset['u'])
                v = np.array(dataset['v'])

                if i < 2:
                    lon = np.array(dataset['longitude'])
                    lat = np.array(dataset['latitude'])
                    lev = np.array(dataset['level'])

                spd = np.sqrt(u**2+v**2)

                ty += t
                uy += u
                vy += v
                spdy += spd

        # save nc
        ncfile = nc.Dataset('outfile'+str(year)+'.nc',
                            "w", format="NETCDF4")
        ncfile.createDimension('lev', len(lev))
        ncfile.createDimension('lat', len(lat))
        ncfile.createDimension('lon', len(lon))

        ncfile.createVariable('ty', 'f32', ('lev', 'lat', 'lon'))
        ncfile.variables['ty'][:] = ty
        ncfile.createVariable('uy', 'f32', ('lev', 'lat', 'lon'))
        ncfile.variables['uy'][:] = uy
        ncfile.createVariable('vy', 'f32', ('lev', 'lat', 'lon'))
        ncfile.variables['vy'][:] = vy
        ncfile.createVariable('spdy', 'f32', ('lev', 'lat', 'lon'))
        ncfile.variables['spdy'][:] = spdy
        exit()


# }}}
