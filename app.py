app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():

    return render_template('home.html')

@app.route('/social_media', methods=['GET'])
def social_media():

    return render_template('social_media.html')

@app.route('/info_facebook', methods=['GET'])
def info_facebook():

    return render_template('info_facebook.html')

@app.route('/assistants', methods=['GET'])
def assistants():

    return render_template('assistants.html')

@app.route('/info_alexa', methods=['GET'])
def info_alexa():

    return render_template('info_alexa.html')


@app.route('/cookies', methods=['GET'])
def cookies():

    return render_template('cookies.html')