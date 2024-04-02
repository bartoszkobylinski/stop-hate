from flask_login import UserMixin
from backend.database import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    tokens_used = db.Column(db.Integer, default=0)
    token_cost = db.Column(db.Integer, default=0.0)

    def update_token_used(self, tokens):
        self.tokens_used += tokens
        self.update_token_used()
        db.session.commit()

    def update_token_cost(self, cost_per_token=0.0001):
        self.token_cost = self.tokens_used * cost_per_token

    def get_token_info(self):
        return {"token_used": self.tokens_used, "token_cost":self.token_cost}
