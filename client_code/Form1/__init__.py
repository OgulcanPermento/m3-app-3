from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
from datetime import datetime

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Get text from server and set it to the label
    self.text_label.text = anvil.server.call('get_text')
    
    # Update the footer with current year
    current_year = datetime.now().year
    self.footer_label.text = f'© {current_year} My App'
    
    # Add some hover effects
    self.main_content.set_event_handler('mouse_enter', self.on_main_content_hover)
    self.main_content.set_event_handler('mouse_leave', self.on_main_content_leave)
    
  def on_main_content_hover(self, **event_args):
    """This method is called when the mouse enters the main content area"""
    self.main_content.background = '#e8eaf6'  # Lighter shade of the background
    
  def on_main_content_leave(self, **event_args):
    """This method is called when the mouse leaves the main content area"""
    self.main_content.background = '#f5f6fa'  # Original background color

    # Any code you write here will run before the form opens.
