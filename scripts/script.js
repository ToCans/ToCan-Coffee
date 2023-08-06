// Makes more sense to load image first
let slideindex = 0;
let image = document.querySelectorAll('img');

function image_scroller() {
	let image_num = image.length;

	// Going through scrolling
	if (slideindex == image_num) {
		slideindex = 0;
	}
	if (slideindex < image_num) {
		for (let counter = 0; counter < image_num; counter++) {
			if (counter != slideindex) {
				image[counter].style.display = 'none';
			}
		}
		image[slideindex].style.display = 'flex';
		image[slideindex].style.animation = 'opacity-in 1000ms ease-in';
	}

	slideindex++;
	// 15 Seconds per image
	setTimeout(image_scroller, 15000);
}

image_scroller();

function offset_calcs() {
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

	if (window.matchMedia('(max-width: 768px)').matches) {
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
// Init Setup for Image Scroller Function
window.onload = offset_calcs();
//screen.orientation.onchange = offset_calcs();
window.addEventListener('resize', offset_calcs);
