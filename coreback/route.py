from coreback import Resource as src

def add(app):
    app.add_route('/test', src.dumy())
    app.add_route('/test/search', src.search())
