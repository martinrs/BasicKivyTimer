from kivy.app import App

# Grafiske komponenter
from kivy.uix.boxlayout import BoxLayout

# Properties til interaktion mellem python og kv
from kivy.properties import StringProperty

# Kivys interne clock til timing og framerate
from kivy.clock import Clock

# Python standard biblioteker
import math

class TimerLayout(BoxLayout):
    # Tekst paa knappen. Bundet via .kv. Bliver aendret i update.
    timerText = StringProperty('Set time')
    buttonText = StringProperty('Start timer')
    running = False        # Nedtaellingen koerer hvis sand
    expired = False
    startTime = 3          # Antal sekunder timeren starter på
    timeLeft = startTime   # Antal sekunder tilbage i nedtaellingen

    # Skifter running til modsatte boolske vaerdi
    def toggle(self):
        if self.expired and not self.running:
            self.timeLeft = self.startTime
            self.expired = False
        else:
            self.running = not self.running

    # Taeller ned hvis running. Opdaterer buttonText ved hvert kald
    def update(self, dt):
        # Opdater tid tilbage, hvis timer kører.
        if self.running:
            self.timeLeft = self.timeLeft - dt
        # Stop tiden, hvis den er nået 0 (eller mindre)
        if self.timeLeft <= 0 and self.running:
            self.toggle()
            self.expired = True

        # Opdater teksten på skærmen via StringProperty
        self.timerText = str(math.ceil(self.timeLeft))

        # Sæt teksten på knappen afhængig af timerens tilstand
        if self.running and not self.expired:
            self.buttonText = 'Stop'
        elif not self.running and not self.expired:
            self.buttonText = 'Start'
        else:
            self.buttonText = 'Reset'

class BasicTimerApp(App):

    def build(self):
        # Initialiser knappen
        layout = TimerLayout()

        # Bed Kivy om at kalde update() 30 gange pr. sekund
        Clock.schedule_interval(layout.update, 1.0/30.0)

        return layout

# Kør appen
if __name__ in ('__main__', '__android__'):
    BasicTimerApp().run()
