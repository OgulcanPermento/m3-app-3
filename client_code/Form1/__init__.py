from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Get text from server and set it to the label
    self.text_label.text = anvil.server.call('get_text')

    # Any code you write here will run before the form opens.
