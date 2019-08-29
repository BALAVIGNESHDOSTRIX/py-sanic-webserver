from sanic import Blueprint, Sanic
from sanic.response import file, json

app = Sanic(__name__)
dostrix1 = Blueprint('dostrixmain', url_prefix='/dostrixmain')
dostrix2 = Blueprint('dostrixfun', url_prefix='/dostrixfun')

@dostrix1.route('/melta')
async def foo(request):
    return json({'msg': 'Welcome to Dostrix Prime'})

@dostrix2.route('/fenoda')
async def foo2(request):
    return json({'msg': 'Make the pignus level more'})


app.blueprint(dostrix1)
app.blueprint(dostrix2)

app.run(host="0.0.0.0", port=8000, debug=True)
