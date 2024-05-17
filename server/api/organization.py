from server import *


class Organization:
    def get_trainings(self, uid):
        response = requests.get(
            f"{BASE_URL}/org/training",
            headers={"uid": uid},
        )
        print(response.json()["response"][1])
        return response.json()["response"]

    def create_training(self, uid, training_data):
        response = requests.post(
            f"{BASE_URL}/org/training",
            headers={"uid": uid},
            json=training_data,
        ).json()
        return response["response"]

    def update_training(
        self,
        uid,
        trainingID,
    ):
        response = requests.put(
            f"{BASE_URL}/org/training/",
            headers={"uid": uid},
            json={"trainingID": trainingID},
        ).json()
        return response["response"]

    def delete_training(self, uid, trainingID):
        response = requests.delete(
            f"{BASE_URL}/org/training/",
            headers={"uid": uid},
            json={"trainingID": trainingID},
        ).json()
        return response["response"]

    def get_volunteer_opportunities(self, uid):
        response = requests.get(
            f"{BASE_URL}/org/jobs",
            headers={"uid": uid},
        ).json()
        return response["response"]

    def create_volunteer_opportunity(self, uid, volunteer_data):
        response = requests.post(
            f"{BASE_URL}/org/jobs",
            headers={"uid": uid},
            json=volunteer_data,
        ).json()
        return response["response"]

    def update_volunteer_opportunity(self, uid, volunteerID, volunteer_data):
        response = requests.put(
            f"{BASE_URL}/org/jobs/{volunteerID}",
            headers={"uid": uid},
            json=volunteer_data,
        ).json()
        return response["response"]

    def delete_volunteer_opportunity(self, uid, volunteerID):
        response = requests.delete(
            f"{BASE_URL}/org/jobs/{volunteerID}",
            headers={"uid": uid},
        ).json()
        return response["response"]

    def get_applicants(self, uid, opportunityID):
        response = requests.get(
            f"{BASE_URL}/org/applicants/{opportunityID}",
            headers={"uid": uid},
        ).json()
        return response["response"]


# The routes in the Flask app are already well-defined, no changes needed there.
