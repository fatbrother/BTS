from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from web3 import Web3
import json
from os import path

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'highly_secret_key'

db = SQLAlchemy(app)
jwt = JWTManager(app)

# Web3 setup (assuming local Ethereum node)
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
# Load contract ABI and bytecode
def load_contract_interface():
    with open('artifacts/contracts/ConcertTickets.sol/ConcertTickets.json') as f:
        contract_json = json.load(f)
        return contract_json['abi'], contract_json['bytecode']

abi, bytecode = load_contract_interface()

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    address = db.Column(db.String(42), unique=True, nullable=False)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    start_time = db.Column(db.Integer, nullable=False)
    end_time = db.Column(db.Integer, nullable=False)
    total_tickets = db.Column(db.Integer, nullable=False)
    introduction = db.Column(db.String(500), nullable=True)
    image_url = db.Column(db.String(200), nullable=True)
    location = db.Column(db.String(200), nullable=True)
    contract_address = db.Column(db.String(42), nullable=False)

# Initialize DB
def create_tables():
    db.create_all()

@app.before_request
def initialize():
    create_tables()

# test api is alive
@app.route('/hello', methods=['GET'])
def hello():
    return 'hello world', 200

# User registration and login
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    address = data.get('address')
    if User.query.filter_by(address=address).first():
        return jsonify({'msg': 'Address already registered'}), 400
    user = User(username='User_' + address[-4:],  # Simple username generation
                address=address)
    db.session.add(user)
    db.session.commit()
    return jsonify({'msg': 'User registered'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    address = data.get('address')
    if not address:
        return jsonify({'msg': 'Missing address'}), 400
    if not User.query.filter_by(address=address).first():
        return jsonify({'msg': 'User not identified'}), 404
    # Create JWT token
    token = create_access_token(identity=address)
    return jsonify({'access_token': token}), 200

# Helper: get current user model
def get_current_user():
    identity = get_jwt_identity()
    return User.query.filter_by(address=identity).first()

# Deploy a new event
# Client must sign the deployment transaction locally and send raw signed tx data
@app.route('/holdEvent', methods=['POST'])
def hold_event():
    data = request.get_json()
    signed_tx = data.get('signedTx')
    name = data.get('eventName')
    start_time = int(data.get('startTime'))
    end_time = int(data.get('endTime'))
    introduction = data.get('introduction', '')
    image_url = data.get('image', '')
    location = data.get('location', '')
    total_tickets = int(data.get('totalTickets'))

    if not signed_tx:
        return jsonify({'msg': 'Missing signedTx'}), 400
    # Broadcast raw transaction
    try:
        tx_hash = w3.eth.send_raw_transaction(bytes.fromhex(signed_tx))
        receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    except Exception as e:
        return jsonify({'msg': f'Transaction failed: {str(e)}'}), 400
    # Save event meta if deployment
    contract_address = receipt.contractAddress
    # To get constructor args, client should include event metadata
    event = Event(name=name,
                  start_time=start_time,
                  end_time=end_time,
                  total_tickets=total_tickets,
                  introduction=introduction,
                  image_url=image_url,
                  location=location,
                  contract_address=contract_address)
    db.session.add(event)
    db.session.commit()
    return jsonify({'contractAddress': contract_address}), 201

# Get all events
@app.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    event_list = []
    for event in events:
        event_list.append({
            'id': event.id,
            'name': event.name,
            'start_time': event.start_time,
            'end_time': event.end_time,
            'total_tickets': event.total_tickets,
            'introduction': event.introduction,
            'image_url': event.image_url,
            'location': event.location,
            'contract_address': event.contract_address,
        })
    return jsonify(event_list), 200

# Get event details
@app.route('/event/<int:event_id>', methods=['GET'])
def get_event(event_id):
    event = Event.query.get_or_404(event_id)
    event_details = {
        'id': event.id,
        'name': event.name,
        'start_time': event.start_time,
        'end_time': event.end_time,
        'total_tickets': event.total_tickets,
        'introduction': event.introduction,
        'image_url': event.image_url,
        'location': event.location,
        'contract_address': event.contract_address,
    }
    return jsonify(event_details), 200

# Reserve a ticket
# Client signs reserve tx locally and sends raw signed tx data
@app.route('/reserveEvent', methods=['POST'])
@jwt_required()
def reserve_event():
    user = get_current_user()
    data = request.get_json()
    signed_tx = data.get('signedTx')
    if not signed_tx:
        return jsonify({'msg': 'Missing signedTx'}), 400
    try:
        tx_hash = w3.eth.send_raw_transaction(bytes.fromhex(signed_tx))
        w3.eth.wait_for_transaction_receipt(tx_hash)
    except Exception as e:
        return jsonify({'msg': f'Transaction failed: {str(e)}'}), 400
    return jsonify({'msg': 'Reservation submitted'}), 200

# Check if user is winner (view call)
@app.route('/checkResult', methods=['GET'])
@jwt_required()
def check_result():
    user = get_current_user()
    contract_address = request.args.get('contractAddress')
    if not contract_address:
        return jsonify({'msg': 'Missing contractAddress'}), 400
    contract = w3.eth.contract(address=contract_address, abi=abi)
    try:
        is_winner = contract.functions.isWinner(user.address).call()
    except Exception as e:
        return jsonify({'msg': f'Call failed: {str(e)}'}), 400
    return jsonify({'isWinner': is_winner}), 200

def create_db(app):
    with app.app_context():
        db.create_all()
        print("Database tables created successfully.")


if __name__ == '__main__':
    if not path.exists('instance/database.db'):
        create_db(app)
    app.run(debug=True)
