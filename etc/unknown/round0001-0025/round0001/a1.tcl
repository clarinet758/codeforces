set line [gets stdin]
scan $line "%d" n

if {$n==1} {
    puts 1
} elseif {$n==2} {
    puts 2
} elseif {$n==3} {
    puts 6
} elseif {$n==4} {
    puts 24
} elseif {$n==5} {
    puts 120
} elseif {$n==6} {
    puts 720
} elseif {$n==7} {
    puts 5040
} elseif {$n==8} {
    puts 40320
} elseif {$n==9} {
    puts 362880
} elseif {$n==10} {
    puts 3628800
}
