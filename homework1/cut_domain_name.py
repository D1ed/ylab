def domain_name(url):
    '''Cut domain name in URL
    :param url: URL
    :return: domain name
    '''
    count = -1
    if url[0:11] == 'https://www':
        url_start_cut = 12
    elif url[0:10] == 'http://www':
        url_start_cut = 11
    elif url[0:8] == 'https://':
        url_start_cut = 8
    elif url[0:7] == 'http://':
        url_start_cut = 7
    elif url[0:4] == 'www.':
        url_start_cut = 4
    else:
        url_start_cut = 0

    for i in url[url_start_cut:]:
        count = count + 1
        if i == '.':
            url_end_cut = url_start_cut + count
            return url[url_start_cut:url_end_cut]


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name('google.com') == "google"
