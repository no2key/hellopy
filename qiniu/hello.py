import qiniu.conf
import qiniu.io
import StringIO

qiniu.conf.ACCESS_KEY = ""
qiniu.conf.SECRET_KEY = ""

import qiniu.rs

policy = qiniu.rs.PutPolicy('dbimage')
uptoken = policy.token()


extra = qiniu.io.PutExtra()
extra.mime_type = 'text/plain'

data = StringIO.StringIO('hello world')
res = qiniu.io.put(uptoken, 'hello', data)

print(res)
