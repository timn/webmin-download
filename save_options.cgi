#!/usr/bin/perl
#
#    Download Webmin Module
#    Copyright (C) 2000 by Tim Niemueller <tim@niemueller.de>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    This module inherited from the Webmin Module Template 0.79.1 by tn

#    Created 07.07.2000

do '../web-lib.pl';
$|=1;
&init_config("download");
%access=&get_module_acl();
&ReadParse();


($in{'levels'} =~ /^\d+$/) || &error("$text{'sopt_levels'}");
($in{'tries'} =~ /^\d+$/) || &error("$text{'sopt_tries'}");


open(FILE, ">$module_config_directory/wget.options");
 for (keys %in) {
   print FILE "$_=$in{$_}\n";
 }
close(FILE);

&redirect("");


### END of save_options.cgi ###.
