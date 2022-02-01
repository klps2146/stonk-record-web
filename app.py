from flask import Flask, redirect, session, render_template, request, url_for
import pymongo, time
from flask_bcrypt import Bcrypt

client = pymongo.MongoClient("mongodb+srv://root:root123@realmcluster.rbqar.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.website
collection=db.users
collection_pwd=db.user
app=Flask(__name__, static_folder="public", static_url_path="/")
app.config["SECRET_KEY"]="jsisc3re"

def value_caculate():
    pass

def session_setting():
    pass

@app.route("/") # main
def index():
    return redirect("/index/index.html")

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
    dividend_rate=round(float(dividend_rate), 2)
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
    divend=(float(dividend_rate)*float(eps_year)*0.01)
    divend=round(divend, 2)
    yield_=100*((float(dividend_rate)*float(eps_year))/float(share))
    yield_=round(float(yield_), 2)
    try:
        datas_get=collection.find()
        data_get=[]
        company_list=[]
        for i in datas_get:
            data_get.append(i)
            company_list.append(i["company"])
        if data_get[0]==None: # none data in DB
            collection.insert_one({
            "company":company,
            "date":last_update,
            "share":share,
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
                "dividend_rate":dividend_rate, 
                "dividend":divend, 
                "yield":yield_, 
            }
        })
        for i in data_get:
            if i['company']==company: 
                collection.update_one({
                    "company":company
                },{
                    "$set":{
                        "date":last_update,
                        "share":share,
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
                            "dividend_rate":dividend_rate,
                            "dividend":divend,
                            "yield":yield_,
                        }
                    }
                })
        else: # nothing exist
            non_exi=0
            for i in company_list:
                if i != company:
                    non_exi+=1
            else:
                if non_exi==len(company_list):
                    collection.insert_one({
                        "company":company,
                        "date":last_update,
                        "share":share,
                        (years):{
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
                            "dividend_rate":dividend_rate, 
                            "dividend":divend,
                            "yield":yield_,
                            "guess":1
                        }
                    })

    except: # out of thinking
        collection.insert_one({
            "company":company,
            "date":last_update,
            "share":share,
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
                "dividend_rate":dividend_rate,
                "dividend":divend,
                "yield":yield_,
            }
        })
    return redirect(url_for("display"))

@app.route("/dis")
def display(): # sorting data
    datas=collection.find()
    data_clus=[]
    year_clus={}
    year_doc=[]
    company_clus=[]
    output_doc={}
    output_clus=[]
    for i in datas:
        data_clus.append(i)
        for f in i:
            if f=="company":
                company_clus.append(i["company"])
            if f!="_id" and f!="company" and f!="date" and f!="guess" and f!="share" and f!="yield_now" and f!="aim" and f!="l_aim" and f != "l_add" and f!="r_add":
                year_doc.append(f)
        else:
            year_clus[i["company"]]=sorted(list(map(int, year_doc)))
            year_doc=[]
    fram=0
    for company_n in year_clus:
        output_doc["company"]=company_n
        output_doc["date"]=data_clus[fram]["date"]
        output_doc["share"]=data_clus[fram]["share"]
        try:
            output_doc["aim"]=data_clus[fram]["aim"]
        except:
            output_doc["aim"]=""
        output_doc["yield_now"]=(data_clus[fram][time.strftime('%Y',time.gmtime())]["yield"])
        try:
            if data_clus[fram]["aim"]!="":
                eps_aim=round(100*(float(data_clus[fram][time.strftime('%Y',time.gmtime())]["dividend"]))/(float(data_clus[fram]["aim"])),2)
                output_doc["l_aim"]=eps_aim
                eps_add=eps_aim-float(data_clus[fram]["share"])
                output_doc["l_add"]=round(eps_add,2)
                output_doc["r_add"]=round(100*eps_add/float(data_clus[fram]["share"]),2)
        except:
            pass
        for year_ in year_clus[company_n]:
            output_doc[year_]=data_clus[fram][str(year_)]
        else:
            output_clus.append(output_doc)
            output_doc={}
        fram+=1
    return render_template("display.html", data=output_clus)

