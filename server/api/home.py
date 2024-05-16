from server import *


class Home:
    @staticmethod
    def contact_us(name, email, message):
        response = requests.post(
            "http://localhost:3000/contact/us",
            json={"name": name, "email": email, "message": message},
        )
        return response.json()["response"]

    @staticmethod
    def sign_up_volunteer(name, email, password, photo_byte_array, phone_number):
        response = requests.post(
            "http://localhost:3000/auth/signup",
            json={
                "email": email,
                "password": password,
                "photo": base64.b64encode(photo_byte_array).decode("utf-8"),
                "phoneNumber": phone_number,
                "name": name,
            },
        )
        return response
