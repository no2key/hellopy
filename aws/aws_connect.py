"""boto 操作aws s3 浪费我一天时间，原来是两处都要设置区域

"""


import boto.s3
from boto.s3.connection import Location
from boto.s3.key import Key

s3 = boto.s3.connect_to_region('cn-north-1', aws_access_key_id='xxxxx', aws_secret_access_key='xxxxx')
boto.set_stream_logger('boto')
s3.create_bucket('xxxx', location=Location.CNNorth1)