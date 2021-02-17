import requests 
import sys
import time

def waybackurls(host):
    # fetch resault from waybackarchive
    waybackarchive = 'http://web.archive.org/cdx/search/cdx?url=%s/*&fl=original' %host
    returned_urls = requests.get(waybackarchive).text
    if returned_urls:
        filename = '%s-all-urls' %host
        with open(filename, 'w') as file:
            file.write(str(returned_urls))
            file.close()
            print('[*] File saved to %s' %filename)
        request_urls(returned_urls, host)
    else:
        print('Nothing found')
    return

def request_urls(urls, host):
    filename = '%s-exist-urls' %host
    urls = str(urls).split('\n')
    for line in urls:
        if line != '':
            code = requests.get(line)
            if code.status_code == 200:
                print('Found %s with status code 200 ...' %line)
                with open(filename, 'a') as file:
                    file.write(line + '\n')
                    file.close()
            time.sleep(0.5)
    print('[*] File saved to %s' %filename)

    return


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 2:
        print('Usage:\n\tpython3 waybackurls.py <url> ')
        sys.exit()

    waybackurls(sys.argv[1])
