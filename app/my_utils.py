import qrcode
import os

QR_CODE_FOLDER = "static/qrcodes"

def generate_qr_code(event_id: int) -> str:
    """
    Generate a QR code for a given event_id.
    """
    data = f"http://localhost:8000/checkin/{event_id}"
    img = qrcode.make(data)
    file_path = os.path.join(QR_CODE_FOLDER, f"event_{event_id}.png")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    img.save(file_path)
    return file_path
