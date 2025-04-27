from app.db import db


class Test(db.Model):
    __tablename__ = "test"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def getId(self):
        return self.id

    def getCreatedAt(self):
        return self.created_at

    def setCreatedAt(self, created_at):
        self.created_at = created_at
        return self
