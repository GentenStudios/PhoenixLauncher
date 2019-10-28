from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout

page = BoxLayout(orientation='horizontal')

#-=- Start Info Pane Modules -=-
infoPane = BoxLayout(orientation='vertical', size_hint_max_x='300')

btn1 = Label(text='Module/ Game specific information here')
infoPane.add_widget(btn1)
btnLaunch = Button(text='launch', background_color=(0, 0, 50, 10), size_hint_max_y='100')
infoPane.add_widget(btnLaunch)

page.add_widget(infoPane)

#-=- Start Grid Modules -=-
grid = StackLayout()

for i in range(20):
    grid.add_widget(Button(text=str(i), width=200, size_hint=(None, 0.15)))

page.add_widget(grid)

#-=- End adding Widgets -=-

class Launcher(App):
    def build(self):
        return page

Launcher().run()