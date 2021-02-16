# Coffee Calc with Kivy Build

# Imports
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window


# File Built From
Builder.load_file('CoffeeCalc.kv')

class MyLayout(Widget):
    pass
    
class CoffeeCalcApp(App):
    def build(self):
        return MyLayout()

if __name__ == "__main__":
    CoffeeCalcApp().run()