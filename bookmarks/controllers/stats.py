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


