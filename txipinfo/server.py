from klein import Klein

from twisted.web.static import File
from twisted.internet.defer import succeed
from twisted.web.template import XMLFile, Element, renderer
from twisted.python.filepath import FilePath

app = Klein()

# TODO: maybe use non-global state by encapsulating router handlers in class?
history = []


class IndexElement(Element):

    loader = XMLFile(FilePath('templates/index.html'))

    @renderer
    def message(self, request, tag):
        if request.method == 'POST':
            # TODO: return when we scheduled the task
            return tag('Message')
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
                whois=record[2],
                datetime=record[3]
            )


@app.route('/')
def index(request):
    return IndexElement()


@app.route('/history', methods=('GET', 'POST'))
def history_get(request):
    global history
    if request.method == 'POST':
        history = []
    return HistoryElement(history)

resource = app.resource
