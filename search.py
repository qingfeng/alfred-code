from __future__ import print_function

import sys
import alfred
import requests


CODE_URL = 'http://code.dapps.douban.com'

def main():
    query = alfred.args()
    if query:
        query = query[0]
    r = requests.get('%s/api/autocomplete_repos?q=%s' % (CODE_URL, query))
    results = r.json()
    items = []
    for repo in results.get('repos', []):
        items.append(alfred.Item({
                u'valid': u'yes',
                u'arg': "%s%s" % (CODE_URL, repo['url']),
                u'uid': u'repo'
                },
                u'%s' % repo['name'],
                u'Hit ENTER to the project',
                u'icon.png'
        ))
    xml = alfred.xml(items, maxresults=10)
    print(xml)
    return 0


if __name__ == '__main__':
    sys.exit(main())