State: /game page playing.  Now do restart/load/store of games.


Game engine => adv5/  The main driver is ad5/python/stepper.py.

TTY emulator => js/tty.js

App logic
 - Json play server: play.py, called from javascript in the html pages.
 - Dispatcher: pages.py, takes care of login, etc.  Defines mapping for
               the application pages: game, help, load/save, score, community.

Play logic
 - Game state is kept in the db.  

 - When receiving TTY input: load the state from the db, pass the
   input to the game engine, catpure the output, save the state to the
   db.

 - If the state does not exist a new state is created.

 - We could add special known commands, such as "restart" to abandon
   the game.  We could also have these accessible as buttons.

HTML templates => html/...

HTML Layout
  - All pages have the adventure header/footer (include them within the
    templating system?) which provides navigation to the various pages.

