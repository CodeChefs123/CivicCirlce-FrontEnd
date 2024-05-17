from server import *


class Home:
    @staticmethod
    def contact_us(name, email, message):
        response = requests.post(
            f"{BASE_URL}/contact/us",
            json={"name": name, "email": email, "message": message},
        )
        return response.json()["response"]

    @staticmethod
    def sign_up_volunteer(name, email, password, photo_byte_array, phone_number):
        response = requests.post(
            f"{BASE_URL}/auth/signup",
            json={
                "email": email,
                "password": password,
                "photo": photo_byte_array,
                "phoneNumber": phone_number,
                "name": name,
            },
        )
        return response

    @staticmethod
    def sign_up_organization(
        name,
        email,
        password,
        photo_byte_array,
        certification_registration_byte_array,
        annual_report_byte_array,
        list_of_board_members_byte_array,
        phone_number,
    ):
        response = requests.post(
            f"{BASE_URL}/auth/org/signup",
            json={
                "email": email,
                "password": password,
                "photo": photo_byte_array,
                "phoneNumber": phone_number,
                "name": name,
                "certificateRegistrationByte8Array": certification_registration_byte_array,
                "annualReportByte8Array": annual_report_byte_array,
                "listBoardMembersByte8Array": list_of_board_members_byte_array,
            },
        )
        return response.json()

    @staticmethod
    def login(email, password):
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={
                "email": email,
                "password": password,
            },
        )
        return response.json()["response"]
