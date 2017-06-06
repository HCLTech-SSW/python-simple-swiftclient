import mimetypes

from os import walk, fstat
from os.path import isfile, isdir, join


def list_dir(path):
    objs = []
    dir_markers = []
    if isfile(path):
        objs.append(path)
    elif isdir(path):
        for (_dir, _ds, _fs) in walk(path):

            if not _ds + _fs:
                dir_markers.append(_dir)
            else:
                objs.extend([join(_dir, _f) for _f in _fs if not _f.startswith('.')])
    else:
        print "Specified file or directory doesn't exists."
        exit()
    return objs


def get_file_infos(filename):

    if not isfile(filename):
        return None

    fh = open(filename, 'r')
    content_length = fstat(fh.fileno())[6]
    content_type = mimetypes.guess_type(filename)[0] or 'application/octet-stream'

    return fh, content_type, content_length
