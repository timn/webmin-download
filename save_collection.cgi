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

if ($in{'new'}) {
  # we create a new collection
  open(FILE, ">$module_config_directory/$in{'coll'}.conf");
    for (keys %in) {
      print FILE "$_=$in{$_}\n";
    }
  close(FILE);
  open(FILE, ">$module_config_directory/$in{'coll'}.list");
  close(FILE);
} elsif ($in{'delete'}) {
  system("rm -f $module_config_directory/$in{'coll'}.list");
  system("rm -f $module_config_directory/$in{'coll'}.conf");
  &redirect("");
} elsif ($in{'download'}) {
  &has_command("wget") || (-x $config{'wgetpath'}) || &error($text{'scoll_err_nowget'});
  $wget = $config{'wgetpath'} ? $config{'wgetpath'} : "wget";

  open(FILE, "$module_config_directory/wget.options");
   while(<FILE>) {
     chomp;
     if (! /^#/ && ($_ ne "")) {
       /^([^=]+)=(.*)$/;
       $options{$1}=$2;
     }
   }
  close(FILE);

  open(FILE, "$module_config_directory/$in{'coll'}.conf");
   while(<FILE>) {
     chomp;
     if (! /^#/ && ($_ ne "")) {
       /^([^=]+)=(.*)$/;
       $conf{$1}=$2;
     }
   }
  close(FILE);

  $cont = $options{'continue'} ? "-c" : "";
  $rec = $options{'recursive'} ? "-r" : "";
  $levels = $options{'levels'} ? "-l$options{'levels'}" : "";
  $tries = $options{'tries'} ? "-t$options{'tries'}" : "";
  

  system("$wget -nv -q -b --directory-prefix=$conf{'dir'} $cont $rec $levels $tries -i $module_config_directory/$in{'coll'}.list");
  
  &redirect("edit_collection.cgi?coll=$in{'coll'}");
} elsif ($in{'stop'}) {

  $pid=0;
  open(CHILD, "ps xw |");
   while(<CHILD>) {
     if (/wget/ && /$module_config_directory\/$in{'coll'}\.list/) {
       /\s+(\d+)*/;
       $pid=$1;
     }
   }
  close(CHILD);

  $pid || &error($text{'scoll_err_nopid'});

  system("kill $pid");

} else {
  if ($in{'newurl'}) {
    open(FILE, ">>$module_config_directory/$in{'coll'}.list");
      print FILE "$in{'newurl'}\n";
    close(FILE);
  }
}


&redirect("edit_collection.cgi?coll=$in{'coll'}");


### END of save_collection.cgi ###.
