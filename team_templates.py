from string import Template
person = Template('''[fusion_builder_column_inner type="1_3" layout="1_3" spacing="" center_content="no" hover_type="none"
 link="" target="_self" min_height="" hide_on_mobile="small-visibility,medium-visibility,large-visibility" class="" id="" background_color="" background_image="" 
background_position="left top" background_repeat="no-repeat" border_size="0" border_color="" border_style="solid" border_position="all" 
border_radius="" box_shadow="no" dimension_box_shadow="" box_shadow_blur="0" box_shadow_spread="0" box_shadow_color="" box_shadow_style="" padding_top="" 
padding_right="" padding_bottom="" padding_left="" 
dimension_margin="" animation_type="" animation_direction="left" animation_speed="0.3" animation_offset="" last="no"]


[fusion_person name="$name" title="$job_title" picture="$pic_url" picture_id="" pic_link="$pic_link" linktarget="_self" 
pic_style="" pic_style_blur="" pic_style_color="" pic_bordersize="" pic_bordercolor="" pic_borderradius="" 
hover_type="none" background_color="" content_alignment="" icon_position="" social_icon_boxed="" 
social_icon_boxed_radius="" social_icon_color_type="" social_icon_colors="" social_icon_boxed_colors=""
social_icon_tooltip="" blogger="" deviantart="" digg="" dribbble="" dropbox="" facebook="" flickr="" forrst="" 
googleplus="" instagram="" linkedin="" myspace="" paypal="" pinterest="" reddit="" rss=""
skype="" soundcloud="" spotify="" tumblr="" twitter="" vimeo="" vk="" whatsapp="" xing="" yahoo="" yelp="" youtube="" 
email="$email" show_custom="no" 
hide_on_mobile="small-visibility,medium-visibility,large-visibility" class="" id="$name_link"]

$description

[/fusion_person]
[/fusion_builder_column_inner]''')

group_head = Template('''

[fusion_title hide_on_mobile="small-visibility,medium-visibility,large-visibility" class="" id="$group_link" content_align="left" size="1" font_size="" line_height="" letter_spacing="" margin_top="" margin_bottom="" margin_top_mobile="" margin_bottom_mobile="" text_color="" style_type="default" sep_color=""]
$group_title
[/fusion_title]

[fusion_builder_row_inner]''')
group_tail = Template('''[/fusion_builder_row_inner]''')


head = Template('''[fusion_builder_container hundred_percent="no" hundred_percent_height="no" hundred_percent_height_scroll="no" hundred_percent_height_center_content="yes" equal_height_columns="no"
 menu_anchor="" hide_on_mobile="small-visibility,medium-visibility,large-visibility" status="published" publish_date="" class="" id="" background_color="" 
background_image="" background_position="center center" background_repeat="no-repeat" fade="no" background_parallax="none" enable_mobile="no" parallax_speed="0.3" video_mp4="" video_webm="" video_ogv="" video_url="" video_aspect_ratio="16:9" video_loop="yes" video_mute="yes"
 video_preview_image="" border_size="" border_color="" border_style="solid" margin_top="" margin_bottom="" padding_top="" padding_right="" padding_bottom="" padding_left=""]
[fusion_builder_row]
[fusion_builder_column type="1_1" layout="1_1" spacing="" center_content="no" link="" target="_self" min_height="" hide_on_mobile="small-visibility,medium-visibility,large-visibility"
 class="" id="" background_color="" background_image="" background_image_id="" 
background_position="left top" background_repeat="no-repeat" hover_type="none"
 border_size="0" border_color="" border_style="solid" border_position="all" 
border_radius="" box_shadow="no" dimension_box_shadow="" box_shadow_blur="0"
 box_shadow_spread="0" box_shadow_color="" box_shadow_style="" padding_top=""
 padding_right="" padding_bottom="" padding_left="" margin_top="" margin_bottom="" 
animation_type="" animation_direction="left" animation_speed="0.3" 
animation_offset="" last="no"]
''')
tail = Template('''[/fusion_builder_column]
[/fusion_builder_row]
[/fusion_builder_container]''')
