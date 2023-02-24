from urllib import request

host = "10.4.1.150"
dest_dir = "."
request.urlretrieve("http://{}/download/", dest_dir)
