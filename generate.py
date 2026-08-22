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
        "bio": "I specialize in full stack website development , web scraping , data visualization , 2D games and custom desktop applications. ",
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
                "description": "I develop custom desktop applications designed around your specific business needs. From data management and automation tools to reporting systems and productivity software, I create reliable applications that improve efficiency and simplify your daily workflow.",
                "price": "From 30$",
            },
            {
                "title": "2D games",
                "description": "I create engaging 2D games using Python, Pygame, and Arcade. From simple arcade-style games to more advanced projects, I build interactive gameplay, smooth controls, scoring systems, animations, and user-friendly interfaces.",
                "price": "From 100$",
            },
        ],
        "website_development": [
            {
                "title": "Portfolio ",
                "description": "A neat portfolio website for an individual or a business",
                "price": "From 60$",
                "duration": "2-7 days",
            },
            {
                "title": "Advanced ",
                "description": " Complex and professional websites for financial services, e-commerce businesses, and booking-based platforms. I create secure, user-friendly experiences that help customers manage accounts, purchase products, schedule appointments, and complete transactions with ease.  ",
                "price": "From 200$",
                "duration": "10-40 days",
            },
            {
                "title": "API integrations",
                "description": "Seamlessly connect your website or application with third-party services using secure and reliable API integrations. From payment gateways and social media platforms to maps, booking systems, and custom business tools, I’ll ensure your systems communicate efficiently and deliver a smooth user experience. ",
                "price": "From 200$",
                "duration": "10-40 days",
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


def generate_freelance_projects_page():
    env = Environment(loader=FileSystemLoader("./"))
    template = env.get_template("freelance_projects.jinja")
    context = {} | base_context
    context["projects"] = PROJECTS
    with open("freelance_projects.html", "w") as f:
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
generate_freelance_projects_page()
generate_paid_projects_page()
generate_bugs_page()
