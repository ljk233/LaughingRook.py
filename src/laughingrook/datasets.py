
import os
import requests
import pandas as pd


def cache_file(folder: str, fname: str, dir_: str = './__cache') -> str:
    """Cache a in the given dir_ with the given fname and return the
    local path.

    Preconditions:
    - lr_path exists in ljk233/lauhingrook-datasets
    - dir_ exists
    """
    remote_path = ('https://raw.githubusercontent.com'
                   + '/ljk233/laughingrook-datasets/main/'
                   + f'/{folder.rstrip("/")}/{fname}')
    local_path = f'{dir_}/{fname}'
    if fname not in os.listdir(dir_):
        r = requests.get(remote_path, allow_redirects=True)
        open(local_path, 'wb').write(r.content)
    return local_path


#def get_advent_input(year, day, cache_dir: str = '__cache') -> list | str:
#    """Cache and return an input from advent of code.
#
#    If the input spans multiple lines, a list is returned. Otherwise,
#    only the first line is returned as a string.
#    """
#    import os
#    import urllib.request
#
#    cache_files = os.listdir(cache_dir)
#    f = f'{year}_{day}.txt'
#    url = REPO + f"/aoc/{year}/{day}/input.txt"
#
#    if f not in cache_files:
#        filename, headers = urllib.request.urlretrieve(
#            url,
#            filename=f"{cache_dir}\\{f}"
#        )
#        print('file was cached.')
#
#    with open(f"{cache_dir}\\{f}") as f:
#        lines = f.read().splitlines()
#
#    if len(lines) == 1:
#        return lines[0]
#    return lines
