from flask import Flask, render_template, request, jsonify
from bson.objectid import ObjectId
app = Flask(__name__)

import certifi

ca = certifi.where()
from pymongo import MongoClient
client = MongoClient('mongodb+srv://marineryu:nara0318!!!@cluster0.arlrm1f.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

def objectIdDecoder(list):
  results=[]
  for document in list:
    document['_id'] = str(document['_id'])
    results.append(document)
  return results

def getSpecificId(id):
  result = objectIdDecoder(list(db.good.find({"_id": ObjectId(id)})))
  return str(result)


@app.route('/')
def home():
    return render_template('main.html')

@app.route('/leehanSelf')
def leehanSelf():
    return render_template('leehanSelf.html')

@app.route('/jun')
def jun():
    return render_template('jun.html')

@app.route('/ho')
def ho():
    return render_template('ho.html')

@app.route('/headam')
def haedam():
    return render_template('headam.html')

@app.route('/bin')
def bin():
    return render_template('bin.html')

@app.route('/guestbook')
def guestbook():
    return render_template('binguestbook.html')



@app.route("/good", methods=["POST"])
def good_post():
    good_receive = request.form['good_give']
    good_list = list(db.good.find({}))
    count = len(good_list) + 1
    doc = {
        'num': count,
        'good': good_receive,
        'done': 0
    }
    db.good.insert_one(doc)
    return jsonify({'msg': '등록완료'})

@app.route("/goods/<id>", methods=["PUT"])
def good_update(id):
    good_receive = request.form['good_give']
    db.good.update_one({'_id': ObjectId(id)}, {'$set': {'good': good_receive}})
    return jsonify({'msg': '수정 완료!'})

@app.route("/goods/<id>", methods=["DELETE"])
def good_delete(id):
    db.good.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': '삭제 완료!'})


@app.route("/good/done", methods=["POST"])
def good_done():
    num_receive = request.form['num_give']
    db.good.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
    return jsonify({'msg': '좋은 습관 완료!'})


@app.route("/good", methods=["GET"])
def good_get():
    good_list = objectIdDecoder(list(db.good.find({})))
    return jsonify({'goods': good_list})



# 혜담님
@app.route("/haedam/comment", methods=["POST"])
def haedam_comment():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.dam.insert_one(doc)
    return jsonify({'msg': '응원 완료!'})


@app.route("/haedam/comments/<id>", methods=["PUT"])
def haedam_comment_update(id):
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    db.dam.update_one({'_id': ObjectId(id)}, {'$set': {'name': name_receive}})
    db.dam.update_one({'_id': ObjectId(id)}, {'$set': {'comment': comment_receive}})
    return jsonify({'msg': '수정 완료!'})


@app.route("/haedam/comments/<id>", methods=["DELETE"])
def haedam_comment_delete(id):
    db.dam.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': '삭제 완료!'})


@app.route("/haedam/comment", methods=["GET"])
def haddam_comment_get():
    comment_list = objectIdDecoder(list(db.dam.find({})))
    return jsonify({'comments': comment_list})



# 원빈
@app.route("/bin/guestbook/wonbin", methods=["POST"])
def bin_comment():
    name_receive = request.form['name_receive']
    comment_receive = request.form['comment_receive']

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.wonbin.insert_one(doc)

    return jsonify({'msg': '등록 완료!'})
@app.route("/bin/guestbook/wonbin/<id>", methods=["PUT"])
def bin_comment_update(id):
    name_receive = request.form['name_receive']
    comment_receive = request.form['comment_receive']
    db.wonbin.update_one({'_id': ObjectId(id)}, {'$set': {'name': name_receive}})
    db.wonbin.update_one({'_id': ObjectId(id)}, {'$set': {'comment': comment_receive}})
    return jsonify({'msg': '수정 완료!'})

@app.route("/bin/guestbook/wonbin/<id>", methods=["DELETE"])
def bin_comment_delete(id):
    db.wonbin.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': '삭제 완료!'})


@app.route("/bin/guestbook/wonbin", methods=["GET"])
def bin_comment_get():
    comment_list = objectIdDecoder(list(db.wonbin.find({})))
    return jsonify({'comments': comment_list})


# 호성
@app.route("/ho/comment", methods=["POST"])
def ho_comment_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.hocomment.insert_one(doc)
    return jsonify({'msg': '응원 완료!'})

@app.route("/ho/comment", methods=["GET"])
def ho_comment_get():
    comment_list = objectIdDecoder(list(db.hocomment.find({})))
    return jsonify({'comments': comment_list})

@app.route("/ho/comments/<id>", methods=["DELETE"])
def ho_comments_delete(id):
    db.hocomment.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': '삭제 완료!'})

@app.route("/ho/comments/<id>", methods=["PUT"])
def ho_comments_update(id):
    comment_receive = request.form['comment_give']
    name_receive = request.form['name_give']
    db.hocomment.update_one({'_id': ObjectId(id)}, {'$set': {'comment': comment_receive}})
    db.hocomment.update_one({'_id': ObjectId(id)}, {'$set': {'name': name_receive}})
    return jsonify({'msg': '수정 완료!'})


# 환준
@app.route("/jun/comment", methods=["POST"])
def jun_comment_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.woncomment.insert_one(doc)
    return jsonify({'msg': '응원 완료!'})

@app.route("/jun/comments/<id>", methods=["PUT"])
def jun_comment_update(id):
    comment_receive = request.form['comment_give']
    name_receive = request.form['name_give']
    db.woncomment.update_one({'_id': ObjectId(id)}, {'$set': {'comment': comment_receive}})
    db.woncomment.update_one({'_id': ObjectId(id)}, {'$set': {'name': name_receive}})
    return jsonify({'msg': '수정 완료!'})


@app.route("/jun/comment", methods=["GET"])
def jun_comment_get():
    comment_list = objectIdDecoder(list(db.woncomment.find({})))
    return jsonify({'comments': comment_list})

@app.route("/jun/comments/<id>", methods=["DELETE"])
def jun_comment_delete(id):
    db.woncomment.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': '삭제 완료!'})



# 한결
@app.route("/leehanSelf/comment", methods=["POST"])
def han_comment_post():
    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]

    doc = {
        'name': name_receive,
        'comment': comment_receive
    }

    db.hancomment.insert_one(doc)
    return jsonify({'msg': '응원 완료!'})

@app.route("/leehanSelf/comments/<id>", methods=["PUT"])
def han_comments_update(id):
    comment_receive = request.form['comment_give']
    name_receive = request.form['name_give']
    db.hancomment.update_one({'_id': ObjectId(id)}, {'$set': {'comment': comment_receive}})
    db.hancomment.update_one({'_id': ObjectId(id)}, {'$set': {'name': name_receive}})
    return jsonify({'msg': '수정 완료!'})


@app.route("/leehanSelf/comment", methods=["GET"])
def han_comment_get():
    comment_list = objectIdDecoder(list(db.hancomment.find({})))
    return jsonify({'comments': comment_list})

@app.route("/leehanSelf/comments/<id>", methods=["DELETE"])
def han_comment_delete(id):
    db.hancomment.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': '삭제 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5006, debug=True)
