# MSF
一个基于flask的微服务框架，方便简单的模型部署等。使得用户不需要关注于服务层面，专注在算法及业务逻辑中。

# 快速入门
## 安装
```
pip install msf
```
## 创建一个WSGI应用
```
from msf import Engine

path_conf = {}
engine = Engine(path_conf, name=__name__)
app = engine.app
```
或者你可以像flask一样使用它，来启动一个flask web服务器
```
from msf import Engine

path_conf = {}
engine = Engine(path_conf, name=__name__)
engine.run(host="0.0.0.0", port="41000")
```
## 添加一个路由
```
from msf import Engine

path_conf = {
    "hello_world":{
        "flow": ["hello_world_node"],
        "args: {
            "hello_world_node": {"text": "hello_world"}
        },
        "description": "describe what the route does"
    }
}
engine = Engine(path_conf, name=__name__)
engine.run(host="0.0.0.0", port="41000")
```
即可POST访问http://localhost:41000/hello_world  
  
path_conf中的key即为路由，flow中为node的有序排列，调用该路由会有序执行该node链表，args中的参数会在该路由中被传入对应函数，方便同一个函数在不同路由实现不同的逻辑
## 添加一个Node
添加路由前需要保证flow中的函数是存在并引用的（我们即将在接下来的一到两个版本推出显式自动加载的函数）  
```
from msf import node_register

@node_register()
def hello_world_node(**kwds):
    text = kwds.get("text")  # text来自于conf中args设置
    return text
```
## 在Node间传递中间结果
```
from msf import node_register, Engine

@node_register(name=hello_word_node)  # 可以通过name参数指定node的name，默认使用被装饰的函数名
def hello_world(**kwds):
    cxt = kwds.get("_context")
    text = cxt.get("text")  # text来自于conf中args设置
    return text

@node_register()
def load_text(**kwds):
    cxt = kwds.get("_context")
    text = kwds.get("text")
    cxt["text"] = text
    return

path_conf = {
    "hello_world":{
        "flow": ["load_text", "hello_world_node"],
        "args: {
            "load_text": {"text": "hello_world"}
        },
        "description": "describe what the route does"
    }
}
engine = Engine(path_conf, name=__name__)
app = engine.app
```
## 参数解析
框架内自带解析，以`_param`参数传递到函数，如果有重写解析的函数的需求，可以通过以下代码覆盖默认的解析方式（未来会优化默认的参数解析，并以更好的方式支持自定义解析）
```
from msf import Engine

def custom_parameter_parser(request):
    ...

path_conf = {}
engine = Engine(path_conf, name=__name__)
engine.param_parse = custom_parameter_parser
app = engine.app
```