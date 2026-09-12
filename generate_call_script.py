import os, sys, reimport docxfrom docx import Documentfrom docx.shared import Inches, Pt, RGBColorfrom docx.enum.text import WD_ALIGN_PARAGRAPHfrom docx.oxml import OxmlElement, parse_xmlfrom docx.oxml.ns import nsdecls, qnimport win32com.clientimport shutil
sys.stdout.reconfigure(encoding='utf-8')
print('Ready to generate')
