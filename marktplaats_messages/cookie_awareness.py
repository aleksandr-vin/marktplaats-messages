# Misc cookie awareness methods



def sniff_clipboard():
    """
    Sniff Cookies from the clipboard. If you copy request from your browser's Network tab (in Developer Tools) as a Curl, then Cookie header will be there.
    """
    from tkinter import Tk
    t = Tk()
    text = t.clipboard_get()
    t.destroy()
    import re
    pattern = r"'Cookie: .*?'"
    match = re.search(pattern, text)
    if match:
        result = match.group(0)[1:][:-1]
        return result
    else:
        return None
    

def store_in(cookie_str, domain):
    """
    Store cookies from 'Cookie: ...' string into a cookie jar file. Provide domain.
    """
    import tempfile

    if cookie_str == None:
        return
    
    with tempfile.NamedTemporaryFile('w+', delete=True) as temp_file:
        import http.cookiejar
        jar = http.cookiejar.LWPCookieJar(temp_file.name)

        for cookie in cookie_str.split(": ")[1].split(";"):
            cookie_name, cookie_value = cookie.split("=", 1)
            cookie = http.cookiejar.Cookie(
                version=0,
                name=cookie_name,
                value=cookie_value,
                port=None,
                port_specified=False,
                domain=domain,
                domain_specified=True,
                domain_initial_dot=False,
                path="/",
                path_specified=True,
                secure=False,
                expires=None,
                discard=True,
                comment=None,
                comment_url=None,
                rest={"HttpOnly": None},
                rfc2109=False
            )
            jar.set_cookie(cookie)

        jar.save(ignore_discard=True)
        temp_file.seek(0)
        print(temp_file.read())


def store_in_env(cookie_str):
    print('COOKIE="' + cookie_str.split(": ")[1] + '"')


if __name__ == "__main__":
    import os
    import sys
    x = sniff_clipboard()
    store_in_env(x)
    #store_in(x, os.environ.get('DOMAIN'))