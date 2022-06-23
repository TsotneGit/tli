import pyfirmata


class ArduinoUno:
    def __init__(self, port: str = "COM5") -> None:
        self.pins = [i for i in range(14)]
        self.board = pyfirmata.Arduino(port)
        self.it = pyfirmata.util.Iterator(self.board)

    def dpin_mode(self, pin: int, mode: str) -> None:
        """Sets pin mode"""
        try:
            if mode.lower() == "input":
                self.board.digital[pin].mode = pyfirmata.INPUT
            elif mode.lower() == "output":
                self.board.digital[pin].mode = pyfirmata.OUTPUT
        except IndexError:
            raise Exception("Invalid pin number")

    def digital_write(self, pin: int, value: bool) -> None:
        """Write a value to a digital pin."""
        try:
            self.board.digital[pin].write(value)
        except IndexError:
            raise Exception("Invalid pin number")

    def digital_read(self, pin: int):
        """Returns the value read from Digital Pin."""
        try:
            return self.board.digital[pin].read()
        except IndexError:
            raise Exception("Invalid pin number")

    def get_pin(self, pin):
        """
        Returns the pin object.
        Pin parameter must be in format like this: x:y:z,
        where x is either d or a standing for Digital and Analog,
        y is the pin number and z is the mode.

        """
        try:
            return self.board.get_pin(pin)
        except IndexError:
            raise Exception("Invalid pin number")

    def start_iterator(self):
        """Starts the iterator."""
        self.it.start()
