const startWordSearch  = (word)=> {
            const duckDuckGoURL = `https://duckduckgo.com/?q=${encodeURIComponent(word)}`;
            window.open(duckDuckGoURL, '_blank'); 
        }

     

$(document).ready(
	function(handler){


var selectSection = (name)=>{
	// hide all sections 
	console.debug("Selecting section....",name);
	$(".page-section").hide(0);
	let target_section = "#"+name+"-section";
	$(target_section).fadeIn();

};

var section_selector_clicked = function (event){
	let section_name = $(this).data("section");
	console.debug("Switching to section , " , section_name , $(this).html);
	selectSection(section_name);
};


		console.log("Prepping page...");





		// STICKY NAV 
let lastScrollTop = 0;
const navbar = document.querySelector('.navigation-bar');

window.addEventListener('scroll', function() {
    const currentScroll = window.pageYOffset || document.documentElement.scrollTop;

    if (currentScroll > lastScrollTop) {
        // Scroll Down
        navbar.style.top = "-50px"; // Adjust based on navbar height
    } else {
        // Scroll Up or at the top
        navbar.style.top = "0";
    }

    lastScrollTop = currentScroll <= 0 ? 0 : currentScroll;
});



//  section selection feature

$(".section-selector").click(section_selector_clicked);

// show the profile section 

selectSection("profile");


// trigger word search on click 
$(".word-search-on-click").click(function(event){
	// when the element is clicked a word search of the 
	// text in data-word is searched 
	let text = $(this).data("word");
	startWordSearch(text);


})
	})



