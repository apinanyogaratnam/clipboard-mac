import rumps
import pyperclip


class Clipboard:
    def __init__(self):
        self.app = rumps.App("Clipboard", "🍅")
        self.clipboard_contents = [pyperclip.paste()]
        self.timer = rumps.Timer(self.update_clipboard, 1)
        self.timer.start()
        self.app.menu = list(self.clipboard_contents)

        self.app.run()
        self.app.run()

    def update_clipboard(self, _):
        new_clipboard_content = pyperclip.paste()
        if new_clipboard_content not in self.clipboard_contents:
            # if len(self.clipboard_contents) == 10:
                # self.clipboard_contents.pop()
            self.clipboard_contents.insert(0, new_clipboard_content)
            self.app.menu = list(self.clipboard_contents)

if __name__ == '__main__':
    app = Clipboard()
    app.run()
