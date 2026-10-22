from flask import Flask, request, jsonify

app = Flask(__name__)

# قاعدة بيانات الأجهزة المسموحة وأكوادها
REGISTERED_DEVICES = {
    "3430fb8bfb44a375": "778899"
}

@app.route('/verify', methods=['POST'])
def verify_activation():
    data = request.get_json() or {}
    device_id = data.get('deviceId')
    otp_code = data.get('otp')
    
    print(f"استلام طلب تفعيل من الجهاز: {device_id} بالرمز: {otp_code}")
    
    if device_id in REGISTERED_DEVICES and REGISTERED_DEVICES[device_id] == otp_code:
        return jsonify({"status": "success", "message": "التفعيل ناجح"}), 200
    else:
        return jsonify({"status": "error", "message": "رمز التفعيل غير صحيح أو الجهاز غير مسجل"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
