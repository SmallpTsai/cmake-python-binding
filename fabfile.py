#
# 
#
from os.path import dirname, join
from fabric.api import lcd, run, task, env, local, settings
from fabric.colors import green, magenta, red, yellow
from fabric.context_managers import shell_env

@task
def build():
    local('docker build -t cmake-python-binding-demo .')

@task
def list_so_symbol():
    local('docker run -it --rm cmake-python-binding-demo nm /usr/local/lib/libdemo.so')

@task
def list_py_symbol():
    local('docker run -it --rm cmake-python-binding-demo ' + 
    ''' python3 -c 'import demo; print(dir(demo)); print(demo.hello_echo("python"))' ''')