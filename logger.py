from eventtracking.tracker import Tracker
from eventtracking.backends.logger import LoggerBackend
import logging

logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

log = logging.getLogger("PythonTest")
log.setLevel(logging.INFO)

backend = LoggerBackend(name="PythonTest")
tracker = Tracker(backends={'PythonTest': backend})
tracker.enter_context('my context name', {'page': 'some specific page context'})
tracker.emit('navigation.request p2e', {'url': 'http://www.edx.org/some/path/1'})
