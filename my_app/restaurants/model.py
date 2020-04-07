from my_app import db
 
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    category = db.Column(db.String(255))
    michellin_stars = db.Column(db.Float(asdecimal=True))
 
    def __init__(self, name, category, michellin_stars):
        self.name = name
        self.category = category
        self.michellin_stars = michellin_stars
 
    def __repr__(self):
        return '<Product %d>' % self.id