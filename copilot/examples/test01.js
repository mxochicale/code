// find all images withouth alternative text
// and give them a red border
function process() {
	var images = find("//img[not(@alt)]");
	for (var i = 0; i < images.length; i++) {
		images[i].setAttribute("style", "border: 3px solid red");
	}
}