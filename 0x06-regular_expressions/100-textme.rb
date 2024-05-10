#!/usr/bin/env ruby
i=ARGV[0].scan(/(?<=from:)[\w+]+/).join(",")
j=ARGV[0].scan(/(?<=to:)[\w+]+/).join(",")
z=ARGV[0].scan(/(?<=flags:)[\w+-:]+/).join(",")
puts [i,j,z].join(",")
