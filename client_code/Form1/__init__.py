from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Initialize the data grid with sample data
    sample_data = [
      {'id': 1, 'name': 'Item 1', 'description': 'Description 1'},
      {'id': 2, 'name': 'Item 2', 'description': 'Description 2'},
      {'id': 3, 'name': 'Item 3', 'description': 'Description 3'},
    ]
    
    # Set the data grid's data source
    self.data_grid.items = sample_data
    
    # Set up column configurations
    self.data_grid.columns = [
      {'id': 'id', 'title': 'ID', 'data_key': 'id'},
      {'id': 'name', 'title': 'Name', 'data_key': 'name'},
      {'id': 'description', 'title': 'Description', 'data_key': 'description'}
    ]

    # Any code you write here will run before the form opens.
