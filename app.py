from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
cors = CORS(app)

@app.route('/races', methods=['GET'])
def get_races():
    con = sqlite3.connect('yosou.db')
    result = con.execute('select * from レース')
    races = [
        {
        'レースID': row[0],
        '日付': row[1],
        '会場': row[2],
        'レース番号': row[3],
        'レース名': row[4],
        '種別': row[5],
        '距離': row[6]
        }for row in result
        ]
    return jsonify(races)

@app.route('/races', methods=['POST'])
def post_races():
    content = request.get_json()
    print(content)
    con = sqlite3.connect('yosou.db')
    sql = "insert into レース (レースID,日付,会場,レース番号,レース名,種別,距離) values(?,?,?,?,?,?,?)"
    con.execute(sql,(content['レースID'],content['日付'],content['会場'],content['レース番号'],content['レース名'],content['種別'],content['距離']))
    con.commit()
    return jsonify({'message': 'created'})


@app.route('/predict',methods=['GET'])
def get_predict():
    con = sqlite3.connect('yosou.db')
    result = con.execute("select * from 予想")
    predict = [
        {
        '予想番号':row[0],
        'レースID':row[1],
        '本命馬番':row[2],
        '対抗馬番':row[3],
        '単穴馬番':row[4],
        '投稿日付':row[5]
        }for row in result
        ]
    return jsonify(predict)

@app.route('/predict',methods=['POST'])
def post_predict():
    content = request.get_json()
    print(content)
    con = sqlite3.connect('yosou.db')
    sql = "insert into 予想 (予想番号,レースID,本命馬番,対抗馬番,単穴馬番,投稿日付) values(?,?,?,?,?,?)"
    con.execute(sql,(content['予想番号'],content['レースID'],content['本命馬番'],content['対抗馬番'],content['単穴馬番'],content['投稿日付']))
    con.commit()
    return jsonify({'message': 'created'})
