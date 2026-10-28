import requests
from bs4 import BeautifulSoup

def print_secret_message(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching the URL: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    if not table:
        print("Could not find a table in the provided Google Doc.")
        return

    rows = table.find_all('tr')
    if len(rows) < 2:
        print("The table doesn't contain enough data rows.")
        return

    headers = [cell.get_text(strip=True).lower() for cell in rows[0].find_all(['td', 'th'])]

    try:
        x_col = next(i for i, h in enumerate(headers) if 'x' in h)
        y_col = next(i for i, h in enumerate(headers) if 'y' in h)
        char_col = next(i for i, h in enumerate(headers) if 'char' in h)
    except StopIteration:
        print("Could not reliably identify X, Y, or Character columns in the table header.")
        return

    grid_data = {}
    max_x = 0
    max_y = 0

    for row in rows[1:]:
        cells = row.find_all(['td', 'th'])
        if len(cells) <= max(x_col, y_col, char_col):
            continue

        try:
            x = int(cells[x_col].get_text(strip=True))
            y = int(cells[y_col].get_text(strip=True))
            char = cells[char_col].get_text(strip=False)

            if len(char) > 1:
                char = char.strip()
            if not char:
                char = ' '

            grid_data[(x, y)] = char

            if x > max_x: max_x = x
            if y > max_y: max_y = y
        except ValueError:
            continue

    for y in range(max_y, -1, -1):
        line = []
        for x in range(max_x + 1):
            line.append(grid_data.get((x, y), ' '))
        print("".join(line))

target_url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
print_secret_message(target_url)
