#!/usr/bin/env Ruby
regex = /hbt{0,}n/
occurs = ARGV[0].scan(regex)
for i in occurs
print i
end
print "\n"
