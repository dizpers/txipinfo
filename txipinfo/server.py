from datetime import datetime

import ipaddress

from klein import Klein

from twisted.internet import utils
from twisted.internet.defer import inlineCallbacks, returnValue

from twisted.names import client

from twisted.python.filepath import FilePath

from twisted.web.template import XMLFile, Element, renderer

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S+0000'

app = Klein()

# TODO: maybe use non-global state by encapsulating router handlers in class?
# history - the list of records (tuples), each of them consists of 4 elements (ip, ptr, whois, datetime)
history = []


class IndexElement(Element):

    loader = XMLFile(FilePath('templates/index.html'))

    def __init__(self, message):
        super(IndexElement, self).__init__(self.loader)
        self._message = message

    @renderer
    def message(self, request, tag):
        if request.method == 'POST':
            return tag(self._message)
        return ''


class HistoryElement(Element):

    loader = XMLFile(FilePath('templates/history.html'))

    def __init__(self, history):
        super(HistoryElement, self).__init__(self.loader)
        self._history = history

    @renderer
    def record(self, request, tag):
        for record in self._history:
            yield tag.clone().fillSlots(
                ip=record[0],
                ptr=record[1],
                # please, feel free to use the following for pretty printing of whois data
                # whois=[tags.pre(part) for part in record[2].split('\n')],
                whois=record[2],
                datetime=record[3]
            )


@inlineCallbacks
def get_result_for(ip):
    reversed_name = '.'.join(reversed(ip.split('.'))) + '.in-addr.arpa'
    # you can simulate latency with
    # answers, _, _ = yield task.deferLater(reactor, 10.0, client.lookupPointer, reversed_name)
    # TODO: handle errors
    answers, _, _ = yield client.lookupPointer(reversed_name)
    ptr = str(answers[0].payload) if answers else ''
    # TODO: handle errors (no such command? we're on windows? anything else?)
    whois = yield utils.getProcessOutput('whois', (ip,))
    datetime_str = datetime.utcnow().strftime(DATETIME_FORMAT)
    returnValue((ip, ptr, whois, datetime_str))


@app.route('/')
def index(request):
    message = 'IP successfully queued for processing'
    if request.method == 'POST':
        try:
            ip = request.args.get('ip')[0]
            if not isinstance(ipaddress.ip_address(unicode(ip)), ipaddress.IPv4Address):
                raise ValueError
        except TypeError:
            message = 'No IP provided'
        except ValueError:
            message = 'IP is invalid'
        else:
            d = get_result_for(ip)
            d.addCallback(history.append)
    return IndexElement(message)


@app.route('/history', methods=('GET', 'POST'))
def history_get(request):
    global history
    if request.method == 'POST':
        history = []
    return HistoryElement(history)

resource = app.resource
