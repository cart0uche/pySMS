import android

from bottle import run, post, error, request, get

@post('/send_sms')
def send_sms():
	number  = request.forms.get('number')
	message = request.forms.get('message')
	print number + ' : ' + message
	droid.smsSend(number,message)

@get('/send_sms')
def fill_sms():
	return '''
	 <form action="/send_sms" method="post">
			Number : <input name="number" type="text" />
			Message: <input name="message" type="text" />
			<input value="Send" type="submit" />
		</form>
	'''

@error(404)
def error404(error):
	return 'Nothing here sorry'

droid = android.Android()
run(host='192.168.1.41', port=8080, reloader=True)
