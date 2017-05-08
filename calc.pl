#! /usr/bin/perl

$in = $ARGV[0];
print "file: $in\n";

$i=0;
$TSA_total1=0;
$TSA_total2=0;
$TSA_diff_total=0;
$PS2_total1=0;
$PS2_total2=0;
$PS2_diff_total=0;
$diff2=0;
$TSA_max1=-999;
$TSA_max2=-999;
$TSA_diff_max=-999;
$PS2_max1=-999;
$PS2_max2=-999;
$PS2_diff_max=-999;
$TSA_min1=999;
$TSA_min2=999;
$TSA_diff_min=999;
$PS2_min1=999;
$PS2_min2=999;
$PS2_diff_min=999;

open(IN, $in) or die;
foreach $line (<IN>){
	chomp $line;
	($n[$i],$TSA1[$i],$TSA2[$i],$TSAdiff[$i],$PS21[$i],$PS22[$i],$PS2diff[$i]) = split(",", $line);
	#print "$n[$i] $TSA1[$i] $TSA2[$i] $TSAdiff[$i] $PS21[$i] $PS22[$i] $PS2diff[$i]\n";
	$TSA_total1     += $TSA1[$i];
	$TSA_total2     += $TSA2[$i];
	$TSA_diff_total += $TSAdiff[$i];
	$PS2_total1     += $PS21[$i];
	$PS2_total2     += $PS22[$i];
	$PS2_diff_total += $PS2diff[$i];
	$TSAdiff2[$i]    = $TSAdiff[$i]*$TSAdiff[$i];
	$PS2diff2[$i]    = $PS2diff[$i]*$PS2diff[$i];
	$diff2          += $TSAdiff2[$i] + $PS2diff2[$i];
	$TSA_max1        = $TSA1[$i]    if $TSA_max1<$TSA1[$i];
	$TSA_max2        = $TSA2[$i]    if $TSA_max2<$TSA2[$i];
	$TSA_diff_max    = $TSAdiff[$i] if $TSA_diff_max<$TSAdiff[$i];
	$PS2_max1        = $PS21[$i]    if $PS2_max1<$PS21[$i];
	$PS2_max2        = $PS22[$i]    if $PS2_max2<$PS22[$i];
	$PS2_diff_max    = $PS2diff[$i] if $PS2_diff_max<$PS2diff[$i];
	$TSA_min1        = $TSA1[$i]    if $TSA_min1>$TSA1[$i];
	$TSA_min2        = $TSA2[$i]    if $TSA_min2>$TSA2[$i];
	$TSA_diff_min    = $TSAdiff[$i] if $TSA_diff_min>$TSAdiff[$i];
	$PS2_min1        = $PS21[$i]    if $PS2_min1>$PS21[$i];
	$PS2_min2        = $PS22[$i]    if $PS2_min2>$PS22[$i];
	$PS2_diff_min    = $PS2diff[$i] if $PS2_diff_min>$PS2diff[$i];

	$i++
}
close IN;

$ndata = $i;
print "data: $ndata\n";

$TSA_mean1     = $TSA_total1/$ndata;
$TSA_mean2     = $TSA_total2/$ndata;
$TSA_diff_mean = $TSA_diff_total/$ndata;
$PS2_mean1     = $PS2_total1/$ndata;
$PS2_mean2     = $PS2_total2/$ndata;
$PS2_diff_mean = $PS2_diff_total/$ndata;
$Loss          = $diff2/2./$ndata;

printf "mean:  %10.6f %10.6f %10.6f %10.6f %10.6f %10.6f\n", $TSA_mean1, $TSA_mean2, $TSA_diff_mean, $PS2_mean1, $PS2_mean2, $PS2_diff_mean;
printf "max:   %10.6f %10.6f %10.6f %10.6f %10.6f %10.6f\n", $TSA_max1, $TSA_max2, $TSA_diff_max, $PS2_max1, $PS2_max2, $PS2_diff_max;
printf "min:   %10.6f %10.6f %10.6f %10.6f %10.6f %10.6f\n", $TSA_min1, $TSA_min2, $TSA_diff_min, $PS2_min1, $PS2_min2, $PS2_diff_min;

