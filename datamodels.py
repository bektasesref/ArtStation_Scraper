class Artist:
    def __init__(self, data):
        self.id = data.get("id")
        self.username = data.get("username")
        self.large_avatar_url = data.get("large_avatar_url")
        self.small_cover_url = data.get("small_cover_url")
        self.is_staff = data.get("is_staff")
        self.pro_member = data.get("pro_member")
        self.artstation_profile_url = data.get("artstation_profile_url")
        self.likes_count = data.get("likes_count")
        self.followers_count = data.get("followers_count")
        self.available_full_time = data.get("available_full_time")
        self.available_contract = data.get("available_contract")
        self.available_freelance = data.get("available_freelance")
        self.location = data.get("location")
        self.is_plus_member = data.get("is_plus_member")
        self.is_studio_account = data.get("is_studio_account")
        self.is_school_account = data.get("is_school_account")
        self.project_views_count = data.get("project_views_count")
        self.full_name = data.get("full_name")
        self.headline = data.get("headline")
        self.followed = data.get("followed")
        self.following_back = data.get("following_back")
        self.sample_projects = [SampleProject(project_data) for project_data in data.get("sample_projects")]
        self.skills = [Skill(skill_data) for skill_data in data.get("skills")]
        self.softwares = [Software(software_data) for software_data in data.get("softwares")]

class SampleProject:
    def __init__(self, data):
        self.id = data.get("id")
        self.smaller_square_cover_url = data.get("smaller_square_cover_url")
        self.url = data.get("url")
        self.title = data.get("title")
        self.adult_content = data.get("adult_content")

class Skill:
    def __init__(self, data):
        self.skill_name = data.get("skill_name")

class Software:
    def __init__(self, data):
        self.software_name = data.get("software_name")