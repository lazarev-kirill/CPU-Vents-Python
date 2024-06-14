from typing import Union, List

from bits import BitArray, Bit
from base_vents import (
    NAND,
    AND,
    OR,
    NOT,
    XOR,
    MUX,
    DMUX,
)


def NAND16(a: Union[list, BitArray], b: Union[list, BitArray]) -> BitArray:
    out = BitArray()
    for bit_a, bit_b in zip(a, b):
        value = NAND(bit_a, bit_b)
        out.append(value)
    return out


def AND16(a: Union[list, BitArray], b: Union[list, BitArray]) -> BitArray:
    out = BitArray()
    for bit_a, bit_b in zip(a, b):
        value = AND(bit_a, bit_b)
        out.append(value)
    return out


def OR16(a: Union[list, BitArray], b: Union[list, BitArray]) -> BitArray:
    out = BitArray()
    for bit_a, bit_b in zip(a, b):
        value = OR(bit_a, bit_b)
        out.append(value)
    return out


def NOT16(a: Union[list, BitArray]) -> BitArray:
    out = BitArray()
    for bit_a in a:
        value = NOT(bit_a)
        out.append(value)
    return out


def XOR16(a: Union[list, BitArray], b: Union[list, BitArray]) -> BitArray:
    out = BitArray()
    for bit_a, bit_b in zip(a, b):
        value = XOR(bit_a, bit_b)
        out.append(value)
    return out


def MUX16(
    a: Union[list, BitArray], b: Union[list, BitArray], sel: Union[int, bool, Bit]
) -> BitArray:
    out = BitArray()
    for bit_a, bit_b in zip(a, b):
        value = MUX(bit_a, bit_b, sel)
        out.append(value)
    return out


def MUX4_16(
    a: Union[list, BitArray],
    b: Union[list, BitArray],
    c: Union[list, BitArray],
    d: Union[list, BitArray],
    sel1: Union[int, bool, Bit],
    sel2: Union[int, bool, Bit],
) -> BitArray:
    out1 = MUX16(a, b, sel2)
    out2 = MUX16(c, d, sel2)
    out3 = MUX16(out1, out2, sel1)
    return out3


def MUX8_16(
    a: Union[list, BitArray],
    b: Union[list, BitArray],
    c: Union[list, BitArray],
    d: Union[list, BitArray],
    e: Union[list, BitArray],
    f: Union[list, BitArray],
    g: Union[list, BitArray],
    h: Union[list, BitArray],
    sel1: Union[int, bool, Bit],
    sel2: Union[int, bool, Bit],
    sel3: Union[int, bool, Bit],
) -> BitArray:
    out1 = MUX16(a, b, sel3)
    out2 = MUX16(c, d, sel3)
    out3 = MUX16(e, f, sel3)
    out4 = MUX16(g, h, sel3)
    out5 = MUX16(out1, out2, sel2)
    out6 = MUX16(out3, out4, sel2)
    out7 = MUX16(out5, out6, sel1)
    return out7


def DMUX4(
    input: Union[list, BitArray],
    sel1: Union[int, bool, Bit],
    sel2: Union[int, bool, Bit],
) -> List[Bit]:
    out000, out001 = DMUX(input, sel1)
    out010, out011 = DMUX(out000, sel2)
    out100, out101 = DMUX(out001, sel2)
    return [out010, out011, out100, out101]


def DMUX8(
    input: Union[list, BitArray],
    sel1: Union[int, bool, Bit],
    sel2: Union[int, bool, Bit],
    sel3: Union[int, bool, Bit],
) -> List[Bit]:
    out0000, out0001 = DMUX(input, sel1)
    out0010, out0011 = DMUX(out0000, sel2)
    out0100, out0101 = DMUX(out0001, sel2)
    out0110, out0111 = DMUX(out0010, sel3)
    out1000, out1001 = DMUX(out0011, sel3)
    out1010, out1011 = DMUX(out0100, sel3)
    out1100, out1101 = DMUX(out0101, sel3)
    return [
        out0110,
        out0111,
        out1000,
        out1001,
        out1010,
        out1011,
        out1100,
        out1101,
    ]
