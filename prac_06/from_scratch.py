from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class from_scratch(App):
    def build(self):
        Window.size = (600, 200)
        self.title = "from_scratch"
        self.root = Builder.load_file('from_scratch.kv')
        return self.root

    def handle_convert(self, value):
        result = value * 1.61
        self.root.ids.output_label.text = str(result) + "\n" + 'Oops, "m" in the screenshot is not a good abbreviation for "miles"'


from_scratch().run()