# -*- coding: utf-8 -*-
from flask import Blueprint, redirect, render_template, request, url_for, flash
from flask_login import login_required

from tldr.utils import flash_errors
from tldr.summarize.forms import SummaryForm
from tldr.summarize.models import Summary

blueprint = Blueprint('summarize', __name__, static_folder='../static')


@blueprint.route('/summarize/create', methods=['GET', 'POST'])
def create_summary():
    summary_form = SummaryForm()
    if request.method == 'POST':
        if summary_form.validate_on_submit():
            summary = Summary.create(url=summary_form.url.data)
            summary.save()
            flash("Successfully created TLDR.")
            return redirect(url_for('public.home'))
        else:
            flash_errors(summary_form)
    return render_template('summarize/create.html', summary_form=summary_form)


@blueprint.route('/summarize/<int:summary_id>')
def summary_detail(summary_id):
    summary = Summary.query.get(summary_id)
    return render_template('summarize/detail.html', summary=summary)


@blueprint.route('/summarize/all')
def summary_list():
    summary_list = Summary.query.all()
    return render_template('summarize/list.html', summary_list=summary_list)
