# cmake-python-binding

This project demo the very basic of How to create python library from C++ using `CMake` & `SWIG`

You can use it as a base/template to your own.

### Environment

See `Dockerfile` for detail required environment.

### build docker images

See `fabfile.py` for detail command

```
docker build -t cmake-python-binding-demo .
```

Native library is at `/usr/local/lib/libdemo.so`
Python package is at `/usr/local/lib/python3.6/dist-packages/demo`

### check the symbol in native library (.so)

```
docker run -it --rm cmake-python-binding-demo nm /usr/local/lib/libdemo.so
```

You should see below 2 symbols

```
0000000000000910 T _ZN4demo10hello_echoERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
0000000000000a00 T _ZN4demo28hello_echo_only_in_cplusplusERKNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEE
```

### check the symbol in python library

```
> docker run -it --rm cmake-python-binding-demo bash

container>  python3 -c 'import demo; print(dir(demo)); print(demo.hello_echo("python"))'
```

You should see below output

```
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_libdemo', 'hello_echo', 'libdemo', 'new_instancemethod']

Hello~python
```

