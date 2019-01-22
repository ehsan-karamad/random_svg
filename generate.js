const dim = 40;
noise = dim / 20;
const max_noise_items = 30
const svg_height = dim;
const svg_width = dim;
const fs = require('fs');

var count = 2000;

function svg(contents) {
	return `<svg xmlns="http://www.w3.org/2000/svg" height="${svg_height}" width="${svg_width}">
	 ${contents.join(" ")} </svg>`;
}

function svg_circle(cx, cy, r, sw, col) {
  return `<circle cx="${cx}" cy="${cy}" r="${r}" stroke="#${col}${col}${col}" stroke-width="${sw}"/>`;
}

function svg_rect(x, y, w, h, sw, col) {
	return `<rect width="${w}" height="${h}" stroke="#${col}${col}${col}" stroke-width="${sw}" x="${x}" y="${y}" />`;
}

// draw circles
function rand_int(n, m) {
	return n + Math.floor(Math.random() * (m - n));
}

csvgs = [];
for (var i = 0; i < count; ++i) {
	var contents = [];
	contents.push(svg_circle(
		rand_int(dim / 2 - noise, dim / 2 + noise),
		rand_int(dim / 2 - noise, dim / 2 + noise),
		rand_int(dim / 4, dim / 2 - noise),
		rand_int(1, 4),
		rand_int(0, 255).toString(16)
		));
	var n = rand_int(0, max_noise_items);
	for (var j = 0; j < n; ++j) {
		contents.push(svg_rect(
			rand_int(0, dim),
			rand_int(0, dim),
			rand_int(1, noise),
			rand_int(1, noise),
			rand_int(1, 2)
			));
	}
	csvgs.push(svg(contents));
}
var index = 0;
csvgs.forEach((svg) => {
	fs.writeFile(`c_${index++}.svg`, svg);
});

rsvgs = [];
for (var i = 0; i < count; ++i) {
	var contents = [];
	contents.push(
		svg_rect(
			rand_int(0, dim / 4),
			rand_int(0, dim / 4),
			rand_int(dim / 2, dim * 3 / 4),
			rand_int(dim / 2, dim * 3 / 4),
			rand_int(1, 4),
			rand_int(0, 255).toString(16)));

	var n = rand_int(0, max_noise_items);
	for (var j = 0; j < n; ++j) {
		contents.push(svg_circle(
		rand_int(0, dim),
		rand_int(0, dim),
		rand_int(0, noise),
		rand_int(1, 2),
		rand_int(0, 255).toString(16)));
	}
	rsvgs.push(svg(contents));
}

index = 0;
rsvgs.forEach((svg) => {
	fs.writeFile(`r_${index++}.svg`, svg);
});
