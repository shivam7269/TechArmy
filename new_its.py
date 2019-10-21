import pymongo
import datetime
import json
from flask import Flask, render_template, request, url_for, redirect, abort, jsonify, make_response
from flask_cors import CORS, cross_origin
from bson import json_util
import random

app=Flask(__name__)


@app.route('/addProblem',methods=['POST','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def addProblem():
	if request.method == 'POST':
		post= request.json
		client = pymongo.MongoClient("mongodb+srv://rohansharma1606:_kwB&9Q4GTZg2fA@se-6kdpi.mongodb.net/test?retryWrites=true&w=majority")
		db=client.hack_se
		posts = db.problem
		post_id = posts.insert_one(post)
		client.close()
		return "added"

@app.route('/getBestScore',methods = ['GET','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def getBestScore():
	if request.method == 'GET':
		client = pymongo.MongoClient("mongodb+srv://rohansharma1606:_kwB&9Q4GTZg2fA@se-6kdpi.mongodb.net/test?retryWrites=true&w=majority")
		db=client.hack_se
		posts=db.contest
		contest_id = posts["contest_id"]

		posts1=posts["student_list"]
		contest_id=request.args.get('contest_id',type=str)
		student_id=request.args.get('student_id',type=str)

		if(posts1.find({"student_id":student_id}) is not None and posts.find({"contest_id":contest_id}) is not None):
			best_score=posts1["best_score"]
			return jsonify({}),201
		else : return jsonify({}),405
		


@app.route('/addBestCode',methods = ['PUT','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def addBestCode():
	if request.method == 'PUT':
		post = request.json
		client = pymongo.MongoClient("mongodb+srv://rohansharma1606:_kwB&9Q4GTZg2fA@se-6kdpi.mongodb.net/test?retryWrites=true&w=majority")
		db=client.hack_se
		posts=db.contest
		student_id = post["student_id"]
		best_score = post["best_score"]
		best_code = post["best_code"]
		best_code_language = post["best_code_language"]

		posts1=posts["student_list"]
		if(posts1.find({"student_id":student_id}) is NULL):
			post_id=posts1.insert_one(post)
			return jsonify('Added'),201
		else :
			result=posts1.update_many(
			{"student_id":student_id},
			{
				"$set":{"best_score":best_score},
				"$set":{"best_code":best_code},
				"$set":{"best_code_language":best_code_language}
			}
		return jsonify({}),201

	
					
		
		
@app.route('/addContest',methods = ['POST','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def addContest():
	if request.method == 'POST':
		post = request.json
		client = pymongo.MongoClient("mongodb+srv://rohansharma1606:_kwB&9Q4GTZg2fA@se-6kdpi.mongodb.net/test?retryWrites=true&w=majority")
		db=client.hack_se
		posts = db.contest
		posts1 = db.problem
		posts2 = db.user
		pid = post["problem_id"]
		em = post["user"] 
		pass_key = post["pass_key"]
		total_time_limit = post["total_time_limit"]
		if (posts1.find({"problem_id":pid}) is not Null) and (posts2.find({"email":em}) is not Null):
			post_id=posts.insert_one(post)
			return jsonify({}),201
			
		client.close()
		return jsonify({}),405

@app.route('/addStudent',methods= ['POST','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def addStudent():
	if request.method == 'POST':
		post=request.json
		#name = post["name"]
		em = post["email"]
		#organization = post["organization"]
		#password = post["password"]
		client = pymongo.MongoClient("mongodb+srv://rohansharma1606:_kwB&9Q4GTZg2fA@se-6kdpi.mongodb.net/test?retryWrites=true&w=majority")
		db=client.hack_se
		posts = db.student
		if posts.find({"email": em}) is None:		
			post_id = posts.insert_one(post)
			return jsonify({}),201
		
		client.close()
		
	else:
		return jsonify({}),405
		
		

@app.route('/addUser',methods= ['POST','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def addUser():
	if request.method == 'POST':
		post=request.json
		name = post["name"]
		em = post["email"]
		organization = post["organization"]
		password = post["password"]
		client = pymongo.MongoClient("mongodb+srv://rohansharma1606:_kwB&9Q4GTZg2fA@se-6kdpi.mongodb.net/test?retryWrites=true&w=majority")
		db=client.hack_se
		posts = db.user
		if posts.find({"email": em}) is None:		
			post_id = posts.insert_one(post)
			return "added"
		else:
			return "user exists"
		
		client.close()
		
	else:
		return jsonify({}),405
'''	
@app.route('/getProblemDescription',methods= ['GET','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def getProblemDescription():
		if request.method == 'GET':
			client = pymongo.MongoClient("mongodb+srv://rohansharma1606:_kwB&9Q4GTZg2fA@se-6kdpi.mongodb.net/test?retryWrites=true&w=majority")
			db=client.hack_se
			posts = db.problem
			pid=request.args.get('problem_id',type=str)
			ab=posts.find({"problem_id":pid})
            return "ab"
		else:
			return jsonify({}),405

'''
if __name__ == '__main__':
	app.run(debug=True)
