from app_lib import app  # Import the app instance from the package
from flask import request, render_template
from . import fetcher, feed_parser  # Import other modules
from django.core.validators import URLValidator
from typing import *

val = URLValidator()


@app.route("/")
def index() -> render_template:
    form = fetcher.RSSForm()
    return render_template("index.html", form=form)


@app.route("/fetch", methods=["post"])
def fetch_feed() -> render_template:
    url = request.form.get("form-input")
    try:
        val(url)
    except Exception as e:
        error_feed = feed_parser.parse_feed(True, f"Unexpected error occured: {str(e)}")
        return render_template(
            "results.html",
            items=error_feed,
            last_updated=feed_parser.get_last_update_time(),
        )

    results_xml = fetcher.fetch(url)
    feed_items = feed_parser.parse_feed(*results_xml)

    if feed_items[1]:
        return render_template(
            "results.html",
            error_feed=feed_items[0],
            last_updated=feed_parser.get_last_update_time(),
        )

    return render_template(
        "results.html",
        items=feed_items[0],
        last_updated=feed_parser.get_last_update_time(),
    )
