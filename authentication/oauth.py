from social_core.backends.oauth import BaseOAuth2


class IonOauth2(BaseOAuth2):
    name = "ion"
    AUTHORIZATION_URL = "https://ion.tjhsst.edu/oauth/authorize"
    ACCESS_TOKEN_URL = "https://ion.tjhsst.edu/oauth/token"
    ACCESS_TOKEN_METHOD = "POST"
    EXTRA_DATA = [("refresh_token", "refresh_token", True), ("expires_in", "expires")]

    def get_scope(self):
        print("Get scope")
        return ["read"]

    def get_user_details(self, response):
        print("Get user details, response:", response)
        profile = self.get_json("https://ion.tjhsst.edu/api/profile", params={"access_token": response["access_token"]})
        print("Profile:", profile)
        # fields used to populate/update User model
        return {
            "id": profile["id"],
            "username": profile["ion_username"],
            "first_name": profile["first_name"],
            "middle_name": profile["middle_name"],
            "last_name": profile["last_name"],
            "full_name": profile["full_name"],
            "email": profile["tj_email"],
            "is_student": profile["is_student"],
            "is_teacher": profile["is_teacher"],
            "graduation_year": int(profile["graduation_year"])
        }

    def get_user_id(self, details, response):
        print("Get user id")
        return details["id"]