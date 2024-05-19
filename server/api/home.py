from server import *


class Home:
    """
    This class represents the home API endpoints.
    """

    @staticmethod
    def contact_us(name, email, message):
        """
        Sends a contact us request to the server.
        Args:
            name (str): The name of the sender.
            email (str): The email of the sender.
            message (str): The message content.
        Returns:
            str: The response from the server.
        """
        response = requests.post(
            f"{BASE_URL}/contact/us",
            json={"name": name, "email": email, "message": message},
        )
        return response.json()["response"]

    @staticmethod
    def sign_up_volunteer(name, email, password, photo_byte_array, phone_number):
        """
        Signs up a volunteer.
        Args:
            name (str): The name of the volunteer.
            email (str): The email of the volunteer.
            password (str): The password of the volunteer.
            photo_byte_array (bytes): The photo of the volunteer as a byte array.
            phone_number (str): The phone number of the volunteer.
        Returns:
            Response: The response from the server.
        """
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
        """
        Signs up an organization.
        Args:
            name (str): The name of the organization.
            email (str): The email of the organization.
            password (str): The password of the organization.
            photo_byte_array (bytes): The photo of the organization as a byte array.
            certification_registration_byte_array (bytes): The certification/registration document of the organization as a byte array.
            annual_report_byte_array (bytes): The annual report of the organization as a byte array.
            list_of_board_members_byte_array (bytes): The list of board members of the organization as a byte array.
            phone_number (str): The phone number of the organization.
        Returns:
            dict: The response from the server.
        """
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
        """
        Logs in a user.
        Args:
            email (str): The email of the user.
            password (str): The password of the user.
        Returns:
            str: The response from the server.
        """
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={
                "email": email,
                "password": password,
            },
        )
        return response.json()["response"]
