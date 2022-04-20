from flask import Flask, jsonify, request
heart_info_app = Flask(__name__)
records = [
    {
        "Heart_ID": "0000",
        "Date": "4/20/2022",
        "Heart_Rate": "99"
    },
    {
        "Heart_ID": "0001",
        "Date": "4/20/2022",
        "Heart_Rate": "100"
    }
]
@heart_info_app.route('/records', methods=['GET'])
def getRecords():
    return jsonify(records)

@heart_info_app.route('/records', methods=['POST'])
def add_record():
    record = request.get_json()
    records.append(record)
    return {'id': len(records)}, 200

@heart_info_app.route('/records/<Heart_ID>', methods=['GET'])
def read_id(Heart_ID):
    heart = record.query.get(Heart_ID)
    result = record.dump(heart)
    return record.jsonfiy(result)

@heart_info_app.route('/records/<int:index>', methods=['DELETE'])
def delete_record(index):
    records.pop(index)
    return 'None', 200

if __name__ == "__main__":
    heart_info_app.run(host = "0.0.0.0", port= 5000, debug=True)

