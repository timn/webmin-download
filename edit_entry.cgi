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
&ReadParse();

open(FILE, "$module_config_directory/$in{'coll'}.list");
 @files = <FILE>;
close(FILE);

$url=$files[$in{'entry'}];

&header($text{'eentry_title'}, "", undef, undef, undef, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de/webmin/modules/download/>Home://page</A>");

print "<HR><BR>\n";

print <<EOM;

<FORM METHOD=POST ACTION="save_entry.cgi">
<INPUT TYPE=hidden NAME="coll" VALUE="$in{'coll'}">
<INPUT TYPE=hidden NAME="entry" VALUE="$in{'entry'}">

<TABLE BORDER=1 CELLPADDING=1 CELLSPACING=0 $cb>
 <TR>
  <TD>

   <TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 $cb WIDTH=100%>
    <TR>
     <TD $tb COLSPAN=2>

      <TABLE BORDER=0 CELLSPACING=3 CELLPADDING=0 $tb WIDTH=100%>
       <TR>
        <TD><B>$text{'eentry_change'}</B></TD>
       </TR>
      </TABLE>

     </TD>
    </TR>

    <TR>
     <TD $cb>$text{'eentry_url'}</TD>
     <TD><INPUT TYPE=text NAME="newurl" SIZE=60 VALUE="$url"> <INPUT TYPE=submit NAME="newentry" VALUE="$text{'save'}"></TD>
    </TR>

   </TABLE>
  </TD>
 </TR>
</TABLE>

</FORM>


<HR>

EOM

&footer("edit_collection.cgi?coll=$in{'coll'}", $text{'eentry_return'});





### END of edit_entry.cgi ###.
