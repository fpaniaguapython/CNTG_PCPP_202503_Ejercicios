from __future__ import annotations
from typing import overload

@overload
def double(entrada: int) -> int: ...

@overload
def double(entrada: list) -> list[int]: ...

def double(entrada: int | list) -> int | list[int]:
    if isinstance(entrada, list):
        return [i * 2 for i in entrada]
    return entrada * 2

print(double(10))
print(double([10,20,30]))