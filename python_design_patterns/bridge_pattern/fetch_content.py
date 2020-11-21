# bridge pattern, for fetching the following types of contents:
# A web page (based on its URL)
# A resource accessed on an FTP server
# A file on the local file system
# A database server
# here, instead of defining WebPageParser, FTPparser, etc..
# Let's try "bridging" them with a ResourceContent class.
import abc
import requests
from config import DATA_DIR
import os


# metaclass helps define the "types of types"
# and abstract base classes
class ResourceContentFetcher(metaclass=abc.ABCMeta):

    # defines the interface for the Implementor classes.
    @abc.abstractmethod
    def fetch(self, path: str):
        raise NotImplementedError


class URLFetcher(ResourceContentFetcher):
    def fetch(self, path: str):
        """
        implements what to do when fetching a URL
        """
        r = requests.get(url=path)
        r.raise_for_status()
        print(r.text)


class LocalFileFetcher(ResourceContentFetcher):
    def fetch(self, path: str):
        """
        implements what to do when fetching a local text file.
        """
        with open(path, 'r') as fh:
            print(fh.read())


class ResourceContent:
    """
    define the abstraction's interface.
    """
    def __init__(self, imp: ResourceContentFetcher):
        # the trick is to maintain a reference to an object which represents
        # the Implementor
        self._imp: ResourceContentFetcher = imp

        # define common methods
    def show_content(self, path: str):
        # use the implementor's method
        self._imp.fetch(path)


def main():
    url_fetcher = URLFetcher()
    resrc_1 = ResourceContent(imp=url_fetcher)
    resrc_1.show_content(path="http://www.python.org")
    print("---------------")
    file_fetcher = LocalFileFetcher()
    resrc_2 = ResourceContent(imp=file_fetcher)
    resrc_2.show_content(path=os.path.join(DATA_DIR, "sample.txt"))


if __name__ == '__main__':
    main()
