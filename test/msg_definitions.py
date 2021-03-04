from field import Field, Nibbles, Bytes, Bits, Bit, Byte

msg_fmts = {
    "GET_ADDR": {
        "id": Nibbles(4, value="x14"),
        "length": Nibbles(4, value=lambda id: id),
        "ptr": Bytes(4),
        "addr": Bits(11),
        "pad": Bits(3, value="b000"),
        "crc": Bytes(2, value=lambda ptr: ptr[:5]),
    },
    "FILL_KEY": {
        "id": Nibbles(4, value="x0015"),
        "ptr": Bytes(3),
        "addr": Bits(2),
        "pad": Bits(4, value="b0000"),
        "crc": Bytes(4, value=lambda pad:pad),
    },
    "WRITE_REGISTER_REQUEST": {
        "mid": Nibbles(4, value="x0016"),
        "length": Bytes(2, value="x0008"),
        "addr": Bytes(4),
        "data": Bytes(4),
    },
    "WRITE_REGISTER_RESPONSE": {
        "mid": Nibbles(4, value="x1014"),
        "length": Bytes(2, value="x0001"),
        "success": Byte(),
    },
    "READ_REGISTER_REQUEST": {
        "mid": Nibbles(4, value="x0015"),
        "length": Bytes(2, value="x0004"),
        "addr": Bytes(4),
    },
    "READ_REGISTER_RESPONSE": {
        "mid": Nibbles(4, value="x0014", fmt=Field.Format.Hex),
        "length": Bytes(2, value="x0008"),
        "addr": Bytes(4),
        "data": Bytes(4),
    },
}

register_defs = {
    "OUTPUTS": {"reset1": Bit(), "reset2": Bit(), "cautions": Byte(), "unused": Bits(22, value="x0000000")},
    "INPUTS": {
        "service_req": Bit(),
        "voltage_ready": Bit(),
        "exit_code": Bytes(2),
        "last_command_mid": Bits(2),
        "unused": Nibbles(3, value="x0"),
    },
}

circular_dep = {
    "CIRCULAR_DEP": {
        "id": Nibbles(4, value="x0015"),
        "len": Nibbles(2, value=lambda crc: crc),
        "ptr": Bytes(3),
        "addr": Bits(2),
        "pad": Bits(4, value="b0000"),
        "crc": Nibbles(2, value=lambda len: len),
    },
}
