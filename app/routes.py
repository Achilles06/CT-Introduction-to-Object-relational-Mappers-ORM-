from flask import request, jsonify, current_app as app
from .models import Member, WorkoutSession, db, MemberSchema, WorkoutSessionSchema

member_schema = MemberSchema()
members_schema = MemberSchema(many=True)
workout_session_schema = WorkoutSessionSchema()
workout_sessions_schema = WorkoutSessionSchema(many=True)

@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()
    new_member = Member(name=data['name'], email=data['email'])
    db.session.add(new_member)
    db.session.commit()
    return member_schema.jsonify(new_member), 201

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    member = Member.query.get_or_404(id)
    return member_schema.jsonify(member)

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    member = Member.query.get_or_404(id)
    data = request.get_json()
    member.name = data['name']
    member.email = data['email']
    db.session.commit()
    return member_schema.jsonify(member)

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = Member.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    return jsonify({"message": "Member deleted successfully"})

@app.route('/workouts', methods=['POST'])
def add_workout():
    data = request.get_json()
    new_workout = WorkoutSession(member_id=data['member_id'], date=data['date'], duration=data['duration'])
    db.session.add(new_workout)
    db.session.commit()
    return workout_session_schema.jsonify(new_workout), 201

@app.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id):
    workout = WorkoutSession.query.get_or_404(id)
    data = request.get_json()
    workout.date = data['date']
    workout.duration = data['duration']
    db.session.commit()
    return workout_session_schema.jsonify(workout)

@app.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = WorkoutSession.query.get_or_404(id)
    return workout_session_schema.jsonify(workout)

@app.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = WorkoutSession.query.get_or_404(id)
    db.session.delete(workout)
    db.session.commit()
    return jsonify({"message": "Workout session deleted successfully"})

@app.route('/members/<int:member_id>/workouts', methods=['GET'])
def get_member_workouts(member_id):
    workouts = WorkoutSession.query.filter_by(member_id=member_id).all()
    return workout_sessions_schema.jsonify(workouts)
