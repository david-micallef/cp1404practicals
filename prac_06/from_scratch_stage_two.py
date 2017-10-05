from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

MILES_TO_KM = 1.61


class FromScratchStageTwo(App):
    def build(self):
        Window.size = (600, 200)
        self.title = "from_scratch_stage_two"
        self.root = Builder.load_file('from_scratch_stage_two.kv')
        return self.root

    def handle_convert(self):
        value = self.exception()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result) + "\n" + 'Oops, "m" in the screenshot is not a good abbreviation for "miles"'

    def handle_increment(self, value):
        increment_calculation = float(self.root.ids.miles_input.text) + value
        self.root.ids.miles_input.text = str(increment_calculation)
        self.handle_convert()

    def exception(self):
        try:
            value = float(self.root.ids.miles_input.text)
            return value
        except ValueError:
            return 0

FromScratchStageTwo().run()
