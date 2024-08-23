from flask import render_template
from se_models import SummerSchool


schools = {
    2021: {
        "name": "Летняя школа 2021",
        "full_name": "Летняя проектная онлайн-школа программирования для обучающихся СПбГУ (<strong>2021</strong>, онлайн).",
        "description": "Школа проводилась с <strong>12-го июля по 6-е августа</strong>. 12 июля в 12:00 прошло открытие школы и презентация проектов. 6 августа были проведены презентации результатов проектов, подведение итогов и закрытие школы.",
        "href": "summer_school_2021",
    },
    2022: {
        "name": "Летняя школа 2022",
        "full_name": "Летняя проектная онлайн-школа программирования для обучающихся СПбГУ (<strong>2022</strong>, онлайн).",
        "description": "Школа проводилась с <strong>4 по 30 июля</strong>. 4 июля в 12:00 прошло открытие школы и презентация проектов. 30 июля были проведены презентации результатов проектов, подведение итогов и закрытие школы.",
        "href": "summer_school_2022",
    },
    2024: {
        "name": "Летняя школа 2024",
        "full_name": "Летняя проектная онлайн-школа программирования для обучающихся СПбГУ (<strong>2024</strong>, онлайн).",
        "description": "Школа проводилась с <strong>8 июля по 3 августа</strong>. 8 июля в 12:00 прошло открытие школы и презентация проектов. 2 августа были проведены презентации результатов проектов, подведение итогов и закрытие школы.",
        "href": "summer_school_2024",
    },
}


def create_summer_school_view(year: int):
    def summer_school():
        projects = SummerSchool.query.filter_by(year=year).all()

        return render_template(
            "summer_school.html", projects=projects, school=schools[year]
        )
    
    # flask makes function identification by name 
    summer_school.__name__ = "summer_school_" + str(year)
    
    return summer_school


def summer_school_list():
    return render_template("summer_school_list.html", schools=schools)
