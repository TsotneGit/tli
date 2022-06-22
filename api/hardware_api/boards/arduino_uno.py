arduino_uno = {
    "digital": tuple(x for x in range(14)),
    "analog": tuple(x for x in range(6)),
    "pwm": (3, 5, 6, 9, 10, 11),
    "use_ports": True,
    "disabled": (0, 1),  # Rx, Tx, Crystal
}
