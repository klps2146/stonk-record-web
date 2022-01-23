from flask import Flask, redirect, session, render_template, request, url_for
import pymongo

client = pymongo.MongoClient("mongodb+srv://root:root123@realmcluster.rbqar.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.website
collection=db.users
app=Flask(__name__, static_folder="public", static_url_path="/")

def value_caculate():
    pass

@app.route("/") # 主頁面
def index():
    return redirect("/main/main.html")

@app.route("/res", methods=["POST"])
def res():
    company=request.form["company"]
    years=request.form["year"]
    eps_1=request.form["EPS_1"]
    eps_2=request.form["EPS_2"]
    eps_3=request.form["EPS_3"]
    eps_4=request.form["EPS_4"]
    m_1=request.form["m_1"]
    m_2=request.form["m_2"]
    m_3=request.form["m_3"]
    m_4=request.form["m_4"]
    m_5=request.form["m_5"]
    m_6=request.form["m_6"]
    m_7=request.form["m_7"]
    m_8=request.form["m_8"]
    m_9=request.form["m_9"]
    m_10=request.form["m_10"]
    m_11=request.form["m_11"]
    m_12=request.form["m_12"]
    dividend_rate=request.form["dividend_rate"]
    last_update=request.form["date"]
    share=request.form["share"]
    if (m_1=="" and m_2==""):
        eps_1=float(eps_1)
        eps_2=float(eps_2)
        eps_3=float(eps_3)
        eps_4=float(eps_4)
        eps_year=eps_1+eps_2+eps_3+eps_4
    else:
        m_1=float(m_1)
        m_2=float(m_2)
        m_3=float(m_3)
        m_4=float(m_4)
        m_5=float(m_5)
        m_6=float(m_6)
        m_7=float(m_7)
        m_8=float(m_8)
        m_9=float(m_9)
        m_10=float(m_10)
        m_11=float(m_11)
        m_12=float(m_12)
        eps_year=m_1+m_2+m_3+m_4+m_4+m_5+m_6+m_7+m_7+m_8+m_9+m_10+m_11+m_12
    divend=str(float(dividend_rate)*float(eps_year))
    yield_=str((float(dividend_rate)*float(eps_year))/float(share))
    try:
        datas_get=collection.find()
        data_get=[]
        for i in datas_get:
            data_get.append(i)
        print(data_get)
        if data_get[0]==None:
            collection.insert_one({
            "company":company,
            "date":last_update,
            years:{
                "EPS_year":eps_year,
                "EPS_Q1":eps_1,
                "EPS_Q2":eps_2,
                "EPS_Q3":eps_3,
                "EPS_Q4":eps_4,
                "EPS_m_1":m_1,
                "EPS_m_2":m_2,
                "EPS_m_3":m_3,
                "EPS_m_4":m_4,
                "EPS_m_5":m_5,
                "EPS_m_6":m_6,
                "EPS_m_7":m_7,
                "EPS_m_8":m_8,
                "EPS_m_9":m_9,
                "EPS_m_10":m_10,
                "EPS_m_11":m_11,
                "EPS_m_12":m_12,
                "dividend_rate":dividend_rate, # 配息率
                "dividend":divend, # 配息
                "yield":yield_ # 殖利率
            }
        })
        for i in data_get:
            if i['company']==company:
                collection.update_one({
                    "company":company
                },{
                    "$set":{
                        "date":last_update,
                        years:{
                            "EPS_year":eps_year,
                            "EPS_Q1":eps_1,
                            "EPS_Q2":eps_2,
                            "EPS_Q3":eps_3,
                            "EPS_Q4":eps_4,
                            "EPS_m_1":m_1,
                            "EPS_m_2":m_2,
                            "EPS_m_3":m_3,
                            "EPS_m_4":m_4,
                            "EPS_m_5":m_5,
                            "EPS_m_6":m_6,
                            "EPS_m_7":m_7,
                            "EPS_m_8":m_8,
                            "EPS_m_9":m_9,
                            "EPS_m_10":m_10,
                            "EPS_m_11":m_11,
                            "EPS_m_12":m_12,
                            "dividend_rate":dividend_rate, # 配息率
                            "dividend":divend, # 配息
                            "yield":yield_ # 殖利率
                        }
                    }
                })
    except:
        collection.insert_one({
            "company":company,
            "date":last_update,
            years:{
                "EPS_year":eps_year,
                "EPS_Q1":eps_1,
                "EPS_Q2":eps_2,
                "EPS_Q3":eps_3,
                "EPS_Q4":eps_4,
                "EPS_m_1":m_1,
                "EPS_m_2":m_2,
                "EPS_m_3":m_3,
                "EPS_m_4":m_4,
                "EPS_m_5":m_5,
                "EPS_m_6":m_6,
                "EPS_m_7":m_7,
                "EPS_m_8":m_8,
                "EPS_m_9":m_9,
                "EPS_m_10":m_10,
                "EPS_m_11":m_11,
                "EPS_m_12":m_12,
                "dividend_rate":dividend_rate, # 配息率
                "dividend":divend, # 配息
                "yield":yield_ # 殖利率
            }
        })

    return redirect(url_for("display"), code=307)

@app.route("/dis", methods=["POST"])
def display():
    return redirect("/display/display.html")
    
app.debug=True
app.run()