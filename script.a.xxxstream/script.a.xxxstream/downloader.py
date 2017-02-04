import xbmcgui
import urllib
import time
 
urllib.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'

def download(url, dest, dp = None):
    if not dp:
        dp = xbmcgui.DialogProgress()
        dp.create("Kobra XXX stream","Downloading Content",' ', ' ')
    dp.update(0)
    start_time=time.time()
    urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))
     
def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100) 
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0 and not percent == 100: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0
            kbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '[CR][COLOR ghostwhite]DOWNLOADING[/COLOR][COLOR darkred] %.02f MB[/COLOR] [COLOR ghostwhite]OF[/COLOR] [COLOR darkred]%.02f MB[/COLOR]' % (currently_downloaded, total) 
            e = '[COLOR ghostwhite]SPEED:[/COLOR] [COLOR darkred]%.02f Kb/s [/COLOR]' % kbps_speed 
            e += '[COLOR ghostwhite]ETA:[/COLOR] [COLOR darkred]%02d:%02d[/COLOR]' % divmod(eta, 60)
            f = '[COLOR ghostwhite]PLEASE WAIT[/COLOR]'
            dp.update(percent, mbs, e, f)
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled(): 
            raise Exception("Canceled")
            dp.close()
