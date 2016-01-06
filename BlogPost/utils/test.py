#encoding = utf8
from BlogPost.utils.tasks import Add1
print 'test===>1'
# res = Add1.apply_async(args=[1,2], queue='z2', routing_key='z2')
res = Add1.delay(1,2)
print 'test===>2'
print res.ready()
print res.get()