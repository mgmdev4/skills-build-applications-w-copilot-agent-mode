from bson import ObjectId
from datetime import timedelta

test_data = {
    "users": [
        {"_id": ObjectId(), "username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
        {"_id": ObjectId(), "username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
        {"_id": ObjectId(), "username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
        {"_id": ObjectId(), "username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "crashoverridepassword"},
        {"_id": ObjectId(), "username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
    ],
    "teams": [
        {"_id": ObjectId(), "name": "Blue Team", "members": []},
        {"_id": ObjectId(), "name": "Gold Team", "members": []},
    ],
    "activities": [
        {"_id": ObjectId(), "user": None, "activity_type": "Cycling", "duration": timedelta(hours=1).total_seconds()},
        {"_id": ObjectId(), "user": None, "activity_type": "Crossfit", "duration": timedelta(hours=2).total_seconds()},
        {"_id": ObjectId(), "user": None, "activity_type": "Running", "duration": timedelta(hours=1, minutes=30).total_seconds()},
        {"_id": ObjectId(), "user": None, "activity_type": "Strength", "duration": timedelta(minutes=30).total_seconds()},
        {"_id": ObjectId(), "user": None, "activity_type": "Swimming", "duration": timedelta(hours=1, minutes=15).total_seconds()},
    ],
    "leaderboard": [
        {"_id": ObjectId(), "team": None, "score": 100},
        {"_id": ObjectId(), "team": None, "score": 90},
    ],
    "workouts": [
        {"_id": ObjectId(), "name": "Cycling Training", "description": "Training for a road cycling event"},
        {"_id": ObjectId(), "name": "Crossfit", "description": "Training for a crossfit competition"},
        {"_id": ObjectId(), "name": "Running Training", "description": "Training for a marathon"},
        {"_id": ObjectId(), "name": "Strength Training", "description": "Training for strength"},
        {"_id": ObjectId(), "name": "Swimming Training", "description": "Training for a swimming competition"},
    ],
}

# Update references for activities and leaderboard to use valid ObjectId values
user_ids = [user['_id'] for user in test_data['users']]
team_ids = [team['_id'] for team in test_data['teams']]

for i, activity in enumerate(test_data['activities']):
    activity['user'] = user_ids[i % len(user_ids)]

for i, entry in enumerate(test_data['leaderboard']):
    entry['team'] = team_ids[i % len(team_ids)]