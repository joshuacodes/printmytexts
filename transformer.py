
from lxml import etree

# Load XML and XSL files
xml = etree.parse('input.xml')
xsl = etree.parse('transform.xsl')

# Create a transformer
transform = etree.XSLT(xsl)

# Apply the transformation
result = transform(xml)

# Write the result to an HTML file
with open('output.html', 'w') as f:
    f.write(str(result))

