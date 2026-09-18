#!/usr/bin/python
# -*- coding: UTF-8 -*-

import argparse
import asyncio

from pyppeteer import launch

import re
from pyppeteer.errors import PageError, TimeoutError, NetworkError


async def save_pdf(name, url):
    browser = await launch(headless=True, args=['--no-sandbox'])
    try:
        page = await browser.newPage()
        await page.goto(url, {'waitUntil': 'networkidle2'})
        await page.pdf({
            'path': name,
            'format': 'A4',
            'printBackground': True,
        })
    finally:
        await browser.close()


def main():
    parser = argparse.ArgumentParser(description='Page Downloader as PDF')
    parser.add_argument('--link', '-l', action='store', dest='link',
                        required=True, help='Inform the link to download.')
    parser.add_argument('--name', '-n', action='store', dest='name',
                        required=False, help='Inform the name to save.')

    arguments = parser.parse_args()

    url = arguments.link

    if not arguments.name:
        name = re.sub(r'^\w+://', '', url.lower())
        name = name.replace('/', '-')
    else:
        name = arguments.name

    if not name.endswith('.pdf'):
        name = name + '.pdf'

    print(f'Name of the file: {name}')

    try:
        asyncio.run(save_pdf(name, url))
    except PageError:
        print('URL could not be resolved.')
    except TimeoutError:
        print('Timeout.')
    except NetworkError:
        print('No access to the network.')


if __name__ == '__main__':
    main()