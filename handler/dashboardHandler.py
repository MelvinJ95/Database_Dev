from flask import jsonify, Flask
from dao.dashboard import DashboardDAO

class DashboardHandler:
    def dashboard(self):
        dao = DashboardDAO()
        trendhash = dao.getTrends()
        # trenduser = dao.trendUser()
        # numlike = dao.getLikesByPostId()
        # numdis = dao.getDislikesByPostId()
        # numr = dao.numreply()
        # numm = dao.nummessage()
        return jsonify(Dashboard={"TrendingHash": self.appendName(trendhash),
                                  # "TrendingUser": self.appendName(trenduser),
                                  # "NumberOfLikes": numlike, "NumberOfDislikes": numdis,
                                  # "NumberOfReplies": numr, "NumberOfMessages": numm
        })

    def appendName(self, m):
        result = []
        for r in m:
            result.append(self.maptoName(r))
        return result

    def maptoName(self, h):
        mapped = {"Name": h[0], "Count": h[1]}
        return mapped