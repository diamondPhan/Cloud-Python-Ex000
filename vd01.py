import web
urls = (
'/', 'index'
)
class index:
    def GET(self):
        return "Welcome !!! Phan Ngoc Kim Cuong !"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
