from browser import document, window, html
from .primitive import box, arrow, cone, curve, pyramid, helix, cylinder, ellipsoid
from .primitive import sphere, ring, attach_trail, compound, extrusion, text
from .utils import create_script_tag
from .vector import vec

GLOWID = '_glow_'
project_stdlib = "../stlib/"  # os.path.dirname("../stdlib{}/".format(os.path.abspath(__file__)))

version = "2.7"

create_script_tag('/js/glow.2.7.min.js')


class Glow:
    def __init__(self, container):
        glowid = GLOWID+container
        if glowid in document:
            document[container].remove()
        document[container] <= html.DIV(Id=glowid, Class="glowscript")
        self._id = document.get(id=glowid)[0]
        # setattr(self._id, 'id', '')

        setattr(window, '__context', {})
        setattr(getattr(window, '__context'), 'glowscript_container',
                self._id.elt)


# todo, make canvas its own class
def canvas():
    return window.glowscript.canvas()


def rate(t, func):
    window.glowscript.rate(t, func)


color = window.glowscript.color
