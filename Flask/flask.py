from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Set up the Flask app and the SQLite database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

# Define the Post model for the SQLite database
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Post {self.id}>'

class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1 = db.Column(db.String(80), nullable=False)
    user2 = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'<Friend {self.id}>'

# Initialize the database with the models
with app.app_context():
    db.create_all()


# Create the /post-to-feed endpoint
@app.route('/post-to-feed', methods=['POST'])
def post_to_feed():
    data = request.get_json()

    if 'username' not in data or 'text' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    new_post = Post(username=data['username'], text=data['text'])
    db.session.add(new_post)
    db.session.commit()

    return jsonify({'message': 'Post created'}), 201

# Create the /view-post endpoint
@app.route('/view-post', methods=['POST'])
def view_post():
    data = request.get_json()

    if 'username' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    posts = Post.query.filter_by(username=data['username']).all()
    post_list = [{'username': post.username, 'text': post.text} for post in posts]

    return jsonify(post_list), 200



@app.route('/friends', methods=['POST'])
def add_friend():
    data = request.get_json()

    if 'username' not in data or 'friend' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    new_friend = Friend(user1=data['username'], user2=data['friend'])
    db.session.add(new_friend)
    db.session.commit()

    return jsonify({'message': 'Friend added'}), 201

@app.route('/view-joint-posts', methods=['POST'])
def view_joint_posts():
    data = request.get_json()

    if 'username' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    username = data['username']
    friends = Friend.query.filter((Friend.user1 == username) | (Friend.user2 == username)).all()
    friend_usernames = [f.user1 if f.user2 == username else f.user2 for f in friends]

    all_posts = Post.query.filter((Post.username == username) | (Post.username.in_(friend_usernames))).all()
    post_list = [{'username': post.username, 'text': post.text} for post in all_posts]

    return jsonify(post_list), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
