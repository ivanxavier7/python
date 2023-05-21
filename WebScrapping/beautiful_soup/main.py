from bs4 import BeautifulSoup
import requests
import time


if __name__ == '__main__':
    root = 'https://subslikescript.com'
    website = f'{root}/movies'
    html = requests.get(website).text
    soup = BeautifulSoup(html, 'lxml')

    pagination = soup.find('ul', class_='pagination')
    pages = pagination.find_all('li', class_='page-item')
    total_pages = int(pages[-2].text)

    for page in range(1, total_pages+1)[:10]:   # First three pages
        endpoint = f'{website}?page={page}'
        html = requests.get(endpoint).text
        soup = BeautifulSoup(html, 'lxml')

        element = soup.find('article', class_="main-article")

        print('--------------------')
        print(page)
        print('--------------------')

        anchors = []  # List to String -> ' \n'.join(str(a) for a in anchors)

        # Get all Anchors
        for url in element.find_all('a', href=True):
            anchors.append(url['href'])

        for anchor in anchors:
            try:
                html = requests.get(f'{root}/{anchor}').text
                soup = BeautifulSoup(html, 'lxml')

                element = soup.find('article', class_="main-article")

                title = element.find('h1').get_text().replace('/', '-').replace(':', ' ').replace('_',' ').replace('.', '')
                transcript = element.find('div', class_='full-script').get_text(strip=True, separator=' ')

                try:
                    print('Writing: ' + title)
                    with open(f"extracted_data/{title}.txt", 'w', encoding='utf8') as file:
                        time.sleep(0.2)
                        file.write(transcript)
                        file.close()
                except:
                    print("Something went wrong with the file: " + f"extracted_data/{title.replace('/', '-')}.txt")
            except:
                print("Something went wrong with the Anchor: " + anchor)