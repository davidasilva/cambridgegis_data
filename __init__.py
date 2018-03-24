import os

def get_directory_structure(rootdir):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir = {}
    rootdir = rootdir.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        files = [path + os.sep + f for f in files]
        subdir = dict.fromkeys(files)

        
        

        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir

class filetree(object):
    def __init__(self, **response):
        for k,v in response.items():
            if isinstance(v,dict):
                k = k.lstrip('.')
                if k[0] in '1234567890':
                    k = 'dir_' + k
                self.__dict__[k.lstrip('.')] = filetree(**v)
            elif isinstance(k,str):
                try:
                    extension=None
                    fname,extension = k.split(os.sep)[-1].split('.')

                    self.__dict__[extension] = k
                except:
                    self.__dict__['files'] = [k]

            else:
                 self.__dict__[k.lstrip('.')] = v
    def __repr__(self):
        return '< Directory with: ' + str(self.__dict__.keys()) + ' >'

    def __str__(self):
        return self.__repr__()
    
    
path = os.path.dirname(__file__)
path_dict = get_directory_structure(path).values()[0]
files = filetree(**path_dict)