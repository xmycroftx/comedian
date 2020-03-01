from user_agents import parse
import re

chrome_minimum_ver = 79
firefox_minimum_ver = 73


class Browser:
    def __init__(self,request):
        self.useragent = request.headers.get('User-Agent')
        self.user_agent = parse(self.useragent)
        self.trusted = False
    def load_uas(self):
        f = open("requirements.txt", "r")
        return f.read()
    def get_ua(self):
    	return self.useragent
    def get_os(self):
        return self.user_agent.os.family
    def get_browser(self):
        return self.user_agent.browser.family
    def get_version(self):
        return self.user_agent.browser.version_string
    
def browser_check(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    b = Browser(request)
    if request.args and 'message' in request.args:
        return request.args.get('message')
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        if re.match("Chrome",b.get_browser()):
            return version_check(chrome_minimum_ver,b)
            
        if re.match("Firefox",b.get_browser()):
            return version_check(firefox_minimum_ver,b)
        return b.get_browser()

def version_check(minimum_version,b):
        bvers=b.get_version().split('.')
        if int(bvers[0]) < minimum_version:
            return "Out of Date: " + b.get_browser() + " " + b.get_version()
        else:
            return "Up to Date: " + b.get_browser() + " " + b.get_version()