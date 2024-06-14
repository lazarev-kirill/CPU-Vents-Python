from typing import Union, List
from bits import Bit


def NAND(a: Union[int, bool, Bit], b: Union[int, bool, Bit]) -> Bit:
    out = a and b
    out = not (out)
    return Bit(out)


def NOT(a: Union[int, bool, Bit]) -> Bit:
    return NAND(a, a)


def AND(a: Union[int, bool, Bit], b: Union[int, bool, Bit]) -> Bit:
    return NOT(NAND(a, b))


def OR(a: Union[int, bool, Bit], b: Union[int, bool, Bit]) -> Bit:
    return NOT(AND(NOT(a), NOT(b)))


def XOR(a: Union[int, bool, Bit], b: Union[int, bool, Bit]) -> Bit:
    return OR(AND(a, NOT(b)), AND(NOT(a), b))


def MUX(
    a: Union[int, bool, Bit], b: Union[int, bool, Bit], sel: Union[int, bool, Bit]
) -> Bit:
    return AND(OR(a, XOR(b, NOT(sel))), OR(XOR(a, sel), b))


def DMUX(input: Union[int, bool, Bit], sel: Union[int, bool, Bit]) -> List[Bit]:
    return [
        Bit(XOR(NOT(input), NOT(AND(sel, input)))),
        Bit(
            AND(
                AND(
                    OR(input, XOR(input, NOT(sel))),
                    OR(XOR(input, sel), input),
                ),
                sel,
            )
        ),
    ]
