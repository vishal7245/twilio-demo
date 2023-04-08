from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.twiml.voice_response import VoiceResponse, Say

app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    print(request.form)
    number = request.form['From']
    message_body = request.form['Body']

    resp = MessagingResponse()
    resp.message('Hello {}, you said: {}'.format(number, message_body))
    
    return str(resp)


@app.route("/voice", methods=['POST'])
def voice():
    response = VoiceResponse()
    say = Say('Hi', voice='Polly.Emma')
    say.break_(strength='x-weak', time='100ms')
    say.p("""Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you""")
    say.break_(strength='x-weak', time='50ms')
    say.p('Goodbye!')

    response.append(say)
    response.record()
    response.hangup()

    return str(response)


@app.route('/')
def index():
    return """<p>Hi this is Vishal!</p>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from waitress import serve
serve(app, host='0.0.0.0', port=8080)
