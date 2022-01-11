import glob
import re
import time_htht as htt
import os


# move data to select era dir
if True:  # {{{
    infiles = glob.glob('/pub/ldx/era/src/201*_0.125x0.125_ldx')  # /pub/ldx/era/src/2017072206_0.125x0.125_ldx
    for infile in infiles:
        stime = re.search(r'(\d{10})', infile).group(1)+'0000'
        ctime = htt.str2time(stime)
        outdir = '/run/media/ldx/My Passport/newJC/selec-era5/'+htt.time2str(ctime, 'yyyy')+'/'

        os.system('cp '+infile+' '+outdir)
# }}}
