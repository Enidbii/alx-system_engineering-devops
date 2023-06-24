#!/usr/bin/env ruby

Fmt = ARGV[0].scan(/from:(.\w+)| to:(.\w+)| flags:([0-9:-]+)/)
message_list = [Fmt[0].compact, Fmt[1].compact, Fmt[2].compact] 

puts message_list.join(,)
