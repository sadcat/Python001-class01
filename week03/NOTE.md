学习笔记

### twisted
- event driven
- [exarkun/pycon-presentation](https://twistedmatrix.com/~exarkun/pycon-presentation.html)
- underlying engine for scrapy
```python
from twisted.internet import defer
from twisted.web.client import getPage
from twisted.internet import reactor


# Call back for getPage
def response(*args, **kwargs):
  # print(args, kwargs)
  print('返回网页的内容')

# Call back for getPage
def callback(*args):
  print('执行了一个回调',args)

# Generates deferred obj then hands over CPU to main
@defer.inlineCallbacks
def start(url):
  deferred = getPage(url.encode('utf-8'))
  deferred.addCallback(response)
  deferred.addCallback(callback)
  yield deferred

# Callback for addboth
def stop(*args, **kwargs):
  reactor.stop()

def main():
  urls = ['http://www.baidu.com','http://www.sougou.com']
  plain_list = []

  for url in urls:
    # Won't block main thread. 
    deferred_obj = start(url)
    plain_list.append(deferred_obj)

  # Convert list to DeferredList
  deferred_obj_list = defer.DeferredList(deferredObjectList)
       
  # addboth: The deferred version of finally.
  #   Execute **stop** function when the deferred list is empty
  deferred_obj_list.addBoth(stop)
    
  reactor.run()

if __name__ == '__main__':
  main()
```

### Multi-process
#### low-level system call
- os.fork()

#### multiprocessing package
- create process
  - Process object
  - inherits from Process object, override run()
- multiprocessing.active_children()
- multiprocessing.cpu_count()
- os.getpid()
- os.getppid()

#### inter-process communication
- multiprocessing.Queue
  - put()
  - get()
- multiprocessing.Pipe
  - parent, child = Pipe()
  - recv()
  - send()
- multiprocessing.Value/Array
  - shared memory
- multiprocessing.Lock()
  - acquire()
  - release() 

#### Process pool
- ```p = Pool(4)```
- ```p.apply_sync(func)```

#### threading module
- ```threading.Thread(target=func, args='test')```
- or inherits from Thread, calls ```super.__init()``` then override ```run()```
- ```thread.is_alive()```
- ```thread.is_getName()```
- ```thread.setDaemo()```

#### threading pool
- ```from concurrent.futures import ThreadPoolExecutor```
```python
# dummy
p = Pool(4)
r = p.map(func, args)
p.close()
p.join()

# executor
with ThreadPoolExecutor(3) as executor:
  executor.submit(func, [2,3,4,5]) # a list as a single parameter
  future = executor.map(func, [2,3,4,5]) # map each elem in the list
  future.result()
```

#### Miscellaneous
- str vs tuple
```python
a=('john')
type(a)
# <class 'str'>
b=('john', )
type(b)
# <class 'tuple'>
```
- flush buffer
  - sys.stdout.flush()
  - sys.stderr.flush()
- python disadvantages:
  - GIL lock: threads are running in a single process.