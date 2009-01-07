import os
import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api import users

class MainPage(webapp.RequestHandler):
  def get(self):
    if users.get_current_user():
      login_url = users.create_logout_url(self.request.uri)
      login_url_linktext = 'Logout'
      user_name = users.get_current_user().nickname()
    else:
      login_url = users.create_login_url(self.request.uri)
      login_url_linktext = 'Login'
      user_name = ''

    template_values = {
      'login_url': login_url,
      'login_url_linktext': login_url_linktext,
      'user_name': user_name,       
    }

    path = os.path.join(os.path.dirname(__file__), 'adv.html')
    self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([('/', MainPage)], debug=True)
wsgiref.handlers.CGIHandler().run(application)
