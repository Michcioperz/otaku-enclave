import protector
from htmldom import htmldom

class AnimeTwistDataProvider(protector.DataProvider):
    def show_datafy(self, show):
        try:
            data = json.loads(htmldom.HtmlDom("https://twist.moe/a/%s" % show.codename).createDom().find("script#series-object").text())
            show.description = data.get("description", "")
            show.title = data.get("title", "")
            show.alternative_title = data.get("altTitle", "")
        except:
            pass
        return show
