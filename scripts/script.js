function offset_calcs() {
    // Definitions of Main Menu
    let basics_main_menu = document.getElementById('basics-tab').getBoundingClientRect();
    let recipes_main_menu = document.getElementById('recipes-tab').getBoundingClientRect();
    let equipment_main_menu = document.getElementById('equipment-tab').getBoundingClientRect();
    let tools_main_menu = document.getElementById('tools-tab').getBoundingClientRect();
    if (window.matchMedia('(max-width: 768px)').matches) {
        // Definition of X Offsets
        basic_menu_offset_x = -basics_main_menu.x + 'px';
        recipes_menu_offset_x = -recipes_main_menu.x + 'px';
        equipment_menu_offset_x = -equipment_main_menu.x + 'px';
        tools_menu_offset_x = -tools_main_menu.x + 'px';
    } else {
        basic_menu_offset_x = '-87.5px';
        recipes_menu_offset_x = '-87.5px';
        equipment_menu_offset_x = '-87.5px';
        tools_menu_offset_x = '-87.5px';
    }
    // Applying Offset
    document.getElementById('basics-sub').style.marginLeft = basic_menu_offset_x;
    document.getElementById('recipes-sub').style.marginLeft = recipes_menu_offset_x;
    document.getElementById('equipment-sub').style.marginLeft = equipment_menu_offset_x;
    document.getElementById('tools-sub').style.marginLeft = tools_menu_offset_x;
}

function image_scroller() {
    let image_num = image.length;

    // Init Hiding all pictures
    for (let counter = 0; counter < image_num; counter++) {
        image[counter].style.display = 'none';
    }
    // Going through scrolling
    if (slideindex == image_num) {
        slideindex = 0;
    }
    if (slideindex < image_num) {
        image[slideindex].style.display = 'flex';
    }
    if (window.matchMedia('(min-width: 768px)').matches) {
        image[slideindex].style.animation = 'opacity-in 500msms ease-in forwards';
    }
    slideindex++;
    setTimeout(image_scroller, 15000);
}

// Main running area
// Init Setup for Image Scroller Function
document.addEventListener('DOMContentLoaded', function (event) {
    offset_calcs();
});
window.addEventListener('resize', offset_calcs);
let slideindex = 0;
let image = document.querySelectorAll('img');
image_scroller();
