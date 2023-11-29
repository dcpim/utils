"""Run tests for DCPIM utils."""

import dcpim

JSONFILE = "/tmp/" + dcpim.guid() + ".json"
json_data = {'name': "Hello world", 'results': ["test 1", "test 2", "test 3"]}

# guid
assert len(dcpim.test("guid", [])) == 16
assert len(dcpim.test("guid", [32])) == 32

# in_tag
assert dcpim.test("in_tag", [
	"<p>This is a link to <a href='http://google.com'>Google</a>.</p>",
	"a"
]) == "Google"
assert dcpim.test("in_tag", [
	"this random string is something, right?",
	"random", ","
]) == "string is something"
assert dcpim.test("in_tag", [
	"this random string is something, right?",
	"umbrella", ","
]) == ""

# save
assert not dcpim.test("save", [JSONFILE, json_data])

# load
assert dcpim.test("load", [JSONFILE]) == json_data

# unixtime
assert dcpim.test("unixtime", []) > 1

# now
assert len(dcpim.test("now", [])) == 19

# max_len
assert dcpim.test("max_len", [
	"This text is too long to fit in the max len.",
	25
]) == "This text is too long ..."

# remove_spaces
assert dcpim.test("remove_spaces", [
	"  This is  a test of   the \"emergency  broadcast system\". "
]) == "This is a test of the \"emergency broadcast system\"."
