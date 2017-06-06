#!/usr/bin/python -u

from optparse import OptionParser, OptionGroup
from sys import argv as sys_argv, exit

from swiftclient import Client

def upload(options):

    values = {
        'username': options.os_username,
        'password': options.os_password,
        'auth_url': options.os_auth_url,
        'project_name': options.os_project_name,
        'user_domain_name': options.os_user_domain_name,
        'project_domain_name': options.os_project_domain_name,
        'storage_url': options.os_storage_url,
    }

    container = options.container
    path = options.upload_path

    cli = Client(values)
    cli.upload(container, path)

def download(options):

    values = {
        'username': options.os_username,
        'password': options.os_password,
        'auth_url': options.os_auth_url,
        'project_name': options.os_project_name,
        'user_domain_name': options.os_user_domain_name,
        'project_domain_name': options.os_project_domain_name,
        'storage_url': options.os_storage_url,
    }

    container = options.container
    objectname = options.object
    download_path = options.download_path

    cli = Client(values)
    cli.download(container, objectname, download_path)

def main(arguments=None):
    if arguments:
        argv = arguments
    else:
        argv = sys_argv

    version = '0.0.1'

    parser = OptionParser(version='%%prog %s' % version,
                          usage='''
Command-line interface to the OpenStack Swift API.

usage: %%prog [--version] [--help]

Mandatory Switch: 
             [--os-username <auth-user-name>]
             [--os-password <auth-password>]
             [--os-project-name <auth-project-name>]
             [--os-auth-url <auth-url>]
             [--os-user-domain-name <auth-user-domain-name>]
             [--os-project-domain-name <auth-project-domain-name>]
             [--os-storage-url <storage-url>]
             [--operation-type <operation-type>]
             [--container <container-name>]

Command Specific Switch:

For Upload (Uploads files or directories to the given container from the upload path.):
             [--upload-path <upload-path>]

For Download (Downloads files from the given container in the download path.):
             [--object <object-name>]
             [--download-path <download-path>]          
'''.strip('\n') % globals())
    parser.add_option('--insecure',
                      action="store_true", dest="insecure",
                      default=True,
                      help='Allow swiftclient to access servers without '
                           'having to verify the SSL certificate. '
                           'Defaults to env[SWIFTCLIENT_INSECURE] '
                           '(set to \'true\' to enable).')

    os_grp = OptionGroup(parser, "OpenStack authentication options")

    os_grp.add_option('--os-username',
                      metavar='<auth-user-name>',
                      help='OpenStack username required to authenticate with OpenStack swift. ')
    os_grp.add_option('--os_username',
                      help='OpenStack username required to authenticate with OpenStack swift. ')
    os_grp.add_option('--os-password',
                      metavar='<auth-password>',
                      help='OpenStack password required to authenticate with OpenStack swift.')
    os_grp.add_option('--os-user-domain-name',
                      metavar='<user-domain-name>',
                      help='OpenStack user domain name required to connect with OpenStack swift.')
    os_grp.add_option('--os-project-name',
                      metavar='<project-name>',
                      help='OpenStack project name required to connect with OpenStack swift.')
    os_grp.add_option('--os-project-domain-name',
                      metavar='<project-domain-name>',
                      help='OpenStack project domain name required to connect with OpenStack swift.')
    os_grp.add_option('--os-auth-url',
                      metavar='<auth-url>',
                      help='OpenStack auth URL required to authenticate with OpenStack Identity to get the '
                           'authentication token.')
    os_grp.add_option('--os-storage-url',
                      metavar='<storage-url>',
                       help='OpenStack storage URL required to connect with the OpenStack Swift.')
    os_grp.add_option('--operation-type',
                      metavar='<operation-type>',
                      help='Specified OpenStack swift related operation which can be upload or download.')
    os_grp.add_option('--container',
                      metavar='<container-name>',
                      help='Specified container name to upload/download object.')
    os_grp.add_option('--object',
                      metavar='<object-name>',
                      help='Specified object name to be downloaded in the downloaded path.')
    os_grp.add_option('--upload-path',
                      metavar='<upload-path>',
                      help='Upload path of the file or directory.')
    os_grp.add_option('--download-path',
                      metavar='<download-path>',
                      help='Download path to download the object.')

    (options, args) = parser.parse_args(argv[1:])

    try:
        if(options.operation_type == 'upload'):
            if(options.upload_path is None):
                parser.print_help()
                exit()
            else:
                upload(options)
        elif(options.operation_type == 'download'):
            if (options.object is None and options.download_path is None):
                parser.print_help()
                exit()
            else:
                download(options)
        else:
            parser.print_help()
            exit()

    except Exception as err:
        print(str(err))

if __name__ == '__main__':
    main()
