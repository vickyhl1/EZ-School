#############################################################################
# Generated by PAGE version 5.6
#  in conjunction with Tcl version 8.6
#  Dec 31, 2020 04:52:09 PM +0200  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m45" -background #fef1b4 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1920x1051+-9+-9
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "נוכחות כיתה ה"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    menu $top.m45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    button $top.but46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #f5cb03 -cursor hand2 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {הגשת נוכחות} 
    vTcl:DefineAlias "$top.but46" "submit" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #fef1b4 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {סמי הכבאי 123498765} -variable che47 
    vTcl:DefineAlias "$top.che47" "stud1" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #fef1b4 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {ליטל פוני 302944245} -variable che49 
    vTcl:DefineAlias "$top.che49" "stud2" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che50 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #fef1b4 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {הדס חדד 230145678} -variable che50 
    vTcl:DefineAlias "$top.che50" "stud3" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #fef1b4 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {לוקי אודינסן 892767673} -variable che51 
    vTcl:DefineAlias "$top.che51" "stud4" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #fef1b4 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {תור אודינסן 892767674} -variable che52 
    vTcl:DefineAlias "$top.che52" "stud5" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che53 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #fef1b4 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {נמו גולד 112223224} -variable che53 
    vTcl:DefineAlias "$top.che53" "stud6" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che54 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #fef1b4 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {דורה אקספלולה 189098079} -variable che54 
    vTcl:DefineAlias "$top.che54" "stud7" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che55 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #fef1b4 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {דיאגו מרדונה 3742310999} -variable che55 
    vTcl:DefineAlias "$top.che55" "stud8" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che56 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #fef1b4 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {אש קצ'אם 382746583} -variable che56 
    vTcl:DefineAlias "$top.che56" "stud9" vTcl:WidgetProc "Toplevel1" 1
    checkbutton $top.che57 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #fef1b4 -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 11 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text {בוב הבנאי 236423233} -variable che57 
    vTcl:DefineAlias "$top.che57" "stud10" vTcl:WidgetProc "Toplevel1" 1
    message $top.mes58 \
        -background #fef1b4 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {אנא סמנו את התלמידים הנוכחים} -width 597 
    vTcl:DefineAlias "$top.mes58" "Message1" vTcl:WidgetProc "Toplevel1" 1
    button $top.but59 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #f5cb03 -cursor hand2 -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {תפריט ראשי} 
    vTcl:DefineAlias "$top.but59" "mainmenu" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but46 \
        -in $top -x 0 -relx 0.385 -y 0 -rely 0.879 -width 456 -relwidth 0 \
        -height 93 -relheight 0 -anchor nw -bordermode ignore 
    place $top.che47 \
        -in $top -x 0 -relx 0.354 -y 0 -rely 0.133 -width 0 -relwidth 0.213 \
        -height 0 -relheight 0.061 -anchor nw -bordermode ignore 
    place $top.che49 \
        -in $top -x 0 -relx 0.365 -y 0 -rely 0.181 -width 0 -relwidth 0.184 \
        -height 0 -relheight 0.061 -anchor nw -bordermode ignore 
    place $top.che50 \
        -in $top -x 0 -relx 0.344 -y 0 -rely 0.238 -width 0 -relwidth 0.227 \
        -height 0 -relheight 0.061 -anchor nw -bordermode ignore 
    place $top.che51 \
        -in $top -x 0 -relx 0.358 -y 0 -rely 0.3 -width 0 -relwidth 0.213 \
        -height 0 -relheight 0.061 -anchor nw -bordermode ignore 
    place $top.che52 \
        -in $top -x 0 -relx 0.354 -y 0 -rely 0.362 -width 0 -relwidth 0.218 \
        -height 0 -relheight 0.051 -anchor nw -bordermode ignore 
    place $top.che53 \
        -in $top -x 0 -relx 0.339 -y 0 -rely 0.41 -width 0 -relwidth 0.233 \
        -height 0 -relheight 0.061 -anchor nw -bordermode ignore 
    place $top.che54 \
        -in $top -x 0 -relx 0.375 -y 0 -rely 0.47 -width 0 -relwidth 0.196 \
        -height 0 -relheight 0.052 -anchor nw -bordermode ignore 
    place $top.che55 \
        -in $top -x 0 -relx 0.365 -y 0 -rely 0.514 -width 0 -relwidth 0.206 \
        -height 0 -relheight 0.062 -anchor nw -bordermode ignore 
    place $top.che56 \
        -in $top -x 0 -relx 0.354 -y 0 -rely 0.571 -width 0 -relwidth 0.217 \
        -height 0 -relheight 0.051 -anchor nw -bordermode ignore 
    place $top.che57 \
        -in $top -x 0 -relx 0.36 -y 0 -rely 0.628 -width 0 -relwidth 0.202 \
        -height 0 -relheight 0.05 -anchor nw -bordermode ignore 
    place $top.mes58 \
        -in $top -x 0 -relx 0.333 -y 0 -rely 0.02 -width 0 -relwidth 0.311 \
        -height 0 -relheight 0.1 -anchor nw -bordermode ignore 
    place $top.but59 \
        -in $top -x 0 -relx 0.01 -y 0 -rely 0.913 -width 176 -relwidth 0 \
        -height 73 -relheight 0 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

