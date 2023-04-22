# Create your models here.
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.core.management import setup_environ
import entorno_app.settings as settings

# Setup Django environment
setup_environ(settings)

# Authenticate with Google Sheets API using service account credentials
scope = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "management-system-384110-178defacc653.json", scope
)
client = gspread.authorize(credentials)

# Open the Google Sheet by name
sheet_name = "Entorno-portal-Database"
sheet = client.open(sheet_name).sheet1

# Retrieve data from Django model and push to Google Sheet
from event_app.models import Event     #need to create database model
data = Event.objects.all().values_list()
sheet.clear()
sheet.insert_rows(data)
