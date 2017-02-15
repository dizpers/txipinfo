from klein import Klein

app = Klein()


@app.route('/')
def index(request):
    return 'Index'

@app.route('/history')
def history(request):
    return 'History'

resource = app.resource