@app.route("/rev", methods=["POST"]) # 更新
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
            if f!="_id" and f!="company" and f!="date" and f!="guess" and f!="share"  and f!="yield_now" and f!="aim"  and f!="l_aim"  and f != "l_add" and f != "r_add":
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
                share=round((float(request.form[f"{cp_n}_share"])), 2)
                dividend_rate=round(100*(float(dividend/eps_q_y)), 2)
                yield_=round(100*(float(dividend/share)), 2)
                if request.form[f"{cp_n}_aim"]!="":
                    aim=round((float(request.form[f"{cp_n}_aim"])), 2)
                else:
                    aim=""
                collection.update_one({
                    "company":cp_n
                },{
                    "$set":{
                        "date":date,
                        "share":share,
                        "aim":aim,
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
                share=round((float(request.form[f"{cp_n}_share"])), 2)
                dividend_rate=round(100*(float(dividend/eps_y)), 2)
                yield_=round(100*(float(dividend/share)), 2)
                if request.form[f"{cp_n}_aim"]!="":
                    aim=round((float(request.form[f"{cp_n}_aim"])), 2)
                else:
                    aim=""
                collection.update_one({
                    "company":cp_n
                },{
                    "$set":{
                        "share":share,
                        "date":date,
                        "aim":aim,
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
                        }
                    }
                })
    return render_template("redirecting.html")

@app.route("/simp") # 簡化
def simplify():
    datas=collection.find()
    year_now=int(time.strftime('%Y',time.gmtime()))
    data_clus=[]
    company_clus=[]
    for i in datas:
        data_clus.append(i)
        for f in i:
            if f=="company":
                company_clus.append(i["company"])
            if f!="_id" and f!="company" and f!="date" and f!="guess" and f!="share" and f!="yield_now" and f!="aim" and f!="l_aim" and f != "l_add" and f!="r_add":
                if int(f) < year_now-1:
                    collection.update_one({
                        "company":i["company"]
                    },{"$set":{
                        f:{
                            "EPS_year":i[f]["EPS_year"],
                            "dividend_rate":i[f]["dividend_rate"],
                            "dividend":i[f]["dividend"],
                            "yield":i[f]["yield"],
                            "simp":1
                        }
                    }})
                    
    return redirect("/dis")

@app.route("/del", methods=["POST"])
def delete():
    try:
        company=request.form["company"]
        year=request.form["year"]
    except:
        pass
    try:
        company_del=request.form["company_del"]
    except:
        pass
    if company_del=="":
        try:
            collection.update_one({
                "company":company
            },{"$unset":{
                year:1,
            }})
        except:
            return redirect("/delete/error.html")
    elif company_del!="":
        try:
            collection.delete_one({"company":company_del})
        except:
            return redirect("/delete/error.html")
    return redirect("/dis")

@app.route("/signin", methods=["POST"])
def signin():
    account=request.form["account"]
    pwd=request.form["pwd"]
    data=collection_pwd.find()
    for i in data:
        if i["account"]==account:
            if Bcrypt().check_password_hash(i["password"], pwd):
                return i["account"]+" signin scuessful"

            else:
                return "wrong password"
    return "no account"

@app.route("/signup", methods=["POST"])
def signup():
    user_name=request.form["usn"]
    account=request.form["acc"]
    pwd=request.form["pwd"]
    pwd=Bcrypt().generate_password_hash(pwd).decode("utf-8")
    data=collection_pwd.find()
    repeat=0
    for i in data:
        if i["account"]==account:
            repeat+=1
        else:
            repeat+=0
    if repeat==0:
        collection_pwd.insert_one({
            "name":user_name,
            "account":account,
            "password":pwd
        })
        return "update scf"
    else:
        return """
        <h1>重複使用的帳號</h1>
        <script>
            function a(){
                window.location.href='/signup/signup.html';
            }
            window.onload=setTimeout(a, 1800);
        </script>
        """

@app.route("/term")
def term():
    return redirect("/term/term.html")

app.debug=True
app.run()
