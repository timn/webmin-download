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

%access=&get_module_acl;

%options=();
open(FILE, "$module_config_directory/wget.options");
 while(<FILE>) {
   chomp;

   if (! /^#/ && ($_ ne "")) {
     /^([^=]+)=(.*)$/;
     $options{$1}=$2;
   }
 }
close(FILE);

if ($options{'continue'}) {
 $continue1=" CHECKED";
} else {
 $continue0=" CHECKED";
}

if ($options{'recursive'}) {
 $recursive1=" CHECKED";
} else {
 $recursive0=" CHECKED";
}

&header($text{'eopt_title'}, "", "intro", 1, 1, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de/webmin/modules/download/>Home://page</A>");

print <<EOM;
<HR><BR>

<FORM METHOD=GET ACTION="save_options.cgi">

<TABLE BORDER=1 CELLPADDING=3 CELLSPACING=0 $cb WIDTH=100%>
 <TR>
  <TD>

   <TABLE BORDER=0 $cb CELLPADDING=0 CELLSPACING=0 WIDTH=100%>
    <TR>
     <TD $tb>

      <TABLE BORDER=0 CELLSPACING=3 CELLPADDING=0 $tb WIDTH=100%>
       <TR>
        <TD><B>$text{'eopt_title'}</B></TD>
       </TR>
      </TABLE>

     </TD>
    </TR>

    <TR>
     <TD $cb>
      <TABLE BORDER=0 WIDTH=100%>
       <TR>
        <TD>$text{'eopt_continue'}</TD>
        <TD>
         <INPUT TYPE=radio NAME="continue" VALUE=1$continue1> $text{'yes'}
         <INPUT TYPE=radio NAME="continue" VALUE=0$continue0> $text{'no'}
        </TD>
        <TD>$text{'eopt_recursive'}</TD>
        <TD>
         <INPUT TYPE=radio NAME="recursive" VALUE=1$recursive1> $text{'yes'}
         <INPUT TYPE=radio NAME="recursive" VALUE=0$recursive0> $text{'no'}
        </TD>
       </TR>
       <TR>
        <TD>$text{'eopt_numoftries'}</TD>
        <TD>
         <INPUT TYPE=text NAME="tries" VALUE="$options{'tries'}">
        </TD>
        <TD>$text{'eopt_numoflevels'}</TD>
        <TD>
         <INPUT TYPE=text NAME="levels" VALUE="$options{'levels'}">
        </TD>
       </TR>

      </TABLE>
     </TD>
    </TR>

   </TABLE>
  </TD>
 </TR>
</TABLE>

<INPUT TYPE=submit NAME="save" VALUE="$text{'save'}">

</FORM>

<HR>

EOM

&footer("/", $text{'index'});





### END of edit_options.cgi ###.
