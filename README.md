# HTML-file-to-generate-VCARD

Here's an explanation of how the code processes the HTML file to generate VCARD entries:

---

### **1. File Reading**
```python
file_path = '/mnt/data/your_imported_contacts.html'
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()
```
- The code reads the uploaded HTML file containing the contact data and loads its content into memory as a string.

---

### **2. Parsing the HTML**
```python
soup = BeautifulSoup(html_content, 'html.parser')
```
- The `BeautifulSoup` library is used to parse the HTML content into a structured format, enabling easy traversal of elements.

---

### **3. Extracting Contacts**
```python
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
```

- **Step-by-Step Explanation:**
  1. **Find All Tables:** `soup.find_all('table')` identifies all the `<table>` tags in the HTML document.
  2. **Iterate Through Rows:** Each table contains rows (`<tr>`), which are processed one by one.
  3. **Extract Data:** Each row contains two `<td>` cells:
     - The first cell specifies whether the data is a "Contact name" or a "Contact point."
     - The second cell contains the actual name or phone number.
  4. **Filter Phone Numbers:** Only valid phone numbers starting with `+91` are considered.
  5. **Store Name and Phone Pair:** If both a name and a phone number are found, they are stored as a tuple in the `contacts` list.

---

### **4. Generating VCARD Entries**
```python
vcard_entries = []
for name, phone in contacts:
    vcard_entry = f"""BEGIN:VCARD
VERSION:3.0
N:;{name};;;
FN:{name}
TEL;type=Mobile:{phone}
END:VCARD"""
    vcard_entries.append(vcard_entry)
```

- **Step-by-Step Explanation:**
  1. For each contact, the `name` and `phone` are used to create a VCARD entry.
  2. The VCARD format follows this structure:
     - `N`: Name field (formatted for VCARD compatibility).
     - `FN`: Full Name (the readable name).
     - `TEL`: Phone number, with `type=Mobile` to indicate it is a mobile number.
  3. Each VCARD is appended to the `vcard_entries` list.

---

### **5. Combining and Saving**
```python
vcard_output = "\n".join(vcard_entries)
output_file_path = '/mnt/data/contacts_vcards.vcf'
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(vcard_output)
```

- **Combining:** All VCARD entries are combined into a single string, separated by newlines.
- **Saving:** The combined VCARD entries are saved to a `.vcf` file, which can be imported into contact management systems.

---

### **Output File**
The final file contains all contacts in the standard VCARD format, ready for use with address books or other applications that support `.vcf` files.

Would you like further clarification or help with additional functionality?
