import xml.etree.ElementTree as ET
import fpdf
import json

tree = ET.parse('item.xml')
root = tree.getroot()
lst = []
for elem in root:
   for subelem in elem:
      print(subelem.text)
      lst.append(subelem.text)

pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)
for i in lst:
    pdf.write(5,i+'\n')
pdf.output("testings.pdf")
