from flask import Flask, redirect, session, render_template, request
import pymongo

app=Flask(__name__, static_folder="public", static_url_path="/")

@app.route("/")
def index():
    return redirect("main/main.html")

@app.route("/a")
def index():
    return redirect("main/main.html")

