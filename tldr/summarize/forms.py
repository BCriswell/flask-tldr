# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import URL, Required, Length


class SummaryForm(Form):
    url = StringField('URL', validators=[Required(), Length(1, 255), URL()])
    submit = SubmitField('Submit')
