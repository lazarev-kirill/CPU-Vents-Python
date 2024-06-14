class Bit:
    def __init__(self, value) -> None:
        self.value = int(value)

    def __bool__(self):
        return bool(self.value)

    def __int__(self) -> int:
        return self.value

    def __repr__(self) -> str:
        return f"{self.value}"


class BitArray:
    def __init__(self, values: list = None) -> None:
        if values is not None:
            self.values = [Bit(bit) for bit in values]
        else:
            self.values = [0] * 16

    def __getitem__(self, index):
        return self.values[index]

    def __repr__(self):
        return f"{self.values}"

    def __str__(self):
        return f"{self.values}"

    def append(self, value: Bit):
        self.values.append(value)
