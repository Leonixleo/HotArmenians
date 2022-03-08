import requests


VACANSIES_URL = 'https://api.hh.ru/vacancies'
PARAMETERS = {'period': 3, 'text': 'QA', 'area': '1'}


def get_links(url):
    return requests.get(url=url, params=PARAMETERS)


if __name__ == '__main__':
    items = get_links(VACANSIES_URL)
    links = []
    for v in items.json()['items']:
        if 'Senior' not in str(v):
            links.append(v['alternate_url'])

    with open('links.html', 'w') as f:
        f.writelines(['<html>', '<body>', '\n'])
        for l in links:
            link = f'<a href={l}>{l}</a><br>'
            f.write(link)
            f.write('<br>')
        f.writelines(['</body>', '</html>', '\n'])
