import rumps


class Clipboard:
    def __init__(self):
        self.app = rumps.App("Clipboard", "🍅")
    def run(self):
        self.app.run()

if __name__ == '__main__':
    app = Clipboard()
    app.run()
