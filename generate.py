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
        "bio": "Apart from my obsession with coding I love anything to do with astronomy , palaentology ,astrophysics , nature , geography , biology,chemistry and anthropology . I enjoy star gazing , exploring nature and reading a good book . ",
    } | base_context
    context["current_page"] = "home"
    with open("index.html", "w") as f:
        f.write(template.render(context))
        print("Template generated ")

    pass


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
                "title": "Portfolio website ",
                "description": "A neat portfolio website for an individual or a business",
                "price": "From 60$",
                "duration": "2-7 days",
            },
            {
                "title": "Finance/Ecommerce/Booking websites",
                "description": " professional websites for financial services, e-commerce businesses, and booking-based platforms. I create secure, user-friendly experiences that help customers manage accounts, purchase products, schedule appointments, and complete transactions with ease.  ",
                "price": "From 200$",
                "duration": "10-40 days",
            },
            {
                "title": "API integrtions",
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
    pass


def generate_freelance_projects_page():
    pass


def generate_paid_projects_page():
    pass


generate_index_page()
generate_services_page()
