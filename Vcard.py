from bs4 import BeautifulSoup

# Load the HTML content
file_path = '/mnt/data/your_imported_contacts.html'
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find all contact entries
contacts = []
for table in soup.find_all('table'):
    rows = table.find_all('tr')
    name = None
    phone = None
    for row in rows:
        cells = row.find_all('td')
        if len(cells) == 2:
            if 'Contact name' in cells[0].text:
                name = cells[1].text.strip()
            elif 'Contact point' in cells[0].text and cells[1].text.startswith('+91'):
                phone = cells[1].text.strip()
    if name and phone:
        contacts.append((name, phone))

# Generate VCARD format
vcard_entries = []
for name, phone in contacts:
    vcard_entry = f"""BEGIN:VCARD
VERSION:3.0
N:;{name};;;
FN:{name}
TEL;type=Mobile:{phone}
END:VCARD"""
    vcard_entries.append(vcard_entry)

# Combine all VCARD entries
vcard_output = "\n".join(vcard_entries)
vcard_output



# Save the generated VCARD entries to a file
output_file_path = '/mnt/data/contacts_vcards.vcf'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(vcard_output)

output_file_path

