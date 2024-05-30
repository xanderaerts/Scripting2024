import requests
import json
from bs4 import BeautifulSoup

# all import for reportlab
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, ListItem, ListFlowable
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY