import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from my_app import db, app
from my_app.restaurants.model import Restaurant
 
restaurants = Blueprint('restaurants', __name__)
 
@restaurants.route('/')
@restaurants.route('/home')
def home():
    return "Welcome to the Restaurant List Home."
 
 
class RestaurantView(MethodView):
 
    def get(self, id=None, page=1):
        if not id:
            res = {}
        else:
            restaurant = Restaurant.query.filter_by(id=id).first()
            if not restaurant:
                abort(404)
            res = {
                'name': restaurant.name,
                'category': restaurant.category,
                'michellin_stars' : str(restaurant.michellin_stars)
            }
        return jsonify(res)
 
    def post(self):
        name = request.form.get('name')
        category = request.form.get('category')
        michellin_stars = request.form.get('michellin_stars')
        restaurant = Restaurant(name, category, michellin_stars)
        db.session.add(restaurant)
        db.session.commit()
        return jsonify({restaurant.id: {
            'name': restaurant.name,
            'category': restaurant.category,
            'michellin_stars': str(michellin_stars)
        }})
 
    def put(self, id):
        name = request.form.get('name')
        category = request.form.get('category')
        michellin_stars = request.form.get('michellin_stars')
        db.session.query(Restaurant).filter(Restaurant.id == id).update({'michellin_stars': str(michellin_stars),'name': name, 'category': category})
        db.session.commit()
        res = {
            'name': restaurant.name,
            'category': restaurant.category,
            'michellin_stars' : str(restaurant.michellin_stars)
        }
        return jsonify(res)
 
    def delete(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        db.session.delete(restaurant)
        db.session.commit()
        return jsonify({restaurant.id: {
            'name': restaurant.name,
            'category': restaurant.category,
            'michellin_stars': str(michellin_stars)
        }})
 
 
restaurant_view =  RestaurantView.as_view('restaurant_view')
app.add_url_rule(
    '/restaurant/', view_func=restaurant_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/restaurant/<int:id>', view_func=restaurant_view, methods=['GET','PUT',"DELETE"]
)