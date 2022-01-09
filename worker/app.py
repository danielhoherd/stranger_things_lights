from upside_down_display import UpsideDownDisplay


# LEDs are 0-indexed starting at your pi. A single 50 strand will have 0-49. Two will have 0-99.
def run_application():
    udd = UpsideDownDisplay()
    udd.set_letter_mappings(
        {
            "a": 22,
            "b": 23,
            "c": 24,
            "d": 25,
            "e": 26,
            "f": 27,
            "g": 28,
            "h": 29,
            "i": 30,
            "j": 31,
            "k": 32,
            "l": 33,
            "m": 34,
            "n": 35,
            "o": 36,
            "p": 37,
            "q": 38,
            "r": 39,
            "s": 40,
            "t": 41,
            "u": 42,
            "v": 43,
            "w": 44,
            "x": 45,
            "y": 48,
            "z": 49,
        }
    )
    udd.run()


if __name__ == "__main__":
    run_application()
