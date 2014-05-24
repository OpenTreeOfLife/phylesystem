#!/usr/bin/env python
from peyotl.phylografter.sync import PhylografterNexsonDocStoreSync
import sys
import os

def get_default_dir_dict(top_level=None):
    r = '.' if top_level is None else top_level
    t = os.path.abspath(r)
    d = {'nexson_dir': t,
         'nexson_state_db': os.path.join(t, '.sync_status.json'), # stores the state of this repo. *very* hacky primitive db.
        }
    return d


if __name__ == '__main__':
    if '-h' in sys.argv:
        sys.stderr.write('''sync.py is a short-term hack.

It stores info about the last communication with phylografter in .to_download.json
Based on this info, it tries to download as few studies as possible to make 
the NexSONs in treenexus/studies/#/... match the export from phylografter.

   -h gives this help message.

If other arguments aree supplied, it should be the study #'s to be downloaded.
''')
        sys.exit(0)

    dd = get_default_dir_dict()
    if len(sys.argv) > 1:
        to_download = sys.argv[1:]
    else:
        to_download = None
    sync = PhylografterNexsonDocStoreSync(dd)
    sync.run(to_download=to_download)

