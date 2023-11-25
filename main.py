from flask import Flask, render_template
from form import MainForm


app = Flask(__name__)
app.config['SECRET_KEY'] = "foodmap_for_finvyz_231054"


@app.route('/')
def end_test():
    form = MainForm()
    return render_template('main_form.html',  title='', form=form)


def main():
    app.run(port=5000, host='127.0.0.1')


if __name__ == '__main__':
    main()