$var_TSA1=0;
$var_TSA2=0;
$var_TSAdiff=0;
$var_PS21=0;
$var_PS22=0;
$var_PS2diff=0;
$var_diff2=0;
for($i=0;$i<$ndata;$i++){
	$var_TSA1    += ($TSA1[$i]-$TSA_mean1)*($TSA1[$i]-$TSA_mean1);
	$var_TSA2    += ($TSA2[$i]-$TSA_mean2)*($TSA2[$i]-$TSA_mean2);
	$var_TSAdiff += ($TSAdiff[$i]-$TSA_diff_mean)*($TSAdiff[$i]-$TSA_diff_mean);
	$var_PS21    += ($PS21[$i]-$PS2_mean1)*($PS21[$i]-$PS2_mean1);
	$var_PS22    += ($PS22[$i]-$PS2_mean2)*($PS22[$i]-$PS2_mean2);
	$var_PS2diff += ($PS2diff[$i]-$PS2_diff_mean)*($PS2diff[$i]-$PS2_diff_mean);
	$var_diff2   += ($TSAdiff2[$i]/2.-$Loss)*($TSAdiff2[$i]/2.-$Loss);
	$var_diff2   += ($PS2diff2[$i]/2.-$Loss)*($PS2diff2[$i]/2.-$Loss);
}

$var_TSA1    = $var_TSA1/($ndata-1);
$var_TSA2    = $var_TSA2/($ndata-1);
$var_TSAdiff = $var_TSAdiff/($ndata-1);
$var_PS21    = $var_PS21/($ndata-1);
$var_PS22    = $var_PS22/($ndata-1);
$var_PS2diff = $var_PS2diff/($ndata-1);
$var_diff2   = $var_diff2/$ndata;

printf "var:   %10.6f %10.6f %10.6f %10.6f %10.6f %10.6f\n", $var_TSA1, $var_TSA2, $var_TSAdiff, $var_PS21, $var_PS22, $var_PS2diff;

$stdev_TSA1    = sqrt($var_TSA1);
$stdev_TSA2    = sqrt($var_TSA2);
$stdev_TSAdiff = sqrt($var_TSAdiff);
$stdev_PS21    = sqrt($var_PS21);
$stdev_PS22    = sqrt($var_PS22);
$stdev_PS2diff = sqrt($var_PS2diff);
$stdev_diff2   = sqrt($var_diff2);
$error_diff2   = $stdev_diff2/sqrt($ndata);

printf "stdev: %10.6f %10.6f %10.6f %10.6f %10.6f %10.6f\n", $stdev_TSA1, $stdev_TSA2, $stdev_TSAdiff, $stdev_PS21, $stdev_PS22, $stdev_PS2diff;
print "\n";

printf "Loss: %10.6f    var %10.6f stdev %10.6f \nerror %10.6f\n", $Loss, $var_diff2, $stdev_diff2, $error_diff2;
print "\n";

printf "mean:  %10.6f %10.6f %10.6f %10.6f %10.6f %10.6f\n", $TSA_mean1*300, $TSA_mean2*300, $TSA_diff_mean*300, $PS2_mean1*200, $PS2_mean2*200, $PS2_diff_mean*200;
printf "max:   %10.6f %10.6f %10.6f %10.6f %10.6f %10.6f\n", $TSA_max1*300, $TSA_max2*300, $TSA_diff_max*300, $PS2_max1*200, $PS2_max2*200, $PS2_diff_max*200;
printf "min:   %10.6f %10.6f %10.6f %10.6f %10.6f %10.6f\n", $TSA_min1*300, $TSA_min2*300, $TSA_diff_min*300, $PS2_min1*200, $PS2_min2*200, $PS2_diff_min*200;
printf "var:   %10.6f %10.6f %10.6f %10.6f %10.6f %10.6f\n", $var_TSA1*300, $var_TSA2*300, $var_TSAdiff*300, $var_PS21*200, $var_PS22*200, $var_PS2diff*200;
printf "stdev: %10.6f %10.6f %10.6f %10.6f %10.6f %10.6f\n", $stdev_TSA1*300, $stdev_TSA2*300, $stdev_TSAdiff*300, $stdev_PS21*200, $stdev_PS22*200, $stdev_PS2diff*200;
print "\n";
