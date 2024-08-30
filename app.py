from flask import Flask, request, make_response, jsonify
import json
from db.DBManager import DBManager
from flask_cors import CORS
from utils.Logger import Logger


app = Flask(__name__)
CORS(app)
#app.wsgi_app = ProxyFix(
#   app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
#)
conn = None

logger = Logger()

@app.route('/listEntries',methods=['GET'])
def listEntries():
    blog_id = request.args.get('blogId') 
    global conn
    conn = DBManager()
    res = conn.list_entries(blog_id)
    out = []
    for entry in res:
        formatted = entry.api_format()
        out.append(formatted)
    return jsonify(out), 200

@app.route('/listBlogs',methods=['GET'])
def listBlogs():
    global conn
    conn = DBManager()
    res = conn.list_blogs()
    out = []
    for blog in res:
        formatted = blog.api_format()
        out.append(formatted)
    return json.dumps(out), 200

@app.route('/listTags',methods=['GET'])
def listTags():
    global conn
    conn = DBManager()
    res = conn.list_tags()
    out = []
    for tag in res:
        formatted = tag.api_format()
        out.append(formatted)
    return json.dumps(out), 200

@app.route('/getBlog/<id>',methods=['GET'])
def getBlog(id=None):
    global conn
    conn = DBManager()
    res = conn.get_blog(id)
    formatted = res.api_format()
    return json.dumps(formatted), 200

@app.route('/getEntry/<id>',methods=['GET'])
def getEntry(id=None):
    global conn
    conn = DBManager()
    res = conn.get_entry(id)
    formatted = res.api_format()
    return json.dumps(formatted), 200

@app.route('/createBlog/<name>',methods=['GET','POST'])
def createBlog(name=None):
    global conn
    conn = DBManager()
    blog_id = conn.create_blog(name)
    return json.dumps(str(blog_id)), 201

@app.route('/createEntry',methods=['GET','POST'])
def createEntry():
    data  = request.json
    global conn
    conn = DBManager()
    entry_id = conn.create_entry(data.get('blogId'), data.get('tagId'), data.get('title'), data.get('content'))
    logger.log("entry created with id {}".format(entry_id))
    return json.dumps(str(entry_id)), 201

@app.route('/updateEntry',methods=['GET','POST'])
def updateEntry():
    data  = request.json
    global conn
    conn = DBManager()
    print(data.get('title'))
    print(data.get('content'))
    conn.update_entry(data.get('entryId'), data.get('title'), data.get('content'))
    return "Success", 204

@app.route('/deleteEntry/<id>',methods=['GET','DELETE'])
def deleteEntry(id=None):
    global conn
    conn = DBManager()
    conn.delete_entry(id)
    return "Success", 204

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
