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

&header($text{'index_title'}, "", undef, 1, 1, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de/webmin/modules/download/>Home://page</A>");

print "<HR><BR>\n";

print "<H3>$text{'index_collections'}</H3>\n";

opendir(DIR, $module_config_directory);
  while($l = readdir(DIR)) {
    if ($l =~ /^(\S+)\.list$/) {
      push(@image, "images/collection.gif");
      push(@text, $1);
      push(@link, "edit_collection.cgi?coll=$1");
    }
  }
closedir(DIR);

if (scalar(@image)) {
  &icons_table(\@link, \@text, \@image, 4);
} else {
  print "<B>$text{'index_nocollections'}</B><BR><BR>\n";
}

print <<EOM;
<BR><A HREF="edit_collection.cgi">$text{'index_newcoll'}</A><HR>

<TABLE BORDER=0>
 <TR>
  <TD>
   <FORM METHOD=GET ACTION="edit_options.cgi">
    <INPUT TYPE=submit NAME="edit" VALUE="$text{'index_editopt'}">
  </TD>
   </FORM>
  <TD>
   $text{'index_optdesc'}
  </TD>
 </TR>
</TABLE>
<BR><HR>
EOM



&footer("/", $text{'index'});





### END of index.cgi ###.
