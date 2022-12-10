import rumps
import pyperclip


class Clipboard:
    def __init__(self):
        self.app = rumps.App("Clipboard", "📎")
        self.timer = rumps.Timer(self.update_clipboard, 0.01)
        self.timer.start()
        self.app.menu = [
            rumps.MenuItem("Clear", callback=self.clear),
            rumps.MenuItem("Quit", callback=rumps.quit_application),
            None,
        ]
        self.app.quit_button = None

    def update_clipboard(self, _):
        new_clipboard_content = pyperclip.paste()
        if new_clipboard_content not in self.app.menu:
            new_menu_item = rumps.MenuItem(new_clipboard_content, callback=self.copy)
            # if len(self.clipboard_contents) == 10:
                # self.clipboard_contents.pop()
            self.app.menu.update(new_menu_item)

    def copy(self, sender):
        pyperclip.copy(sender.title)

    def run(self):
        self.app.run()

    def clear(self, sender):
        self.app.menu.clear()
        self.app.menu.update([
            rumps.MenuItem("Clear", callback=self.clear),
            rumps.MenuItem("Quit", callback=rumps.quit_application),
            None,
        ])

    def quit(self, sender):
        self.app.quit()

if __name__ == '__main__':
    app = Clipboard()
    app.run()
