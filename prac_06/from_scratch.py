from kivy.app import App
from kivy.lang import Builder


class from_scratch(App):
    def build(self):
        self.title = "from_scratch"
        self.root = Builder.load_file('from_scratch.kv')
        return self.root


from_scratch().run()