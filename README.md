# Pythonista ui examples
 
 This contains a collection small examples to cover [ios pythonista](http://omz-software.com/pythonista/)
 ui module functionality based on the examples from pythonista forum and the examples provided with the app.
 
*   incdec.py, incdec.pyui -  example with label  and button
    - See Calculator.py in examples/User Interface directory for a more elaborate example
*   incdec1.py - above example without using pyui
*   dogcat.py, dogcat.pyui - example with imageview and circular button with background image
*   dogcat1.py - above example without using pyui
*   imageview_in_scrollview - image size is not changed by putting inside scrollview, read from photos
*   basic_ui_elements.py - modify label using textfield, segmentedcontrol, datepicker, switch, slider and button
    - See ColorMixer.py in examples/User Interface directory for a more elaborate example
*   buttonitem_example.py - view with button items
*   lorem_generator - textview example
*   table_example1,2,3,4 - tableview examples
    - from forum
        - file navigation https://github.com/dgelessus/filenav/blob/master/litenav.py
        - fill rows based on the characters that are entered on textfield
            - https://forum.omz-software.com/topic/4328/modules-of-pythonista-displayed-with-help
*   webview1,2 - webview examples
    - running javascript example https://gist.github.com/encela95dus/3b672b4119b598064d2c943158fabaad
*   dialog examples
    - editlist_dialog_test.py
    - form_dialog_with_sections.py
    - multiselection_list_dialog.py
    - pyui_pretty_print.py - file selection dialog
    - custom dialog from designer
        - https://gist.github.com/encela95dus/73431fef1f00c462c3bee0551bd14be8
*   image manipulation
    - creating image    
        - imagecontext1.py 
            - creating images by drawing shapes and copying images
            - show it on console and save it in a file
        - imagecontext2.py - drawing rotated text (using GState and coordinate transformation)
        - imagecontext3.py - drawing a polygon
        - imagecontext4.py - drawing an image inside a polygon
    - basic_image_transform.py 
    - create image by taking snapshot of a view
        -  https://forum.omz-software.com/topic/4554/saving-console-display-to-an-image
    - omz gists for image manipulation
        - https://gist.github.com/omz/61373e17a7a450f2eb9f2b2b43ca2b5f
        - https://gist.github.com/omz/a7c5f310e1c8b829a5a613cd556863d4
    - creating images using designer
        - https://forum.omz-software.com/topic/4288/creating-images-using-designer-by-combining-images-texts-shapes/1
*   customview examples
    - customview1.py, radio_button.py  
    - custonview_imagemask.py - drawing a masked image (image inside a polygon) in a custom view
    - interactive drawing in customview - see sketch.py in examples directory
    - update functionality examples digitalclock.py, stopwatch.py, analogclock
    - from forum
        - UI components https://github.com/jsbain/uicomponents
        - UI tools in  Pythonista Tools https://github.com/Pythonista-Tools/Pythonista-Tools/blob/master/UI.md
        - update functionality
            - https://forum.omz-software.com/topic/5078/filling-tableview-gradually/2
            - for animations https://forum.omz-software.com/topic/4671/scripter-for-scene-and-other-updates
*   animation examples
    - animate1.py - animating color
    - animation2.py - animating scale, alpha and move
    - transform playground https://forum.omz-software.com/topic/2268/view-transform-origin
    - viewslide.py
    - delay_test.py
    - from forum
        -  https://forum.omz-software.com/topic/3504/lab-ui-animate-sliding-in-views
        -  gstate  https://forum.omz-software.com/topic/3180/understanding-ui-transform-rotation
*   navigationview example
    - navigationview_example.py, navtest_mainview, navtest_subview1,2
    - navigation view from pyui templates
        - https://gist.github.com/encela95dus/1ea94076e60e4d58f8a92915ce3d3e0d
*   scrollview - from forum
    - https://forum.omz-software.com/topic/2164/using-a-scroll-view-to-prevent-a-form-being-obscured-by-the-keyboard/7
    - https://forum.omz-software.com/topic/2410/horizonally-scrolling-textview
    - https://forum.omz-software.com/topic/3642/print-console-in-textview-or-scrollview       
*   mapview - from forum
    - https://gist.github.com/omz/451a6685fddcf8ccdfc5
    - https://forum.omz-software.com/topic/3507/need-help-for-calling-an-objective_c-function/2
    - https://forum.omz-software.com/topic/3511/show-on-a-map-the-chronological-route-of-your-photos/1
    - https://forum.omz-software.com/topic/4990/display-thumbs-of-your-photos-at-their-locations-on-a-map/1  
*   scene examples
    - animation examples in examples directory
    - games examples in examples directory
    - basic_nodes.py
    - change_attributes.py
    - change_positions.py 
    - update_example.py
    - scene_action1,2,3
    - textanimation.py
    - textanimation_wayy.py
    - scene_viewexample.py - scene embedded in a view
    - digital_watch.py, stop_watch.py - more examples on update
    - action_based_timer.py
    - animations from forum
        - planet motion https://forum.omz-software.com/topic/3754/show-all-scene-child-nodes
        - pendulum motion https://forum.omz-software.com/topic/3312/labelsprite-rotate_by-problem
        - https://forum.omz-software.com/topic/4284/how-do-i-make-a-full-screen-button-and-handle-button-down-and-button-up-events/6
    - games from forum
        - pong https://forum.omz-software.com/topic/3367/drawing-with-pythonistas-modules
        - cards   https://forum.omz-software.com/topic/4856/can-someone-turn-this-script-into-a-node-tutorial-please
        - word game   https://forum.omz-software.com/topic/4790/boggle-app-need-help-changing-labels-3x-in-a-function/9
    - shader
        - shader_example1.py - basic example to run shaders
        - template_shadertoy.py - template to run shadertoy examples
           - https://www.shadertoy.com/ contains a large collection of shader examples 
        - from forum
            - an introductory online book on shaders to learn shaders
                - https://thebookofshaders.com/
            - https://forum.omz-software.com/topic/3274/fast-color-change-animation-of-a-shape
*   simple tools  - to be added to editor action menu 
    - clipboard_image_on_console
    - clipboard_image_share.py
    - clipboard_view_edit_save.py
*   editor action - tools using editor module, to be added to editor action menu 
    - backup_editor.py - create a copy of file 
    - comment_uncomment.py
    - display_editor_path.py
    - pyui_pretty_print.py
    - preview_markup.py
    - preview_html.py
*   appex examples
    - convert_to_gray_image.py
  
