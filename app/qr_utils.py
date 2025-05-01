import qrcode
import os
from fastapi.responses import FileResponse
from fastapi import HTTPException

# Define the folder where QR codes will be saved
QR_CODE_FOLDER = "static/qrcodes"

def generate_qr_code(event_id: int) -> str:
    """
    Generate a QR code for a given event_id.

    Args:
    - event_id (int): The ID of the event for which QR code is being generated.

    Returns:
    - file_path (str): Path to the generated QR code image file.
    """
    # Data to be encoded in the QR code (URL to check-in)
    data = f"http://localhost:8000/checkin/{event_id}"
    
    # Generate QR code image
    img = qrcode.make(data)
    
    # Define the file path to save the QR code
    file_path = os.path.join(QR_CODE_FOLDER, f"event_{event_id}.png")
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Save the QR code image
    img.save(file_path)
    
    return file_path

def get_qr_code(event_id: int):
    """
    Retrieve the generated QR code for a specific event by its ID.

    Args:
    - event_id (int): The ID of the event to get the QR code for.

    Returns:
    - FileResponse: The QR code image as a response.
    """
    file_path = generate_qr_code(event_id)
    
    # Check if file exists
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="QR code not found.")
    
    return FileResponse(file_path)
