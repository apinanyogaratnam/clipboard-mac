import rumps
import pyperclip


class Clipboard:
    def __init__(self):
        self.app = rumps.App("Clipboard", "🍅")
        self.timer = rumps.Timer(self.update_clipboard, 0.01)
        self.timer.start()
        self.app.menu = []

        self.app.run()

    def update_clipboard(self, _):
        new_clipboard_content = pyperclip.paste()
        if new_clipboard_content not in self.app.menu:
            # if len(self.clipboard_contents) == 10:
                # self.clipboard_contents.pop()
            self.app.menu.update([new_clipboard_content])

if __name__ == '__main__':
    app = Clipboard()
    app.run()
