set line [gets stdin]

set op [string index $line 1]
set a [string index $line 0]
set b [string index $line 2]

switch $op {
    "+" {
        set ans [expr {$a+$b}]
        puts $ans
    }
    "-" {
        set ans [expr {$a-$b}]
        puts $ans
    }
}
