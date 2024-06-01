import requests
import json
from bs4 import BeautifulSoup
import cairosvg
import os

# all import for reportlab
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, ListItem, ListFlowable
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib import colors


# styles for report lab
styles = getSampleStyleSheet()
title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=26, alignment=1)
text_style = ParagraphStyle('BodyText', parent=styles['BodyText'], fontName='Helvetica', fontSize=12, leading=14, alignment=TA_JUSTIFY)
bold_style = ParagraphStyle('Bold', parent=styles['BodyText'], fontName='Helvetica-Bold', fontSize=16, leading=14)
bold_style2 = ParagraphStyle('Bold', parent=styles['BodyText'], fontName='Helvetica-Bold', fontSize=20, leading=14)
error_style = ParagraphStyle('Bold', parent=styles['BodyText'], fontName='Helvetica-Bold', fontSize=16, leading=14,textColor = colors.red)
error_style2 = ParagraphStyle('Bold', parent=styles['BodyText'], fontName='Helvetica-Bold', fontSize=12, leading=14,textColor = colors.red)
