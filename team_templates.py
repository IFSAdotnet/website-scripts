from string import Template
person = Template('''[fusion_builder_column type="1_3" layout="1_3" spacing="50px" center_content="yes" link="" 
target="_self" min_height="" hide_on_mobile="small-visibility,medium-visibility,large-visibility" class="" id=""
background_color="" background_image="" background_image_id="" background_position="left top"
background_repeat="no-repeat" hover_type="zoomin" border_size="1" border_color="#006633" border_style="solid"
border_position="all" box_shadow="no" box_shadow_blur="0" box_shadow_spread="0" box_shadow_color=""
box_shadow_style="" animation_type="" animation_direction="left" animation_speed="0.3" animation_offset="" 
first="true" last="false" padding_right="15" padding_top="15" padding_bottom="15" padding_left="15"
border_radius_top_left="7" border_radius_top_right="7" border_radius_bottom_left="7"
border_radius_bottom_right="7"]

[fusion_person name="$name" title="$job_title" picture="$pic_url" picture_id="" pic_link="$pic_link" linktarget="_self"
pic_style="" pic_style_blur="" pic_style_color="" pic_bordersize="" pic_bordercolor="" pic_borderradius="10px"
hover_type="none" background_color="" content_alignment="" icon_position="bottom" social_icon_boxed="yes"
social_icon_boxed_radius="" social_icon_color_type="" social_icon_colors="" social_icon_boxed_colors=""
social_icon_tooltip="" blogger="" deviantart="" digg="" dribbble="" dropbox="" facebook="" flickr="" forrst=""
instagram="" linkedin="" myspace="" paypal="" pinterest="" reddit="" rss="" skype="" soundcloud="" spotify=""
tumblr="" twitter="" vimeo="" vk="" whatsapp="" xing="" yahoo="" yelp="" youtube="" email="$email" show_custom="yes"
hide_on_mobile="small-visibility,medium-visibility,large-visibility" class="" id="$name_link" /]
[/fusion_builder_column]''')

group = Template('''

[fusion_title hide_on_mobile="small-visibility,medium-visibility,large-visibility" class="" id="$group_link"
 content_align="left" size="1" font_size="" line_height="" letter_spacing="" margin_top="" margin_bottom=""
  margin_top_mobile="" margin_bottom_mobile="" text_color="" style_type="default" sep_color=""]
$group_title
[/fusion_title]
''')



head = Template('''[fusion_builder_container hundred_percent="no" equal_height_columns="no" menu_anchor=""
hide_on_mobile="small-visibility,medium-visibility,large-visibility" class="" id="" background_color=""
background_image="" background_position="center center" background_repeat="no-repeat" fade="no" 
background_parallax="none" parallax_speed="0.3" video_mp4="" video_webm="" video_ogv="" video_url=""
video_aspect_ratio="16:9" video_loop="yes" video_mute="yes" overlay_color="" video_preview_image="" border_size=""
border_color="" border_style="solid" padding_top="" padding_bottom="" padding_left="" padding_right=""]

''')
tail = Template('''[/fusion_builder_row]
[/fusion_builder_container]''')
