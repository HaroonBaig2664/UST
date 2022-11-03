# Import Flask class

from flask import Flask, redirect,render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# make changes in flask config
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///products.db"

# database instance
db=SQLAlchemy(app)

# schema of database
class MyProduct(db.Model):
    productid=db.Column(db.Integer,primary_key=True)
    product=db.Column(db.String(200),nullable=False)
    desc=db.Column(db.String(200),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.productid}-{self.product}-{self.desc}"


# @ - Decorators in Python to tell flask what URL should trigger our function
# app.route() function returns an instance of single flask route. 
# This route can be used to handle HTTP with some optional middleware.  
@app.route('/',methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        product_id=request.form['productid']
        product=request.form['product']
        desc=request.form['desc']
        product=MyProduct(productid=product_id,product=product,desc=desc)
        db.session.add(product)
        db.session.commit()
    all_product=MyProduct.query.all()
    return render_template("index.html",allProducts=all_product)
    # return "<p>Welcome to Flask</p>"

# end points using app.routes
@app.route('/show')
def show():
    all_product=MyProduct.query.all()
    print(all_product)
    return "<p>This is clothing page</p>"

# end points using app.routes
@app.route('/update/<int:productid>',methods=["GET","POST"])
def update_fun(productid):
    if request.method=="POST":
        productid=request.form['productid']
        product=request.form['product']
        desc=request.form['desc']
        product_details=MyProduct.query.filter_by(productid=productid).first()
        product_details.productid=productid
        product_details.product=product
        product_details.desc=desc
        db.session.add(product_details)
        db.session.commit()
        return redirect("/")
    product=MyProduct.query.filter_by(productid=productid).first()
    return render_template("update.html",product=product)

@app.route('/delete/<int:productid>')
def delete_fun(productid):
    product=MyProduct.query.filter_by(productid=productid).first()
    db.session.delete(product)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True,port=8000)

