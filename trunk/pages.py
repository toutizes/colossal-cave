#!/usr/bin/env python
#
# Main handler.
# Redirects to login page if needed.
# Otherwise expands the template for the selected page.

import os
import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from google.appengine.api import users

class CommonPage(webapp.RequestHandler):
  def CommonValues(self):
    return {
      'login_url': users.create_logout_url(self.request.uri),
      'login_url_linktext': 'Logout',
      'user_name': users.get_current_user().nickname(),
    }

  def get(self):
    if not users.get_current_user():
      self.redirect(users.create_login_url(self.request.uri))
    else:
      values = self.CommonValues()
      path = os.path.join(os.path.dirname(__file__), self.page)
      self.response.out.write(template.render(path, values))


class CreditsPage(CommonPage):
  page = 'pages/credits.html'
    
class GamePage(CommonPage):
  page = 'pages/game.html'

class ScorePage(CommonPage):
  page = 'pages/score.html'
    
class TestPage(CommonPage):
  page = 'pages/test.html'
    

application = \
  webapp.WSGIApplication([('/game', GamePage),
                          ('/credits', CreditsPage),
                          ('/score', ScorePage),
                          ('/test', TestPage),
                          ('/', CreditsPage)],
                         debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
