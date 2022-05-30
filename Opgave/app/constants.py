import os

# Constants
PROJECT_DIR = os.path.dirname(os.path.realpath(__file__)) # Gets the current project folder
DATA_DIR = PROJECT_DIR + '/data/' # Directory of data files
SAVE_DIR = PROJECT_DIR + '/data/_savedata/' # Directory to save and load data
SITE_DIR = PROJECT_DIR + '/_site/' # Directory for the html files
TEMPLATE_DIR = PROJECT_DIR + '/_site/templates/' # Directory for the html templates
AMOUNT_GEBRUIKERS = 55000 # Amount of gebruikers to generate
AMOUNT_VELOS = 4200 # Amount of velos to generate
TIME_FORMAT = "%d/%m/%Y %H:%M:%S" # Format the date and time will be displayed in