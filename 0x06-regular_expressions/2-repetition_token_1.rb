#!/usr/bin/env ruby
regex = /hb{0,1}tn/
occurs =ARGC[0].scan(regex)
for i in occurs
print i
end
print "\n"
