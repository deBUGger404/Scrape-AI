from bs4 import BeautifulSoup

def get_body_ele_without_sidebar(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.body
    sidebar_content = body_content.find('aside')
    if not sidebar_content:
        sidebar_content = body_content.find('div', {'class': 'sidebar'}) or soup.find('div', {'id': 'side-tab'})
    if sidebar_content:
        sidebar_content.decompose()
    return body_content