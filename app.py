from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/categories/')
def categories():
    categories_list = {"Одежда": "clothes.html", "Обувь": "shoes.html", "Спортивное": "sports.html",
                       "Аксессуары": "accessories.html"}
    return render_template('categories.html', categories_list=categories_list)


@app.route('/clothes/')
def clothes():
    clothes_list = [
        {'name': 'Футболка', 'price': 75.13},
        {'name': 'Джинсы', 'price': 477.54},
        {'name': 'Платье', 'price': 457.65}
    ]
    return render_template('clothes.html', list=clothes_list)


@app.route('/shoes/')
def shoes():
    shoes_list = [
        {'name': 'Кроссовки', 'price': 254.47},
        {'name': 'Кеды', 'price': 156.32},
        {'name': 'Туфли', 'price': 568.08}
    ]
    return render_template('shoes.html', list=shoes_list)


@app.route('/sports/')
def sports():
    sports_list = [
        {'name': 'Форма', 'price': 5282.14},
        {'name': 'Тренажер', 'price': 15478.10},
        {'name': 'Гантеля', 'price': 188.97}
    ]
    return render_template('sports.html', list=sports_list)


@app.route('/accessories/')
def accessories():
    accessories_list = [
        {'name': 'Серьги', 'price': 166.20},
        {'name': 'Кольцо', 'price': 122.54},
        {'name': 'Подвеска', 'price': 558.42}
    ]
    return render_template('accessories.html', list=accessories_list)


@app.route('/about/')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
