from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

import psutil
import os

Builder.load_file('main.kv')

Window.size = (400, 600)

class myLayout(BoxLayout):
    slide_text = ObjectProperty(None)
    user_limit = 0  # Initialize user_limit
    sound = None

    def __init__(self, **kwargs):
        super(myLayout, self).__init__(**kwargs)
        self.sound = SoundLoader.load("mySound.mp3")
        if not self.sound:
            print("Error loading sound")

    def slide_it(self, *args):
        self.slide_text.text = str(int(args[1]))
        self.user_limit = int(args[1])  # Update user_limit

    def submit_button_pressed(self):
        battery_slider = self.ids.battery_slider
        user_limit = battery_slider.value
        print("User selected battery limit:", user_limit)
        self.user_limit = user_limit  # Update user_limit with the selected value

        battery = psutil.sensors_battery()
        plugged = battery.power_plugged
        plugged = "Plugged In" if plugged else "Not Plugged In"

        if battery.percent >= self.user_limit and plugged == "Plugged In":
            if self.sound:
                self.sound.play()

class BatteryPrototypeApp(App):
    def build(self):
        return myLayout()

if __name__ == '__main__':
    app = BatteryPrototypeApp()
    app.run()
