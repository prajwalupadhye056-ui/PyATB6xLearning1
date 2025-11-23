class Browser:

    def make_http_request(self, url):
        print("Hi , Let's make HTTP request without auth", url)


    def make_http_request(self, url,auth="admin"):
        print("Hi , Lets make HTTP request with auth", url,auth)


obj_ref = Browser()
obj_ref.make_http_request("google.com")
