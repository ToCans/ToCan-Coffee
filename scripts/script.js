function offset_calcs() {
    if (window.matchMedia('(max-width: 768px)').matches) {
        // Definitions of Main Menu
        let basics_main_menu = document.getElementById('basics-tab');
        let recipes_main_menu = document.getElementById('recipes-tab');
        let equipment_main_menu = document.getElementById('equipment-tab');
        let tools_main_menu = document.getElementById('tools-tab');

        // Definition of X Offsets
        let basic_menu_offset_x = -basics_main_menu.getBoundingClientRect().x + 'px';
        let recipes_menu_offset_x = -recipes_main_menu.getBoundingClientRect().x + 'px';
        let equipment_menu_offset_x = -equipment_main_menu.getBoundingClientRect().x + 'px';
        let tools_menu_offset_x = -tools_main_menu.getBoundingClientRect().x + 'px';

        // Applying Offset
        document.getElementById('basics-sub').style.marginLeft = basic_menu_offset_x;
        document.getElementById('recipes-sub').style.marginLeft = recipes_menu_offset_x;
        document.getElementById('equipment-sub').style.marginLeft = equipment_menu_offset_x;
        document.getElementById('tools-sub').style.marginLeft = tools_menu_offset_x;
    } else {
        document.getElementById('basics-sub').style.marginLeft = '-87.5px';
        document.getElementById('recipes-sub').style.marginLeft = '-87.5px';
        document.getElementById('equipment-sub').style.marginLeft = '-87.5px';
        document.getElementById('tools-sub').style.marginLeft = '-87.5px';
    }
}

// Main running area
document.addEventListener('DOMContentLoaded', function (event) {
    offset_calcs();
});
window.addEventListener('resize', offset_calcs);
