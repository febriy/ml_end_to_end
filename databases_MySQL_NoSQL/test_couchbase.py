import sys

sys.path.append("/usr/lib64/python3.7/site-packages")

import couchbase

print(couchbase.__version__)

from couchbase.admin import Admin

adm = Admin("Administrator", "123456", host="localhost", port=8091)

# https://docs.couchbase.com/python-sdk/2.4/managing-connections.html#connecting-to-a-bucket
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator

import os

docker_host = os.environ["DOCKER_HOST"]
print("couchbase://{0}".format(docker_host))

cluster = Cluster("couchbase://{0}".format(docker_host))

authenticator = PasswordAuthenticator("Administrator", "123456")
cluster.authenticate(authenticator)


bucket = cluster.open_bucket("bucket_1")


bucket.upsert(
    "entry_3",
    {
        "type": "product_2",
        "sku": "CBSRV4sdf5DP",
        "msrp": [6.43, "USD"],
        "ctime": "092011",
        "mfg": "couchbase",
        "tags": ["server", "database", "couchbase", "nosql", "fast", "json", "awesome"],
    },
)
