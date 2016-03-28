import re, subprocess

unprotected = ['/schedules']

with open('testfiles/views.py', 'r') as file:
    f = file.readlines()
urls = [re.findall('\'([^\']*)', line)[0] for line in f if(line.find('route') != -1)]


class TestUS327:

    def test_check_numen_enpoints_require_login(self):

        def checkurl(url):
            return subprocess.check_output(['curl','-ILs', 'https://numen.qa.ggoutfitters.com'+url]).split()[1]

        resps = [(checkurl(url),url) for url in urls if url not in unprotected]

        for resp in resps:
            print resp

        codes = [(int(code[0]) >300) for code in resps]
        assert False not in codes
