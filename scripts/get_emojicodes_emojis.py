from bs4 import BeautifulSoup
import requests


def start_requests():
    urls = [
        'http://emoji.codes/family?c=people',
        'http://emoji.codes/family?c=nature',
        'http://emoji.codes/family?c=food',
        'http://emoji.codes/family?c=activity',
        'http://emoji.codes/family?c=travel',
        'http://emoji.codes/family?c=objects',
        'http://emoji.codes/family?c=symbols',
        'http://emoji.codes/family?c=flags',
        'http://emoji.codes/family?c=diversity'
    ]

    print('emojis=(')
    for url in urls:
        req = requests.get(url)
        html = BeautifulSoup(req.text, 'html.parser')
        parse(html, url.split('=')[1])
    print(')')


def parse(html, title):
    emoji_list = html.find(id='emoji-list')
    print('\n\t# category: ' + title + '\n')

    for emoji in emoji_list.find_all('tr'):
        code = u'\\U' + emoji.get('id').replace('-', '\\U')
        shortcode = emoji.select_one('span[class*=shortcode]').text

        if title == 'diversity':
            if 'tone1' in shortcode:
                print(
                    '\t[\"' + shortcode.replace('_tone1', '') +
                    '\"]=\"\\' + (code.split('\\'))[1].split('\\')[0] + '\"'
                )
        print('\t[\"' + shortcode + '\"]=\"' + code + '\"')


if __name__ == '__main__':
    start_requests()
