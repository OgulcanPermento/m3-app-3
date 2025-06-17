from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
from datetime import datetime

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Get text from server and set it to the label
    server_text = anvil.server.call('get_text')
    self.text_label.text = server_text
    
    # Update the footer with current year
    current_year = datetime.now().year
    self.footer_label.text = f'© {current_year} Professional Dashboard'
    
    # Add hover effects to panels
    self.stats_panel.set_event_handler('mouse_enter', self.on_panel_hover)
    self.stats_panel.set_event_handler('mouse_leave', self.on_panel_leave)
    self.info_panel.set_event_handler('mouse_enter', self.on_panel_hover)
    self.info_panel.set_event_handler('mouse_leave', self.on_panel_leave)
    
  def on_panel_hover(self, **event_args):
    """This method is called when the mouse enters a panel"""
    panel = event_args['sender']
    panel.background = '#f5f5f5'
    panel.border = '1px solid #1a237e'
    
  def on_panel_leave(self, **event_args):
    """This method is called when the mouse leaves a panel"""
    panel = event_args['sender']
    panel.background = 'white'
    panel.border = '1px solid #e0e0e0'

    # Any code you write here will run before the form opens.
