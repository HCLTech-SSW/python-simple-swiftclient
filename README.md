
---
Title: python-simple-swiftclient
Description: This project is owned by HCL Tech System Software team to provide the simple swift client to support the object upload and download operation over OpenStack Swift.
Owner of the Project: HCL Tech System Software Team
Contributor: HCL Tech System Software Team
Mail To: hcl_ss_oss@hcl.com
Tags: python-simple-swiftclient, swift-client, swift-python-library, simple-swiftclient.
Created:  2017 Jun 05
Modified: 2017 Jun 06
---

python-simple-swiftclient 
=========================

Overview of the Project
=======================
The project python-simple-swiftclient can be used for operating the operations (Upload and Download) of OpenStack Swift Mitaka release as a Client to manage objects using python standard libraries.

How to Install
==============
In order to install the client, the following command will be used:<pre>pip install python-simple-swiftclient </pre>

How to Execute
==============
For Upload operation the following command will be executed:
<pre>
python-simple-swiftclient --os-username [username] --os-password [password] --os-project-name [project name] --os-auth-url [http://yourhost:35357/v3] --os-user-domain-name [user domain name] --os-project-domain-name [project domain name] --os-storage-url [http://yourhost:8080/v1/AUTH_tenant_id] --operation-type upload --container [container name] --upload-path [Upload path of File or Directory]
</pre>

For Download operation the following command will be executed:
<pre>
python-simple-swiftclient --os-username [username] --os-password [password] --os-project-name [project name] --os-auth-url [http://yourhost:35357/v3] --os-user-domain-name [user domain name] --os-project-domain-name [project domain name] --os-storage-url [http://yourhost:8080/v1/AUTH_tenant_id] --operation-type download --container [container name] --object [Name of the object to be downloaded] --download-path [Download path of File] 
</pre>

Example for Operations
======================
The following directory structure explained as an example for Upload and Download operation: 
<pre>
dir1
|-- dir2
|    |-- image1.jpg 
|-- dir3
|    |-- sample.txt 
</pre>

Example 1:
<pre>
$ python-simple-swiftclient [...] --operation-type upload --container [container name] --upload-path dir1/dir2/image1.jpg 

This command will create an object over OpenStack swift named as **dir1/dir2/image1.jpg**
</pre>

Example 2:
<pre>
$ python-simple-swiftclient [...] --operation-type upload --container [container name] --upload-path dir1/ 

This command will create 2 objects over OpenStack swift named as **dir1/dir2/image1.jpg** and **dir1/dir3/sample.txt**
</pre>

Example 3:
<pre>
$ python-simple-swiftclient [...] --operation-type download --container [container name] --object dir1/dir2/image1.jpg --download-path /home/admin/download

This command will download image1.jpg from OpenStack swift to /home/admin/download
</pre>
