from server import *


class Organization:
    def get_trainings(self, uid):
        """
        Get the trainings for a specific organization.
        Args:
            uid (str): The organization's unique identifier.
        Returns:
            list: A list of training objects.
        """
        response = requests.get(
            f"{BASE_URL}/org/training",
            headers={"uid": uid},
        )
        return response.json()["response"]

    def create_training(self, uid, training_data):
        """
        Create a new training for an organization.
        Args:
            uid (str): The organization's unique identifier.
            training_data (dict): The data for the new training.
        Returns:
            dict: The response from the server.
        """
        response = requests.post(
            f"{BASE_URL}/org/training",
            headers={"uid": uid},
            json=training_data,
        ).json()
        return response["response"]

    def update_training(self, uid, trainingID):
        """
        Update an existing training for an organization.
        Args:
            uid (str): The organization's unique identifier.
            trainingID (str): The ID of the training to update.
        Returns:
            dict: The response from the server.
        """
        response = requests.put(
            f"{BASE_URL}/org/training/",
            headers={"uid": uid},
            json={"trainingID": trainingID},
        ).json()
        return response["response"]

    def delete_training(self, uid, trainingID):
        """
        Delete a training from an organization.
        Args:
            uid (str): The organization's unique identifier.
            trainingID (str): The ID of the training to delete.
        Returns:
            dict: The response from the server.
        """
        response = requests.delete(
            f"{BASE_URL}/org/training/",
            headers={"uid": uid},
            json={"trainingID": trainingID},
        ).json()
        return response["response"]

    def get_volunteer_opportunities(self, uid):
        """
        Get the volunteer opportunities for a specific organization.
        Args:
            uid (str): The organization's unique identifier.
        Returns:
            list: A list of volunteer opportunity objects.
        """
        response = requests.get(
            f"{BASE_URL}/org/jobs",
            headers={"uid": uid},
        ).json()
        return response["response"]

    def create_volunteer_opportunity(self, uid, volunteer_data):
        """
        Create a new volunteer opportunity for an organization.
        Args:
            uid (str): The organization's unique identifier.
            volunteer_data (dict): The data for the new volunteer opportunity.
        Returns:
            dict: The response from the server.
        """
        response = requests.post(
            f"{BASE_URL}/org/jobs",
            headers={"uid": uid},
            json=volunteer_data,
        ).json()
        return response["response"]

    def update_volunteer_opportunity(self, uid, volunteerID, volunteer_data):
        """
        Update an existing volunteer opportunity for an organization.
        Args:
            uid (str): The organization's unique identifier.
            volunteerID (str): The ID of the volunteer opportunity to update.
            volunteer_data (dict): The updated data for the volunteer opportunity.
        Returns:
            dict: The response from the server.
        """
        response = requests.put(
            f"{BASE_URL}/org/jobs/{volunteerID}",
            headers={"uid": uid},
            json=volunteer_data,
        ).json()
        return response["response"]

    def delete_volunteer_opportunity(self, uid, volunteerID):
        """
        Delete a volunteer opportunity from an organization.
        Args:
            uid (str): The organization's unique identifier.
            volunteerID (str): The ID of the volunteer opportunity to delete.
        Returns:
            dict: The response from the server.
        """
        response = requests.delete(
            f"{BASE_URL}/org/jobs/{volunteerID}",
            headers={"uid": uid},
        ).json()
        return response["response"]

    def get_applicants(self, uid, opportunityID):
        """
        Get the applicants for a specific volunteer opportunity.
        Args:
            uid (str): The organization's unique identifier.
            opportunityID (str): The ID of the volunteer opportunity.
        Returns:
            list: A list of applicant objects.
        """
        response = requests.get(
            f"{BASE_URL}/org/applicants/{opportunityID}",
            headers={"uid": uid},
        ).json()
        return response["response"]
