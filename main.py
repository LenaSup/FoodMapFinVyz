from flask import Flask, render_template
from form import MainForm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurants import Rest


app = Flask(__name__)
app.config['SECRET_KEY'] = "foodmap_for_finvyz_231054"

engine = create_engine('sqlite:///db/data_base.db')
Session = sessionmaker(bind=engine)
session = Session()
restaurants = session.query(Rest).all()
session.commit()


@app.route('/')
def start_search():
    form = MainForm()
    return render_template('main_form.html',  title='', restaurants=restaurants, form=form)


@app.route('/<rest_name>', )
def show_menu(rest_name):
    form = MainForm()
    return render_template('main_form.html', title='', form=form)


def main():
    app.run(port=5000, host='127.0.0.1')


if __name__ == '__main__':
    main()