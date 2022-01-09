import logging
import os
import random
import time

import board
import neopixel
import requests


class UpsideDownDisplay:
    """Displays messages on LEDs from the upside down"""

    def __init__(self, num_leds=100):
        self.num_leds = num_leds
        self.char_limit = 15
        self.data_pin = board.D18
        self.character_delay = 0.0  # how long to wait between characters
        self.character_time = 1.0  # how long to display characters for
        self.message_delay = 2.0  # how long to wait between messages
        self._setup_leds()

    def set_letter_mappings(self, letter_mappings):
        """Set letter to LED mappings for the display"""
        self.letter_mappings = letter_mappings

    def _setup_leds(self):
        """Set up the LEDs (ws2811 12v)"""
        self.leds = neopixel.NeoPixel(
            self.data_pin,
            self.num_leds,
            brightness=1,
            auto_write=False,
            pixel_order=neopixel.RGB,
        )
        self._twinkle_leds(25)

    def _get_server_host(self):
        """Fetch the hotsname of the server"""
        return os.getenv("SERVER_HOST", "server")

    def _get_server_key(self):
        """Fetch the API key for the server"""
        return os.getenv("SERVER_KEY", "")

    def _get_server_url(self):
        host = self._get_server_host()
        key = self._get_server_key()
        return "http://" + host + "/next?key=" + key

    def _get_latest_message(self):
        print("running _get_latest_message")
        try:
            server_url = self._get_server_url()
            print(f"fetching {server_url}")
            response = requests.get(self._get_server_url())
            if response.status_code != 200:
                print(f"{response.status_code=}")
                return
            if not response.text:
                print(f"{response.status_code=} with no text")
                return
            if len(response.text) > self.char_limit:
                print(
                    f"{response.status_code=} {response.text} exceeded allowed length of {self.char_limit}"
                )
                return
            print(response.text)
        except Exception as e:
            logging.error(e)
            return
        self._display_message(response.text)

    def _set_led(self, led_number, rgb=[255, 255, 255], update_now=True):
        """Sets a specific LED, defaults to white"""
        self.leds[led_number] = rgb
        if update_now:
            self.leds.show()

    def _clear_led(self, led_number, update_now=True):
        """Clears a specific LED"""
        self.leds[led_number] = [0, 0, 0]
        if update_now:
            self.leds.show()

    def _clear_all_leds(self):
        self.leds.fill((0, 0, 0))
        self.leds.show()

    def _get_colour_dict(self):
        """Returns a dict of standard colours"""
        return {
            "red": (255, 0, 0),
            "yellow": (255, 150, 0),
            "green": (0, 255, 0),
            "cyan": (0, 255, 255),
            "blue": (0, 0, 255),
            "purple": (180, 0, 255),
            "white": (255, 255, 255),
        }

    def _get_random_colour(self):
        """Returns a random colour from a predefined dict"""
        return random.choice(list(self._get_colour_dict().items()))[1]

    def _twinkle_leds(self, num_times=10, delay=0.1, num_choices=10, brightness=0.8):
        """Twinkle the LEDs to catch attention"""
        self.leds.fill([0, 0, 0])
        self.leds.show()
        for _ in range(0, num_times):
            choices = [
                random.randint(0, self.num_leds - 1) for x in range(0, num_choices)
            ]
            for i in choices:
                self.leds[i] = [int(x * brightness) for x in self._get_random_colour()]
            self.leds.show()
            time.sleep(delay)
            for i in choices:
                self.leds[i] = [0, 0, 0]
            self.leds.show()
            time.sleep(delay)

    def _display_character(self, character):
        """Flash a character on the LEDs"""
        print(f"running _display_character: {character}", flush=True)
        led_number = self.letter_mappings.get(str(character).lower())
        if not led_number:
            time.sleep(self.character_time)
            time.sleep(self.character_delay)
            return
        self._set_led(led_number, self._get_random_colour())
        time.sleep(self.character_time)
        self._clear_led(led_number)
        time.sleep(self.character_delay)

    def _display_message(self, message):
        """Displays the message on the LEDs"""
        print(f"running _display_message: {message}", flush=True)
        self._twinkle_leds()
        for character in message:
            self._display_character(character)

    def run(self):
        """Run the worker"""
        while True:
            self._get_latest_message()
            time.sleep(self.message_delay)
