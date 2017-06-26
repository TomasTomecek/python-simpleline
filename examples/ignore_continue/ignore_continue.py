#!/bin/python3

from simpleline.base import App
from simpleline.render import INPUT_PROCESSED
from simpleline.render.prompt import Prompt
from simpleline.event_loop.signals import RenderScreenSignal
from simpleline.render.ui_screen import UIScreen
from simpleline.render.widgets import TextWidget, CenterWidget


class MyApp(App):
    def application_quit_cb(self):
        print("Application is closing. Bye!")


class InfiniteScreen(UIScreen):
    title = u"You need to use 'q' to quit"

    def __init__(self):
        super().__init__()
        self.continue_count = 0

    def refresh(self, args=None):
        """Print text to user with number of continue clicked"""
        super().refresh(args)
        text = TextWidget("You pressed {} times on continue".format(self.continue_count))
        self._window += [CenterWidget(text), ""]
        return True

    def input(self, args, key):
        """Catch 'c' keys for continue and increase counter"""
        if key == Prompt.CONTINUE:
            self.continue_count += 1
            self.emit_draw_signal()
            return INPUT_PROCESSED

        return key


if __name__ == "__main__":
    App.initialize("Hello World")
    s = InfiniteScreen()
    App.renderer().schedule_screen(s)
    App.run()
