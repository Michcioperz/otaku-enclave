import mimetypes, os


class Episode(object):
    def __init__(self, show, filename):
        self.show = show
        self.filename = filename

class Show(object):
    def __init__(self, storage, codename):
        self.storage = storage
        self.codename = codename
    def episodes(self):
        return [Episode(self, i) for i in os.listdir(os.path.join(self.storage.path, self.codename)) if os.path.isfile(os.path.join(self.storage.path, self.codename, i)) and str(mimetypes.guess_type(os.path.join(self.storage.path, self.codename, i), strict=False)[0]).startswith("video/")]

class Storage(object):
    def __init__(self, path, codename):
        self.path = path
        self.codename = codename
    def shows(self):
        return [Show(self, h) for h in os.listdir(self.path) if os.path.isdir(os.path.join(self.path, h)) and len([e for e in [str(mimetypes.guess_type(os.path.join(self.path, h, f), strict=False)[0]) for f in os.listdir(os.path.join(self.path, h))] if e.startswith("video/")]) > 0] # TODO drop the bass
