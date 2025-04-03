from json import dumps
from typing import Callable
import inspect

class Persistence:
    def write(msg: str):
        raise NotImplementedError("Not implemented")
    
class StdoutPersistence(Persistence):
    def write(self, msg):
        print(msg)

class FilePersistence(Persistence):
    def __init__(self, file_name: str):
        super().__init__()
        self._file_name = file_name

    def write(self, msg):
        with open(self._file_name, 'a') as d:
            d.write(msg + "\n")

stdout_persistence = StdoutPersistence()
file_persistence = FilePersistence('/tmp/python-035.log')

def logger(persistence: Persistence):
    def fn_wrapper(fn: Callable):
        signature = inspect.signature(fn)
        fn_name = fn.__name__
        print(f"Decorating {fn_name}")
        for param in signature.parameters.values():
            print(f" Arg: {param.name}, Type: {param.annotation}, Default: {param.default}")

        def args_wrapper(*args, **kwargs):
            fn_name = fn.__name__
            args_str = dumps(args)
            kwargs_str = dumps(kwargs)
            persistence.write(f"Calling function {fn_name} with args: {args_str} and kwargs: {kwargs_str}")
            res = fn(*args, **kwargs)
            res_json = dumps(res)
            persistence.write(f"Return function {fn_name}: {res_json}")
            return res
        return args_wrapper
    return fn_wrapper


@logger(stdout_persistence)
def calcular_suma(sum1: int, sum2: int):
    return sum1 + sum2

calcular_suma(1,2)
calcular_suma(1,3)

@logger(file_persistence)
def calcular_resta(sum1: int, sum2: int):
    return sum1 - sum2

calcular_resta(2,1)
calcular_resta(2,2)