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

if ($in{'coll'}) {
  # we are editing an existing collection
  $title=$text{'ecoll_title_edit'};
  
  if (! -e "$module_config_directory/$in{'coll'}.list") {
    &error(&text('ecoll_err_notexist', $in{'coll'}));
  }
  
  open(FILE, "$module_config_directory/$in{'coll'}.list");
    @files=<FILE>;
  close(FILE);

} else {
  # we want to create a new collection
  $title=$text{'ecoll_title_new'};
}

  &header($title, "", undef, undef, undef, undef,
        "Written by<BR><A HREF=mailto:tim\@niemueller.de>Tim Niemueller</A><BR><A HREF=http://www.niemueller.de/webmin/modules/download/>Home://page</A>");

print "<HR><BR>\n";

if ($in{'coll'}) {

$pid=0;
open(CHILD, "ps xw |");
 while(<CHILD>) {
   if (/wget/ && /$module_config_directory\/$in{'coll'}\.list/) {
     /\s+(\d+)*/;
     $pid=$1;
   }
 }
close(CHILD);

if ($pid) {
print <<EOM;
<H3>Wget is downloading this collection with PID $pid.</H3>
<BR>

EOM
}

print <<EOM;

<TABLE BORDER=1 CELLPADDING=3 CELLSPACING=0 $cb WIDTH=100%>
 <TR>
  <TD>

   <TABLE BORDER=0 $cb CELLPADDING=0 CELLSPACING=0 WIDTH=100%>
    <TR>
     <TD $tb COLSPAN=2>

      <TABLE BORDER=0 CELLSPACING=3 CELLPADDING=0 $tb WIDTH=100%>
       <TR>
        <TD><B>$title</B></TD>
       </TR>
      </TABLE>

     </TD>
    </TR>

EOM

for (my $i=0; $i < @files; $i++) {
  chomp $files[$i];
  next if ($files[$i] =~ /^#/);

print <<EOM;
    <TR>
     <TD $cb>$files[$i]</TD>
     <TD ALIGN=right><A HREF="edit_entry.cgi?coll=$in{'coll'}&entry=$1">Edit</A> /
                     <A HREF="delete_entry.cgi?coll=$in{'coll'}&entry=$i">Delete</A></TD>
    </TR>
EOM

}

if (! scalar(@files)) {
  print "<TR><TD $cb>$text{'ecoll_nofiles'}</TD></TR>";
}

print <<EOM;

   </TABLE>
  </TD>
 </TR>
</TABLE>


<FORM METHOD=GET ACTION="save_collection.cgi">
<INPUT TYPE=hidden NAME="coll" VALUE="$in{'coll'}">

<TABLE BORDER=1 CELLPADDING=1 CELLSPACING=0 $cb>
 <TR>
  <TD>

   <TABLE BORDER=0 CELLPADDING=0 CELLSPACING=0 $cb WIDTH=100%>
    <TR>
     <TD $tb COLSPAN=2>

      <TABLE BORDER=0 CELLSPACING=3 CELLPADDING=0 $tb WIDTH=100%>
       <TR>
        <TD><B>$text{'ecoll_addentry'}</B></TD>
       </TR>
      </TABLE>

     </TD>
    </TR>

    <TR>
     <TD $cb><B>$text{'ecoll_url'}: </B></TD>
     <TD><INPUT TYPE=text NAME="newurl" SIZE=60> <INPUT TYPE=submit NAME="newentry" VALUE="$text{'save'}"></TD>
    </TR>

   </TABLE>
  </TD>
 </TR>
</TABLE>

<BR>
<INPUT TYPE="submit" NAME="delete" VALUE="$text{'ecoll_delete'}">
EOM

if ($pid) {
  print "<INPUT TYPE=submit NAME=\"stop\" VALUE=\"$text{'ecoll_stop'}\">";
} else {
  print "<INPUT TYPE=submit NAME=\"download\" VALUE=\"$text{'ecoll_download'}\">";
}

print "</FORM><HR>";


} else {


 $dirch = &file_chooser_button("dir", 1);

print <<EOM;

<FORM METHOD=GET ACTION="save_collection.cgi">

<TABLE BORDER=1 CELLPADDING=3 CELLSPACING=0 $cb>
 <TR>
  <TD>

   <TABLE BORDER=0 $cb WIDTH=100%>
    <TR>
     <TD $tb COLSPAN=2>

      <TABLE BORDER=0 CELLSPACING=3 CELLPADDING=0 $tb WIDTH=100%>
       <TR>
        <TD><B>$title</B></TD>
       </TR>
      </TABLE>

     </TD>
    </TR>

    <TR>
     <TD $cb>$text{'ecoll_name'}</TD>
     <TD><INPUT TYPE=text NAME="coll"></TD>
    </TR>

    <TR>
     <TD $cb>$text{'ecoll_dir'}</TD>
     <TD><INPUT TYPE=text NAME="dir"> $dirch</TD>
    </TR>

   </TABLE>
  </TD>
 </TR>
</TABLE>

<INPUT TYPE=submit NAME="new" VALUE="$text{'save'}">

</FORM>

<HR>

EOM

}

&footer("index.cgi", $text{'ecoll_return'});





### END of edit_collection.cgi ###.
