from jinja2 import Template, FileSystemLoader, Environment

from work import PROJECTS, FREELANCE_WORK
from critters import CRITTERS


skills = {
    "backend": ["Python", "SQL", "Django", "Bash", "C"],
    "frontend": ["Javascript", "HTML", "CSS", "Jquery", "Bootstrap"],
}

contact_information = {
    "email": "letingvictorkipkemboi@gmail.com",
    "phone_number": "+254 712 553 793",
    "github": "https://github.com/victhepythonista",
    "linkedin": "https://www.linkedin.com/in/victor-kipkemboi-leting-b58963187?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B5AFyhMPWT6elwrzcmQ05Mw%3D%3D",
    "sololearn": "https://www.sololearn.com/en/profile/16972905",
    "whatsapp": "+254 712 553 793",
    "leetcode": "https://leetcode.com/u/victhepythonista",
    "codewars": "https://www.codewars.com/users/victhepythonista",
}

about_me = {
    "long": """Chess | Space | Nature | Art""",
    "short": """I specialize in full stack website development , web scraping , data visualization , 2D games and custom desktop applications. """,
}

context = {
    "name": "Victor Kipkemboi",
    "about_me": about_me,
    "projects": PROJECTS,
    "freelance_work": FREELANCE_WORK,
    "skills": skills,
    "contact_info": contact_information,
    "critters": CRITTERS,
}


def generate_portfolio_page(raw_data_file, context):
    print("Generating .....")
    env = Environment(loader=FileSystemLoader("content"))
    template = env.get_template(raw_data_file)
    with open("index.html", "w") as f:
        f.write(template.render(context))
        print("Template generated ")


def generate_index_page():
    env = Environment(loader=FileSystemLoader("./"))
    template = env.get_template("index.jinja")
    context = {
        "bio": "Apart from my obsession with coding I love anything to do with astronomy , palaentology ,astrophysics , nature , geography , biology,chemistry and anthropology . I enjoy star gazing , exploring nature and reading a good book . ",
    }
    with open("index.html", "w") as f:
        f.write(template.render(context))
        print("Template generated ")

    pass


def generate_skills_page():
    pass


def generate_freelance_projects_page():
    pass


def generate_paid_projects_page():
    pass


generate_index_page()
