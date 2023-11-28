"""Run tests for DCPIM utils."""

import dcpim

jsonfile = "/tmp/" + dcpim.guid() + ".json"
jsondata = {'name': "Hello world", 'results': ["test 1", "test 2", "test 3"]}

# guid
assert len(dcpim._test("guid", [])) == 16
assert len(dcpim._test("guid", [32])) == 32

# in_tag
assert dcpim._test("in_tag", [
	"<p>This is a link to <a href='http://google.com'>Google</a>.</p>",
	"a"
]) == "Google"
assert dcpim._test("in_tag", [
	"this random string is something, right?",
	"random", ","
]) == "string is something"
assert dcpim._test("in_tag", [
	"this random string is something, right?",
	"umbrella", ","
]) == ""

# save
assert not dcpim._test("save", [jsonfile, jsondata])

# load
assert dcpim._test("load", [jsonfile]) == jsondata

# unixtime
assert dcpim._test("unixtime", []) > 1

# now
assert len(dcpim._test("now", [])) == 19

# max_len
assert dcpim._test("max_len", [
	"This text is too long to fit in the max len.",
	25
]) == "This text is too long ..."

# remove_spaces
assert dcpim._test("remove_spaces", [
	"  This is  a test of   the \"emergency  broadcast system\". "
]) == "This is a test of the \"emergency broadcast system\"."


