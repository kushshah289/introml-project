import sys
import os
import urllib.request

def download_progress(count, block_size, total_size):
    pct_complete = float(count * block_size) / total_size

    msg = "\r- Download progress: {0:.1%}".format(pct_complete)

    sys.stdout.write(msg)
    sys.stdout.flush()
	

def weights_download(url): 
    fname = url.split('/')[-1]
    if not os.path.exists(fname):
        fpath, _ = urllib.request.urlretrieve(url=url,
                                                  filename=fname,
                                                  reporthook=download_progress)

        print()
        print("Download finished")

        
    else:
        print("Data has already been downloaded")