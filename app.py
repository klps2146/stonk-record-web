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
    share=round(float(share), 2)
    dividend_rate=float(dividend_rate)
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
    divend=(float(dividend_rate)*float(eps_year))
    divend=round(divend, 2)
    yield_=round((float(dividend_rate)*float(eps_year))/float(share), 2)
    yield_=round(yield_, 2)
    try:
        datas_get=collection.find()
        data_get=[]
        company_list=[]
        for i in datas_get:
            data_get.append(i)
            company_list.append(i["company"])
        print(data_get)
        if data_get[0]==None: # 資料庫沒資料
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
                "yield":yield_, # 殖利率
                "share":share
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
                            "yield":yield_, # 殖利率
                            "share":share
                        }
                    }
                })
        else: # 都不存在
            non_exi=0
            for i in company_list:
                if i != company:
                    non_exi+=1
            else:
                if non_exi==len(company_list):
                    collection.insert_one({
                        "company":company,
                        "date":last_update,
                        int(years):{
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
                            "yield":yield_, # 殖利率
                            "share":share,
                            "guess":1
                        }
                    })

    except: # 資料庫為空少數例外 無法獲得資料庫資料
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
                "yield":yield_, # 殖利率
                "share":share
            }
        })
    return redirect(url_for("display"))

@app.route("/dis")
def display():
    datas=collection.find()
    return render_template("display.html", data=datas)

@app.route("/rev", methods=["POST"])
def revise():
    datas=collection.find()
    data_clus=[]
    year_clus={}
    year_doc=[]
    company_clus=[]
    date=request.form["up_dt"]
    for i in datas:
        data_clus.append(i)
        for f in i:
            if f=="company":
                company_clus.append(i["company"])
            if f!="_id" and f!="company" and f!="date" and f!="guess":
                year_doc.append(f)
        else:
            year_clus[i["company"]]=year_doc
            year_doc=[]  
    st=False
    for cp_n in company_clus:
        for years in year_clus[cp_n]:
            for da_c in data_clus:
                if da_c["company"]==cp_n:
                    if da_c[years]["EPS_Q1"]!="":
                        st=True
                    else:
                        st=False
            if st:
                eps_q_1=round((float(request.form[f"{cp_n}_{years}_Q_1"])), 3)
                eps_q_2=round((float(request.form[f"{cp_n}_{years}_Q_2"])), 3)
                eps_q_3=round((float(request.form[f"{cp_n}_{years}_Q_3"])), 3)
                eps_q_4=round((float(request.form[f"{cp_n}_{years}_Q_4"])), 3)
                eps_q_y=float(eps_q_1)+float(eps_q_2)+float(eps_q_3)+float(eps_q_4)
                eps_q_y=round(eps_q_y, 3)
                dividend=round((float(request.form[f"{cp_n}_{years}_dividend"])), 2)
                share=round((float(request.form[f"{cp_n}_{years}_share"])), 2)
                dividend_rate=round(float(dividend/eps_q_y), 2)
                yield_=round(float(dividend/share), 2)
                collection.update_one({
                    "company":cp_n
                },{
                    "$set":{
                        "date":date,
                        years:{ 
                            "EPS_year":eps_q_y,
                            "EPS_m_1":"",
                            "EPS_m_2":"",
                            "EPS_m_3":"",
                            "EPS_Q1":eps_q_1,
                            "EPS_Q2":eps_q_2,
                            "EPS_Q3":eps_q_3,
                            "EPS_Q4":eps_q_4,
                            "dividend_rate":dividend_rate,
                            "dividend":dividend,
                            "yield":yield_,
                            "share":share
                        }
                    }
                })
            else:
                eps_m_1=round((float(request.form[f"{cp_n}_{years}_m_1"])), 3)
                eps_m_2=round((float(request.form[f"{cp_n}_{years}_m_2"])), 3)
                eps_m_3=round((float(request.form[f"{cp_n}_{years}_m_3"])), 3)
                eps_m_4=round((float(request.form[f"{cp_n}_{years}_m_4"])), 3)
                eps_m_5=round((float(request.form[f"{cp_n}_{years}_m_5"])), 3)
                eps_m_6=round((float(request.form[f"{cp_n}_{years}_m_6"])), 3)
                eps_m_7=round((float(request.form[f"{cp_n}_{years}_m_7"])), 3)
                eps_m_8=round((float(request.form[f"{cp_n}_{years}_m_8"])), 3)
                eps_m_9=round((float(request.form[f"{cp_n}_{years}_m_9"])), 3)
                eps_m_10=round((float(request.form[f"{cp_n}_{years}_m_10"])), 3)
                eps_m_11=round((float(request.form[f"{cp_n}_{years}_m_11"])), 3)
                eps_m_12=round((float(request.form[f"{cp_n}_{years}_m_12"])), 3)
                eps_y=eps_m_1+eps_m_2+eps_m_3+eps_m_4+eps_m_5+eps_m_6+eps_m_7+eps_m_8+eps_m_9+eps_m_10+eps_m_11+eps_m_12
                dividend=round((float(request.form[f"{cp_n}_{years}_dividend"])), 2)
                share=round((float(request.form[f"{cp_n}_{years}_share"])), 2)
                dividend_rate=round(float(dividend/eps_y), 2)
                yield_=round(float(dividend/share), 2)
                collection.update_one({
                    "company":cp_n
                },{
                    "$set":{
                        "date":date,
                        years:{
                            "EPS_year":eps_y,
                            "EPS_m_1":eps_m_1,
                            "EPS_m_2":eps_m_2,
                            "EPS_m_3":eps_m_3,
                            "EPS_m_4":eps_m_4,
                            "EPS_m_5":eps_m_5,
                            "EPS_m_6":eps_m_6,
                            "EPS_m_7":eps_m_7,
                            "EPS_m_8":eps_m_8,
                            "EPS_m_9":eps_m_9,
                            "EPS_m_10":eps_m_10,
                            "EPS_m_11":eps_m_11,
                            "EPS_m_12":eps_m_12,
                            "EPS_Q1":"",
                            "EPS_Q2":"",
                            "dividend_rate":dividend_rate,
                            "dividend":dividend,
                            "yield":yield_,
                            "share":share
                        }
                    }
                })
                pass
    return "jx"