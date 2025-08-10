# ❌ This script deletes data but logs nothing
import os

def delete_user_data(user_id):
    file_path = f"./{user_id}.txt"
    if os.path.exists(file_path):
        os.remove(file_path)  # silently delete
        # No log, no audit trail

delete_user_data("user123")
