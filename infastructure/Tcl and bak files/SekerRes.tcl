#############################################################################
# Generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#  Dec 31, 2020 04:54:12 PM +0200  platform: Windows NT
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




proc vTclWindow.top55 {base} {
    global vTcl
    if {$base == ""} {
        set base .top55
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background #8080ff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1366x705+383+106
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1370 749
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm title $top "???????????? ??????"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    label $top.lab56 \
        -activebackground #f9f9f9 -activeforeground black -background #8080ff \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {???????????? ??????} 
    vTcl:DefineAlias "$top.lab56" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab57 \
        -activebackground #f9f9f9 -activeforeground black -background #8080ff \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {???????? ????????????                      ??????????????} 
    vTcl:DefineAlias "$top.lab57" "Allpar" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab58 \
        -activebackground #f9f9f9 -activeforeground black -background #8080ff \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {?????????? 1 ????????????} 
    vTcl:DefineAlias "$top.lab58" "Q1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab59 \
        -activebackground #f9f9f9 -activeforeground black -background #8080ff \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {?????????? 2 ????????????} 
    vTcl:DefineAlias "$top.lab59" "Q2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab60 \
        -activebackground #f9f9f9 -activeforeground black -background #8080ff \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {?????????? 3 ????????????} 
    vTcl:DefineAlias "$top.lab60" "Q3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab61 \
        -activebackground #f9f9f9 -activeforeground black -background #8080ff \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {?????????? 4 ????????????} 
    vTcl:DefineAlias "$top.lab61" "Q4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab62 \
        -activebackground #f9f9f9 -activeforeground black -background #8080ff \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {?????????? 5 ????????????} 
    vTcl:DefineAlias "$top.lab62" "Q5" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab63 \
        -activebackground #f9f9f9 -activeforeground black -background #8080ff \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {?????????? 6 ????????????} 
    vTcl:DefineAlias "$top.lab63" "Q6" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab64 \
        -activebackground #f9f9f9 -activeforeground black -background #8080ff \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {?????????? 7 ????????????} 
    vTcl:DefineAlias "$top.lab64" "Q7" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab65 \
        -activebackground #f9f9f9 -activeforeground black -background #8080ff \
        -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {?????????? 8 ????????????} 
    vTcl:DefineAlias "$top.lab65" "Q8" vTcl:WidgetProc "Toplevel1" 1
    button $top.but67 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {?????????? ????????} 
    vTcl:DefineAlias "$top.but67" "BackButton" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab51 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 1 
    vTcl:DefineAlias "$top.lab51" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab52 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 2 
    vTcl:DefineAlias "$top.lab52" "Label3" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab53 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text 3 
    vTcl:DefineAlias "$top.lab53" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab54 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab54" "q11" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab55 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab55" "q12" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab66 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab66" "q13" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab67 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab67" "q23" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab68 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab68" "q22" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab69 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab69" "q21" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab70 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab70" "q33" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab71 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab71" "q32" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab72 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab72" "q31" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab73 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab73" "q41" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab74 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab74" "q42" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab75 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab75" "q43" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab76 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab76" "q61" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab77 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab77" "q62" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab78 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab78" "q63" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab79 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab79" "q71" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab80 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab80" "q72" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab81 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab81" "q73" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab82 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab82" "q83" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab83 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab83" "q82" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab84 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab84" "q81" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab45 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text Label 
    vTcl:DefineAlias "$top.lab45" "q51" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab46 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text Label 
    vTcl:DefineAlias "$top.lab46" "q52" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab47 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) -text Label 
    vTcl:DefineAlias "$top.lab47" "q53" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab56 \
        -in $top -x 0 -relx 0.4 -y 0 -rely 0.067 -width 0 -relwidth 0.207 \
        -height 0 -relheight 0.091 -anchor nw -bordermode ignore 
    place $top.lab57 \
        -in $top -x 0 -relx 0.366 -y 0 -rely 0.156 -width 0 -relwidth 0.54 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab58 \
        -in $top -x 0 -relx 0.659 -y 0 -rely 0.27 -width 0 -relwidth 0.088 \
        -height 0 -relheight 0.047 -anchor nw -bordermode ignore 
    place $top.lab59 \
        -in $top -x 0 -relx 0.652 -y 0 -rely 0.34 -width 0 -relwidth 0.105 \
        -height 0 -relheight 0.031 -anchor nw -bordermode ignore 
    place $top.lab60 \
        -in $top -x 0 -relx 0.659 -y 0 -rely 0.411 -width 0 -relwidth 0.091 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab61 \
        -in $top -x 0 -relx 0.659 -y 0 -rely 0.482 -width 0 -relwidth 0.092 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab62 \
        -in $top -x 0 -relx 0.652 -y 0 -rely 0.553 -width 0 -relwidth 0.105 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab63 \
        -in $top -x 0 -relx 0.659 -y 0 -rely 0.61 -width 0 -relwidth 0.092 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab64 \
        -in $top -x 0 -relx 0.659 -y 0 -rely 0.667 -width 0 -relwidth 0.092 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab65 \
        -in $top -x 0 -relx 0.659 -y 0 -rely 0.723 -width 0 -relwidth 0.092 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.but67 \
        -in $top -x 0 -relx 0.029 -y 0 -rely 0.908 -width 87 -relwidth 0 \
        -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 0 -relx 0.564 -y 0 -rely 0.227 -width 0 -relwidth 0.026 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab52 \
        -in $top -x 0 -relx 0.483 -y 0 -rely 0.227 -width 0 -relwidth 0.026 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab53 \
        -in $top -x 0 -relx 0.41 -y 0 -rely 0.227 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.031 -anchor nw -bordermode ignore 
    place $top.lab54 \
        -in $top -x 0 -relx 0.564 -y 0 -rely 0.284 -width 0 -relwidth 0.026 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab55 \
        -in $top -x 0 -relx 0.483 -y 0 -rely 0.284 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab66 \
        -in $top -x 0 -relx 0.41 -y 0 -rely 0.284 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab67 \
        -in $top -x 0 -relx 0.41 -y 0 -rely 0.34 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab68 \
        -in $top -x 0 -relx 0.483 -y 0 -rely 0.34 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab69 \
        -in $top -x 0 -relx 0.564 -y 0 -rely 0.34 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab70 \
        -in $top -x 0 -relx 0.41 -y 0 -rely 0.397 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab71 \
        -in $top -x 0 -relx 0.483 -y 0 -rely 0.397 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab72 \
        -in $top -x 0 -relx 0.564 -y 0 -rely 0.397 -width 0 -relwidth 0.026 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab73 \
        -in $top -x 0 -relx 0.564 -y 0 -rely 0.468 -width 0 -relwidth 0.026 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab74 \
        -in $top -x 0 -relx 0.483 -y 0 -rely 0.468 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab75 \
        -in $top -x 0 -relx 0.41 -y 0 -rely 0.468 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab76 \
        -in $top -x 0 -relx 0.564 -y 0 -rely 0.61 -width 0 -relwidth 0.026 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab77 \
        -in $top -x 0 -relx 0.483 -y 0 -rely 0.61 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab78 \
        -in $top -x 0 -relx 0.41 -y 0 -rely 0.61 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab79 \
        -in $top -x 0 -relx 0.564 -y 0 -rely 0.681 -width 0 -relwidth 0.026 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab80 \
        -in $top -x 0 -relx 0.483 -y 0 -rely 0.681 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab81 \
        -in $top -x 0 -relx 0.41 -y 0 -rely 0.681 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab82 \
        -in $top -x 0 -relx 0.41 -y 0 -rely 0.738 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab83 \
        -in $top -x 0 -relx 0.483 -y 0 -rely 0.738 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab84 \
        -in $top -x 0 -relx 0.564 -y 0 -rely 0.738 -width 0 -relwidth 0.026 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab45 \
        -in $top -x 0 -relx 0.564 -y 0 -rely 0.553 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab46 \
        -in $top -x 0 -relx 0.483 -y 0 -rely 0.553 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
    place $top.lab47 \
        -in $top -x 0 -relx 0.41 -y 0 -rely 0.553 -width 0 -relwidth 0.025 \
        -height 0 -relheight 0.03 -anchor nw -bordermode ignore 
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
Window show .top55 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

