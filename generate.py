from jinja2 import Template, FileSystemLoader, Environment

from work import PROJECTS, FREELANCE_WORK
from critters import CRITTERS


skills = {
    "backend": ["Python", "SQL", "Django", "Bash", "C"],
    "frontend": ["Javascript", "HTML", "CSS", "Jquery", "Bootstrap"],
    "cloud": ["AWS s3 storage", "Cloudinary", "Koyeb hosting configs", "Docker"],
    "Web scraping": ["Selenium", "Playwright", "Requests"],
}

contact_information = {
    "email": "letingvictorkipkemboi@gmail.com",
    "phone_number": "+254 712 553 793",
    "github": "https://github.com/victhepythonista",
    "linkedin": "https://www.linkedin.com/in/victor-kipkemboi-leting-b58963187?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B5AFyhMPWT6elwrzcmQ05Mw%3D%3D",
    "sololearn": "https://www.sololean.com/en/profile/16972905",
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

base_context = {"current_page": ""}


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
        "bio": "I specialize in full stack website development , web scraping ,  custom desktop applications , data visualization , graphics design , pixel art and  2D games. ",
    } | base_context
    with open("index.html", "w") as f:
        f.write(template.render(context))
        print("Template generated ")


def generate_contacts_page():
    env = Environment(loader=FileSystemLoader("./"))
    template = env.get_template("contact.jinja")
    context = {} | base_context | {"contact_info": contact_information}
    with open("contact.html", "w") as f:
        f.write(template.render(context))
        print("contacts.html generated ")


def generate_services_page():
    env = Environment(loader=FileSystemLoader("./"))
    template = env.get_template("services.jinja")
    context = {} | base_context
    context["services"] = {
        "app_development": [
            {
                "title": "Custom apps ",
                "description": "Desktop tools , dashboards , trackers , counters ....",
                "price": "From 30$",
            },
            {
                "title": "2D games",
                "description": "Simulations and 2D games using Python, Pygame, and Arcade ",
                "price": "From 100$",
            },
        ],
        "website_development": [
            {
                "title": "Portfolio <br> (from 15$)",
                "description": "A neat portfolio website for an individual or a business",
                "duration": "2-7 days",
            },
            {
                "title": "Advanced <br> (from 200$)",
                "description": " Complex and professional websites for financial services, e-commerce businesses,  booking-based platforms ..etc ",
                "duration": "10-40 days",
            },
            {
                "title": "API integrations <br>  (from 80$)",
                "description": "Seamlessly connect your website or application with third-party services ",
                "duration": "2-20 days",
            },
        ],
    }
    context["current_page"] = "services"
    with open("services.html", "w") as f:
        f.write(template.render(context))
        print("Template generated ")

    pass


def generate_skills_page():
    env = Environment(loader=FileSystemLoader("./"))
    template = env.get_template("skillset.jinja")
    context = {
        "skills": skills,
    } | base_context
    with open("skillset.html", "w") as f:
        f.write(template.render(context))
        print("Template generated ")


def generate_personal_projects_page():
    env = Environment(loader=FileSystemLoader("./"))
    template = env.get_template("personal_projects.jinja")
    context = {} | base_context
    context["projects"] = PROJECTS
    with open("personal_projects.html", "w") as f:
        f.write(template.render(context))
        print("Freelance projects page  generated ")


def generate_paid_projects_page():
    env = Environment(loader=FileSystemLoader("./"))
    template = env.get_template("paid_projects.jinja")
    context = {} | base_context
    context["paid_projects"] = FREELANCE_WORK
    with open("paid_projects.html", "w") as f:
        f.write(template.render(context))
        print("Paid projects page generated ")


def generate_bugs_page():
    env = Environment(loader=FileSystemLoader("./"))
    template = env.get_template("bugs.jinja")
    context = {} | base_context
    context["critters"] = CRITTERS
    with open("bugs.html", "w") as f:
        f.write(template.render(context))
        print("bugs page generated ")


generate_index_page()
generate_services_page()
generate_skills_page()
generate_contacts_page()
generate_personal_projects_page()
generate_paid_projects_page()
generate_bugs_page()
