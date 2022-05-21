from bookmarks.models.tables.visits import Visit
from sqlalchemy import extract
from datetime import (
    datetime,
    timedelta
)


def monthly_stats(current_month, bookmark_id):

    months = [
        "jan",
        "feb",
        "mar",
        "apr",
        "may",
        "jun",
        "jul",
        "aug",
        "sep",
        "oct",
        "nov",
        "dec"
    ]

    if isinstance(current_month, str):
        current_month = current_month[0:3].lower()
        current_month = months.index(current_month)
    elif isinstance(current_month, int):
        current_month = current_month - 1
    else:
        return {
            "error":
            "Input a valid month. str with 3 characters (jan, fev, mar...) or int value (1=jan, 2=feb, 3=mar...)"
        }

    data = []

    for i in range(current_month, current_month - 12, -1):
        month = (months.index(months[i]) + 1)
        visit = Visit.query.filter(
            extract('month', Visit.visiting_hours) == month,
            Visit.bookmark_id == bookmark_id
        ).all()
        data.append(
            {
                "month": months[i],
                "number_visits": len(visit)
            }
        )
    return data


def weekly_stats(bookmark_id):
    today = datetime.today()
    correction_value = int(today.strftime("%u"))
    week = []

    if correction_value == 7:
        week.append(today)
        week.append(today + timedelta(6))
    else:
        week.append(
            today - timedelta(int(today.strftime("%u")))
        )
        week.append(
            today + timedelta(6 - int(today.strftime("%u")))
        )

    weeks = []

    for i in range(12):
        visit = Visit.query.filter(
            Visit.visiting_hours.between(
                week[0], week[1]
            ),
            Visit.bookmark_id == bookmark_id
        ).all()
        weeks.append(
            {
                "week": week[0].strftime("%U"),
                "number_visits": len(visit)
            }
        )
        week[0] = week[0] - timedelta(7)
        week[1] = week[1] - timedelta(7)

    return weeks


def last_days_stats(days, bookmark_id):
    date = datetime.today()
    last_days = []

    for i in range(days):
        visit = Visit.query.filter(
            extract("month", Visit.visiting_hours) == date.strftime("%m"),
            extract("day", Visit.visiting_hours) == date.strftime("%d"),
            Visit.bookmark_id == bookmark_id
        ).all()
        if days == 7:
            last_days.append(
                {
                    "day": date.strftime("%a"),
                    "number_visits": len(visit)
                }
            )
        else:
            last_days.append(
                {
                    "day": date.strftime("%x"),
                    "number_visits": len(visit)
                }
            )
        date = date - timedelta(1)

    return last_days
