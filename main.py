from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurants import Rest
from dish import Dish


app = Flask(__name__)
app.config['SECRET_KEY'] = "foodmap_for_finvyz_231054"

engine = create_engine('sqlite:///db/data_base.db')
Session = sessionmaker(bind=engine)
session = Session()
restaurants = session.query(Rest).all()
session.commit()


@app.route('/')
def start_search():
    return render_template('main_form.html',
                           title='', objects=restaurants, restaurants=restaurants, search=True)


@app.route('/menu', methods=['GET'])
def show_menu():
    rest_id = request.args.get('id')
    dishs = session.query(Dish).filter(rest_id)
    session.commit()
    return render_template('main_form.html',
                           title='', objects=dishs, restaurants=restaurants, search=False)


def main():
    app.run(port=5000, host='127.0.0.1')


if __name__ == '__main__':
    main()