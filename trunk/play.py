#!/usr/bin/env python
#
# Json interface to the adventure API.

from datetime import datetime

import pickle
import sys
import wsgiref.handlers

from adv5.python.stepper import Stepper
from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp

class LogEntry:
  def __init__(self, input, output):
    self.input = input
    self.output = output
    
  def json(self):
    output_lines = self.output.replace("\"", "\\\"");
    output_lines = ["\"" + x + "\"" for x in output_lines.split("\n")]
    input = ""
    if self.input:
      input = ">&nbsp;" + self.input.replace("\"", "\\\"");
    return "\"" + input + "\", " + ", ".join(output_lines)


MAX_LOG_SIZE=100

class State(db.Model):
  username = db.StringProperty()   # Name of the user
  saved_state = db.BlobProperty()  # Saved state from stepper
  log = db.BlobProperty()          # pickled Array of LogEntry
  save_name = db.StringProperty()  # Name under which the game is saved
  # Location of the explorer in the cave
  location = db.StringProperty(default="nowhere")
  # Date and time of last move
  last_played = db.DateTimeProperty(auto_now=True, default=datetime.now())
  score = db.IntegerProperty(default=0)

  def newForUser(username):
    state = State()
    state.username = username
    state.saved_state = None
    state.stppr = Stepper(None)
    state.log_entries = [LogEntry("", state.stppr.get_output())]
    state.save_name = 'save'
    return state
  newForUser = staticmethod(newForUser)

  def loadForUser(username, save_name):
    query = State.gql("WHERE username = :1", username)
    states = query.fetch(2)
    found_state = None
    for state in states:
      if state.save_name == save_name:
        state.stppr = Stepper(state.saved_state)
        state.log_entries = pickle.loads(state.log)
        return state
    return None
  loadForUser = staticmethod(loadForUser)

  def saveForUser(self):
    self.location = self.stppr.get_location()
    self.saved_state = self.stppr.get_saved_state()
    if len(self.log_entries) > MAX_LOG_SIZE:
      self.log_entries = self.log_entries[-MAX_LOG_SIZE:]
    self.log = pickle.dumps(self.log_entries)
    self.put()

  def copyFrom(self, other_state):
    self.username = other_state.username
    self.saved_state = other_state.saved_state
    self.log = other_state.log

  def saveToBackup(self):
    backup_state = State.loadForUser(self.username, 'backup')
    if not backup_state:
      backup_state = State()
    backup_state.copyFrom(self)
    backup_state.save_name = 'backup'
    backup_state.put()

  def restoreFromBackup(self):
    backup_state = State.loadForUser(self.username, 'backup')
    if not backup_state:
      return False
    self.copyFrom(backup_state)
    self.put()
    self.log_entries = pickle.loads(self.log)

  def deleteForUser(username):
    query = State.gql("WHERE username = :1", username)
    states = query.fetch(2)
    for state in states:
      if state.save_name == 'save':
        state.delete()
  deleteForUser = staticmethod(deleteForUser)

  def play(self, input):
    self.stppr.step(input)
    self.last_log_entry = LogEntry(input, self.stppr.get_output())
    self.log_entries.append(self.last_log_entry)

  def lastLogEntry(self):
    return self.last_log_entry

  def allLogEntries(self):
    return self.log_entries


class JsonStart(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'

    user = users.GetCurrentUser()
    if not user:
      self.response.out.write('{"full":0, "lines":["You are not logged in.", ""]}')
      return

    username = user.nickname()

    if self.request.get('new'):
      State.deleteForUser(username)

    state = State.loadForUser(username, 'save')
    if not state:
      state = State.newForUser(username)
      state.saveForUser()

    entries = state.allLogEntries()
    json_entries = [x.json() for x in entries]
    joined = ','.join(json_entries)
    self.response.out.write('{ full:1 , lines:[%s] }' % joined)


class JsonPlay(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'

    user = users.GetCurrentUser()
    if not user:
      self.response.out.write('{"full":0, "lines":["You are not logged in.", ""]}')
      return

    username = user.nickname()

    state = State.loadForUser(username, 'save')
    if not state:
      self.response.out.write('{"full":0, "lines":["No game in progress.", ""]}')
      return

    state.play(self.request.get('input').strip())
    state.saveForUser()

    self.response.out.write(
        '{ full:0 , lines:[%s] }' % state.last_log_entry.json())


class JsonBackup(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'

    user = users.GetCurrentUser()
    if not user:
      self.response.out.write('{"full":0, "lines":["You are not logged in.", ""]}')
      return

    username = user.nickname()

    state = State.loadForUser(username, 'save')
    if not state:
      self.response.out.write('{"full":0, "lines":["No game in progress.", ""]}')
      return

    state.saveToBackup()
    self.response.out.write('{ full:0 , lines:["Game saved.", ""] }')


class JsonRestore(webapp.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'

    user = users.GetCurrentUser()
    if not user:
      self.response.out.write('{"full":0, "lines":["You are not logged in.", ""]}')
      return

    username = user.nickname()

    state = State.loadForUser(username, 'save')
    if not state:
      self.response.out.write('{"full":0, "lines":["No game in progress.", ""]}')
      return

    state.restoreFromBackup()

    entries = state.allLogEntries()
    json_entries = [x.json() for x in entries]
    joined = ','.join(json_entries)
    self.response.out.write('{ full:1 , lines:[%s, "Game restored.", ""] }' % joined)


application = webapp.WSGIApplication([('/play/step', JsonPlay),
                                      ('/play/start', JsonStart),
                                      ('/play/backup', JsonBackup),
                                      ('/play/restore', JsonRestore),],
                                     debug=True)
wsgiref.handlers.CGIHandler().run(application)
