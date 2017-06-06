
import json
import urllib2

import helper

class ClientException(Exception):
    pass

class Client(object):

    def __init__(self, opts):
        self.auth_url = opts.get('auth_url')
        self.username = opts.get('username')
        self.password = opts.get('password')
        self.project_name = opts.get('project_name')
        self.user_domain_name = opts.get('user_domain_name')
        self.project_domain_name = opts.get('project_domain_name')
        self.storage_url = opts.get('storage_url')

        self._token = None
        self._service_catalog = None
        self._user = None
        self._metadata = None

        self._authenticate()

    def _authenticate(self):

        data = json.dumps({
            "auth": {
                "identity": {
                    "methods": ["password"],
                    "password": {
                        "user": {
                            "name": self.username,
                            "domain": {
                                "name": self.user_domain_name
                            },
                            "password": self.password
                        }
                    }
                },
                "scope": {
                    "project": {
                        "name": self.project_name,
                        "domain": {
                            "name": self.project_domain_name
                        }
                    }
                }
            }
        })

        url = '{}/auth/tokens'.format(self.auth_url)

        req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
        conn = urllib2.urlopen(req)
        resp = conn.read()

        response_headers = conn.info()

        self._token= response_headers.dict.get('x-subject-token')

        try:
            json_resp = json.loads(resp)
        except ValueError:
            raise ClientException('Fail to authenticate')

        conn.close()

        self._service_catalog = json_resp.get('token').get('catalog')

    def get_token(self):
         return self._token

    def get_storage_url(self):
        return self.storage_url

    def upload(self, container, path, verbose=True):
        if path[-1] == '/':
           path = path[:-1]
        files = helper.list_dir(path)
        for filename in files:
            (fh, content_type, content_length) = helper.get_file_infos(filename)
            oFileToUpload = open(filename, "rb")

            if (filename[0] == '/'):
                filename = filename[1:]

            url = "{}/{}/{}".format(self.get_storage_url(),
                                    container,
                                    filename)

            data=oFileToUpload.read()

            opener = urllib2.build_opener(urllib2.HTTPHandler)
            request = urllib2.Request(url, data=data)
            request.add_header("X-Auth-Token", self.get_token())
            request.add_header("Content-Type", content_type)

            request.get_method = lambda: "PUT"
            response = opener.open(request)
            if response.code == 201:
                msg = '{} - OK'.format(filename)
            else:
                msg = '{} - FAIL (error {})'.format(filename, response.code)
            if verbose:
                print(msg)

    def download(self, container, objectname, download_path, verbose=True):

        download_file_path = ''
        if download_path[-1] == '/':
            download_path = download_path[:-1]
        if (objectname[0] == '/'):
            objectname = objectname[1:]
        url = "{}/{}/{}".format(self.get_storage_url(),
                                container,
                                objectname)

        opener = urllib2.build_opener(urllib2.HTTPHandler)
        request = urllib2.Request(url)
        request.add_header("X-Auth-Token", self.get_token())
        response = opener.open(request)

        data = response.read()

        if '/' in objectname:
            objectname = objectname.split('/')
            objectname = objectname[-1]

        download_file_path = download_path + '/' + objectname

        with open(download_file_path, 'wb') as download_file:
            download_file.write(data)
            download_file.close()
        print (objectname + " has been downloaded in the path as: " + download_path)