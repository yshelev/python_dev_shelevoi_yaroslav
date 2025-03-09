from peewee import Case

from scripts.models import EventType, SpaceType

CASES = {
	"EVENT_TYPE": {
		"EQUAL_LOGIN":
			Case(None, [
                (EventType.name == "login", 1)],
		        0
		    ),
		"EQUAL_LOGOUT" :
			Case(None, [
                (EventType.name == "logout", 1)],
                0
            )
	},
	"SPACE_TYPE": {
		"EQUAL_BLOG":
			Case(None, [
                (SpaceType.name == "blog", 1)],
                0
            )
	}
}