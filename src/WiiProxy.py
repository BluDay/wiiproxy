from . import _MultiWiiData

from serial    import Serial
from struct    import pack, unpack
from threading import Thread
from time      import sleep
from queue     import PriorityQueue

class WiiProxy(_MultiWiiData):
    """The main class of this module that handles everything.
    
    This class merely requires an open serial connection---at baudrate 115200---to be
    passed at instantiation. Everything else, like the commands, the thread, each data
    instance, gets created automatically.

    This module and this class only supports the legacy version of MSP (MultiWii Serial Protocol).
    """

    """ATmega328 microprocessor and most Arduino-based microcontrollers use Little-endian."""
    _ENDIANNESS = '<' # '>'

    """Same as above, but for serializing `int`s without `struct`."""
    _INT_BYTEORDER = 'little'

    """The message preamble format for `struct.pack` and `struct.unpack`."""
    _PREAMBLE_STRUCT_FORMAT = f'{ENDIANNESS}3b'

    """Same as above, but for the payload.

    The format consists of a `%s` specifier and is used for creating complete payload
    formats using either a dynamic or a non-dynamic data format for a specific command.
    """
    _PAYLOAD_STRUCT_FORMAT = f'{ENDIANNESS}2B'

    """
    A pre-packed preamble payload for incoming messages. All message preambles for
    incoming messages are the same, and do not need to be re-packed every single
    time at runtime.

    Example:

        \\x24\\x4d\\x3c

        $M< (ASCII)
    """
    _PREAMBLE_IN = pack(_PREAMBLE_STRUCT_FORMAT, '$M<')

    """
    Same as above, but with outgoing messages.

    Example:

        \\x24\\x4d\\x3e

        $M> (ASCII)
    """
    _PREAMBLE_OUT = pack(_PREAMBLE_STRUCT_FORMAT, '$M>')

    def __init__(self, serial: Serial) -> None:
        """Initializes an instance using the provided serial connection.
        
        The provided serial instance that presumably has been connected with a device
        with a baudrate of 115200.

        Parameters:
            serial (Serial): The serial connection instance.
        """
        super().__init__()

        self._is_active = False

        self._command_queue = PriorityQueue(100)

        self._serial = serial

        self._thread = Thread(target=self._handle_command_queue)

        self._write_delay = 0.005

    def __del__(self) -> None:
        """None: Stops the worker and the thread at destruction."""
        self._stop()

    @property
    def is_active(self) -> bool:
        """bool: Gets a value indicating whether the module is communicating to the flight controller."""
        return self._is_active

    @property
    def write_delay(self) -> float:
        """float: Gets the delay value for serial writes."""
        return self._write_delay

    @write_delay.setter
    def write_delay(self, value: float) -> None:
        """Sets the write delay value.

        Parameters:
            value (float): A floating-point value in seconds.
        """
        if not isinstance(value, float):
            raise TypeError

        if value < 0:
            raise ValueError
            
        self._write_delay = value
    
    @classmethod
    def __assemble_message(cls, format: str, data: tuple) -> bytes:
        """Assembles a complete serialized message with the provided format and data values.

        Parameters:
            format (str): The payload struct format.
            data (tuple): The data values.

        Returns:
            bytes: an array of bytes for the whole message.
        """
        payload = pack(format, *data)
            
        checksum = cls.__get_crc(payload).to_bytes(
            length=1,
            byteorder=cls._INT_BYTEORDER,
            signed=False
        )

        return cls._PREAMBLE_IN + payload + checksum

    @classmethod
    def __disassemble_message(cls, format: str, payload: bytes) -> tuple:
        """Disassembles a serialized outgoing message into a tuple of raw values.

        Parameters:
            format (str): A `struct` format for the full message.
            payload (bytes): The full message buffer.

        Returns:
            tuple: A tuple of raw and unevaluated values of integers.
        """
        return unpack(format, payload)
    
    @staticmethod
    def __get_crc(payload: bytes) -> int:
        """Calculates the a single byte checksum using CRC (cyclic redundancy check).

        Parameters:
            payload (bytes): A serialized payload buffer.

        Returns:
            int: The calculated CRC value for the provided payload.
        """
        checksum = 0

        for value in payload: checksum ^= value

        return checksum

    @staticmethod
    def get_message_direction(incoming: bool = True) -> str:
        """Gets an incoming or an outgoing message direction character.

        Parameters:
            incoming (bool): Decides which direction characters should be included.
        """
        return '<' if incoming else '>'

    @staticmethod
    def get_message_preamble() -> str:
        """Gets the message preamble string.

        Parameters:
            incoming (bool): Decides which direction characters should be included.

        Returns:
            str: A preamble format string with a direction char.
        """
        return '$M'

    def __handle_command_queue(self) -> None:
        """The thread worker method that performs the whole communication part.

        This worker method runs continously in a thread and handles everything
        from enqueuing commands and sending messages to the flight controller, to
        receiving messages and updating their corresponding data value instances.
        """
        while True:
            # TODO: Fill command queue with prioritized commands if empty.
            # TODO: Dequeue the most prioritized command from the queue.
            # TODO: Reset the input/output buffer.
            # TODO: Send message with empty data values to receive a response.
            # TODO: Read response message.
            # TODO: Update corresponding instance for command with new values if not null.
            # TODO: Indicate that the command has been processed.

            pass

    def __send_message(self, command: Command, data: tuple) -> None:
        """Creates a serialized message and sends it to the flight controller.

        Parameters:
            command (Command): The command to execute on the FC.
            data (tuple): A tuple of raw integer values to sent to the FC.
        """

        # TODO: Get size and format for command.
        # TODO: Create payload tuple.
        # TODO: Assembly message using the format and payload.
        # TODO: Write message to the serial port.
        # TODO: Sleep for `write_delay` seconds.

        pass

    def __read_message(self, command: Command) -> tuple:
        """Attempts to read a message of a specific command from the serial connection.

        Parameters:
            command (Command): The targeted command.

        Returns:
            tuple: An immutable list of data values for the command.
        """

        # TODO: Read preamble, code and data size.
        # TODO: Validate preamble.
        # TODO: Read data value bytes and checksum value.
        # TODO: Unpack the whole message.
        # TODO: Return the unpacked message.

        pass

    def __reset_input_output_buffer(self) -> None:
        """Resets both the input and output buffer of the serial connection."""
        self._serial.reset_input_buffer()
        self._serial.reset_output_buffer()

    def start(self) -> None:
        """Starts the worker thread and enables communication to the craft."""
        if self._is_active: return
        
        self._thread.start()
        
        self._is_active = True

    def stop(self) -> None:
        """"Stops the worker thread and disables all communication."""
        if not self._is_active: return

        self._thread.join()

        self._is_active = False
