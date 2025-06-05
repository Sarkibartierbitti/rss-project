from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from typing import *
import requests


class RSSForm(FlaskForm):
    url = StringField(
        "RSS URL", validators=[DataRequired(), URL(message="Invalid URL format")]
    )
    submit = SubmitField("/fetch")


def fetch(url: str) -> Tuple[bool, str]:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        if response.encoding != "utf-8":
            enc = response.encoding
            try:
                return (False, response.content.decode(encoding=enc, errors="replace"))
            except:
                return (True, "Failed to decode content")

        return (False, response.text)
    except Exception as e:
        return (True, str(e))
