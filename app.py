import os
from flask import Flask,jsonify,request,render_template,make_response
from flask_restful import Resource,Api
import base64
app=Flask(__name__)
api=Api(app)
'''===========================DB CONNECTION==============================='''
import psycopg2
conn = psycopg2.connect(
    host=os.getenv("host"),
    database=os.getenv("database"),
    user=os.getenv("user"),
    password=os.getenv("password")
)

cursor = conn.cursor()



class imagedisplayer(Resource):
    def get(self):
        image=request.args.get('image')
        cursor.execute("SELECT * FROM photos WHERE unique_id=%s",(image,))
        data=cursor.fetchone()
        with open('static/'+data[1], 'wb') as file_to_save:
            file_to_save.write(data[2])
        '''show image on html page'''
        return make_response(render_template('image.html',image=data[1]))

api.add_resource(imagedisplayer,'/')

if __name__=='__main__':
    app.run(debug=True)