# -*- coding: utf-8 -*-
import datetime

from tldr.database import Column, Model, SurrogatePK, db, reference_col, relationship

from pyteaser import SummarizeUrl


class Summary(SurrogatePK, Model):
    __tablename__ = 'summaries'
    # summary_id = Column(db.Integer, primary_key=True)
    url = Column(db.String(255))
    summary = Column(db.Text())
    posted_date = Column(db.Date, default=datetime.datetime.utcnow())

    def __init__(self, url, summary=None, **kwargs):
        db.Model.__init__(self, url=url, **kwargs)
        if url:
            self.get_article_summary(url)
        else:
            self.summary = None

    def __repr__(self):
        return '<Summary({url})>'.format(url=self.url)

    def get_article_summary(self, url):
        summaries = SummarizeUrl(url)
        if summaries:
            self.summary = ' '.join(summaries)
        else:
            self.summary = 'No summary available.'
