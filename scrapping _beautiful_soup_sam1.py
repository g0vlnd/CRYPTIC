from bs4 import BeautifulSoup

# Open and parse the HTML file
with open('Palo Alto Networks Security Advisories.htm', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')

# Find the table in the HTML
table = soup.find('table', {'class': 'tbl salist wide'})  # Replace 'table' with the specific class or ID if needed


# Check if a table exists
if table:
    # Extract all rows
    rows = table.find_all('tr')
    for row in rows:
        # Extract columns in each row
        columns = row.find_all(['th', 'td'])  # Includes both headers and data cells
        # Print the text in each column
        print([col.text.strip() for col in columns])
else:
    print("No table found in the HTML file.")

